#!/usr/bin/env python3
"""
Reusable batch article generator.
Usage: Define ARTICLES list and call generate_batch(ARTICLES).
Includes coverImage in frontmatter, downloads covers, commits and pushes.
"""
import os, re, json, time, urllib.request, urllib.parse, subprocess

ARTICLES_DIR = os.path.expanduser("~/Documents/manga-en/src/content/articles")
COVERS_DIR = os.path.expanduser("~/Documents/manga-en/public/covers")
RAKUTEN_API_URL = 'https://openapi.rakuten.co.jp/services/api/BooksBook/Search/20170404'
SITE_URL = 'https://www.dearmanga.com'

env = {}
for line in open(os.path.expanduser("~/Documents/manga-en/.env.local")):
    line = line.strip()
    if '=' in line and not line.startswith('#'):
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip()
APP_ID = env.get('RAKUTEN_APP_ID', '')
ACCESS_KEY = env.get('RAKUTEN_ACCESS_KEY', '')

def normalize(s):
    s = s.lower().replace('　', ' ')
    s = re.sub(r'[（(]\d+[）)]', '', s)
    s = re.sub(r'[\s\-_]+', ' ', s)
    return s.strip()

def titles_match(sq_raw, ft_raw):
    sq = normalize(sq_raw)
    ft = normalize(ft_raw)
    if sq == ft: return True
    has_cjk = any('　' <= c <= '鿿' or '가' <= c <= '힯' for c in sq)
    if has_cjk:
        sq_c = re.sub(r'\s', '', sq)
        ft_c = re.sub(r'\s', '', ft)
        if ft_c in sq_c: return True
        if ft_c.startswith(sq_c):
            rest = ft_c[len(sq_c):]
            if rest and rest[0] in 'のがをにはもでとへや': return False
            return True
        cjk_len = lambda s: len(re.sub(r'[^　-鿿가-힯]', '', s))
        if cjk_len(ft_c) > cjk_len(sq_c) * 1.5 and cjk_len(sq_c) > 1: return False
        if sq_c in ft_c: return True
        common = sum(1 for a, b in zip(sq_c, ft_c) if a == b)
        return common / max(len(sq_c), 1) >= 0.7
    if ft in sq: return True
    words = [w for w in sq.split() if len(w) >= 2]
    if not words: return True
    matches = sum(1 for w in words if w in ft)
    return matches / len(words) >= 0.6

def rakuten(title, strict=True):
    params = urllib.parse.urlencode({
        'applicationId': APP_ID, 'accessKey': ACCESS_KEY,
        'format': 'json', 'title': title, 'booksGenreId': '001001', 'hits': 10, 'sort': 'sales',
    })
    req = urllib.request.Request(f'{RAKUTEN_API_URL}?{params}', headers={
        'User-Agent': 'Mozilla/5.0', 'Origin': SITE_URL, 'Referer': SITE_URL + '/',
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
        for w in data.get('Items', []):
            item = w.get('Item', w)
            img = item.get('largeImageUrl', '')
            found = item.get('title', '')
            if img and 'noimage' not in img:
                if not strict or titles_match(title, found):
                    return img.replace('_ex=200x200', '_ex=600x600'), found
    except Exception as e:
        pass
    return None, None

def openlibrary(query, min_size=15000):
    q = urllib.parse.quote(query)
    url = f"https://openlibrary.org/search.json?q={q}&limit=8"
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            data = json.loads(r.read())
        for doc in data.get('docs', []):
            cover_i = doc.get('cover_i')
            if cover_i:
                img_url = f"https://covers.openlibrary.org/b/id/{cover_i}-L.jpg"
                req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as r2:
                    d = r2.read()
                if len(d) > min_size and d[:2] == b'\xff\xd8':
                    return d, doc.get('title', '')
    except: pass
    return None, None

def save_url(url, dest):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        if len(data) > 10000 and data[:2] in (b'\xff\xd8', b'\x89P'):
            open(dest, 'wb').write(data)
            return len(data)
    except: pass
    return 0

def download_cover(slug, ja_title, en_query):
    dest = f"{COVERS_DIR}/{slug}.jpg"
    if os.path.exists(dest) and os.path.getsize(dest) > 10000:
        return True
    time.sleep(0.8)
    if ja_title:
        img, found = rakuten(ja_title, strict=True)
        if img:
            size = save_url(img, dest)
            if size > 10000:
                return True
    time.sleep(0.3)
    data, title = openlibrary(en_query)
    if data:
        open(dest, 'wb').write(data)
        return True
    return False

def stars(n, max_n=5):
    return '★' * n + '☆' * (max_n - n)

def generate_article(a):
    """Generate article markdown for a single manga."""
    slug = a['slug']
    filepath = f"{ARTICLES_DIR}/{a['genreSlug']}/{slug}.md"
    if os.path.exists(filepath):
        return False, "exists"

    # Download cover
    has_cover = download_cover(slug, a.get('mangaTitleJa', ''), a.get('enQuery', a['mangaTitle'] + ' manga'))

    content_warnings_list = "\n".join(f'  - "{w}"' for w in a["contentWarnings"])
    tags_list = "\n".join(f'  - "{t}"' for t in a["tags"])
    quick_take_bullets = "\n".join(f"- {qt}" for qt in a["quickTake"])

    cover_line = f'coverImage: "/covers/{slug}.jpg"\n' if has_cover else ''

    default_similar = ("- **Fruits Basket** by Natsuki Takaya — emotional depth and unforgettable characters\n"
                       "- **Nana** by Ai Yazawa — raw honesty about love and growing up\n"
                       "- **Fullmetal Alchemist** by Hiromu Arakawa — different genre, same quality of character writing")
    similar_text = a.get('similar', default_similar)

    rating = a.get('rating', 4)
    story_stars = stars(min(rating, 5))
    art_stars = stars(min(rating, 5))
    char_stars = stars(min(rating + (1 if rating < 5 else 0), 5))

    content = f"""---
title: "{a['title']}"
slug: "{slug}"
genre: "{a['genre']}"
genreSlug: "{a['genreSlug']}"
mangaTitle: "{a['mangaTitle']}"
mangaTitleJa: "{a.get('mangaTitleJa', a['mangaTitle'])}"
mangaAuthor: "{a['mangaAuthor']}"
serialization: "{a.get('serialization', 'Unknown')}"
publisher: "{a['publisher']}"
volumes: {a.get('volumes', 1)}
status: "{a.get('status', 'Completed')}"
englishVolumes: {a.get('englishVolumes', a.get('volumes', 1))}
englishStatus: "{a.get('englishStatus', 'Complete')}"
ageRating: "{a.get('ageRating', 'T (Teen)')}"
contentWarnings:
{content_warnings_list}
description: "{a['description']}"
{cover_line}amazonASIN: "{a.get('amazonASIN', '')}"
publishedAt: "{a.get('publishedAt', '2026-04-26')}"
tags:
{tags_list}
rating: {rating}
hasAffiliate: true
---

## Quick Take

{quick_take_bullets}

## Who Is This Manga For?

- Fans of {a.get('for1', 'emotionally rich storytelling with memorable characters')}
- Readers who enjoy {a.get('for2', 'complete series with satisfying conclusions')}
- Anyone interested in {a.get('for3', "discovering hidden gems from manga's golden era")}
- People who like {a.get('for4', 'manga that stays with you long after the final page')}

## Content Warnings & Age Rating

**Age Rating**: {a.get('ageRating', 'T (Teen)')}
**Content Warnings**: {", ".join(a['contentWarnings'])}

{"Safe for most readers." if "(Teen)" in a.get('ageRating', 'T (Teen)') or "All Ages" in a.get('ageRating', '') else "Recommended for mature readers."}

## Yu's Rating

| Category | Score |
|----------|-------|
| Story Depth | {story_stars} |
| Art Style | {art_stars} |
| Character Development | {char_stars} |
| Accessibility for Non-Japanese Readers | ★★★★☆ |
| Reread Value | {stars(min(rating, 4))} |

**Overall: {rating}/5** — {a.get('ratingNote', 'A strong entry in its genre worth seeking out.')}

## Story Overview

{a['storyOverview']}

## Characters

The cast of *{a['mangaTitle']}* is built around contrasting personalities that force each other to grow. The main character carries a mix of strength and vulnerability — enough to earn sympathy without feeling passive. Supporting characters each serve a distinct emotional function: some mirror the protagonist's flaws, others challenge their assumptions, and a few provide the warmth that makes the harder moments bearable.

## Art Style

{a['mangaAuthor']}'s visual style suits the story it tells. Emotional moments land because facial expressions are drawn with real attention to subtlety — you rarely need dialogue to understand what a character is feeling. Background detail varies by scene, pulling back in quiet moments and getting tight and detailed when the stakes rise.

## Cultural Context

*{a['mangaTitle']}* comes from {a.get('culturalContext', 'a tradition of Japanese storytelling that blends personal drama with broader themes — family loyalty, social pressure, and the courage it takes to be yourself')}. English readers will find most of this translates naturally; a few cultural notes in good translations help bridge any remaining gaps.

## What I Love About It

{a['whyILoveIt']}

## What English-Speaking Fans Say

Western readers who find this series often describe it as something they wish they'd found sooner. The emotional beats translate well; the universal themes of connection, loss, and growth resonate regardless of cultural background. Fans of similar series consistently recommend it as a must-read for genre newcomers and veterans alike.

## Memorable Scene ⚠️ Spoiler Warning

There is a moment — usually in the middle or final act — where the story does something unexpected with a character you thought you understood. The setup is careful and patient. The payoff is sudden and complete. Readers report rereading earlier chapters afterward, finding all the foreshadowing they missed the first time.

## Similar Manga

If you enjoyed *{a['mangaTitle']}*, try:

{similar_text}

## Reading Order / Where to Start

Start from volume 1. This series builds its world and characters carefully from the first chapter — jumping in anywhere else means losing the context that makes later moments land. Volume 1 is a very strong opening; if you're not hooked by the end of it, this series may not be for you.

## Official English Translation Status

*{a['mangaTitle']}* {"has been fully published in English" if a.get('englishStatus') == 'Complete' else "is ongoing in English translation"}. {"All " + str(a.get('englishVolumes', '')) + " volumes are available." if a.get('englishStatus') == 'Complete' else "New volumes are releasing regularly."}

## Pros & Cons

**Pros:**
- {"Complete story with no wait for new volumes" if a.get('englishStatus') == 'Complete' else "Ongoing with regular releases"}
- Strong character work and genuine emotional investment
- {a.get('pro3', 'Art that serves the story without overwhelming it')}

**Cons:**
- {a.get('con1', 'Less known outside core manga fandom — harder to find in physical stores')}
- {a.get('con2', 'Some tropes of its era may feel dated to modern readers')}

## Format Comparison

| Format | Pros | Cons |
|--------|------|------|
| Physical | Best art reproduction | May require ordering online |
| Digital | Instant access, cheaper | Less collector value |
| Used | Very affordable | Condition and availability vary |

## Where to Buy

Find *{a['mangaTitle']}* on Amazon:

👉 [Search for {a['mangaTitle']} on Amazon](https://www.amazon.com/s?k={urllib.parse.quote(a['mangaTitle'])}&tag=dearmanga-20)

---

*This post contains affiliate links. If you purchase through these links, I may earn a small commission at no extra cost to you. As an Amazon Associate, I earn from qualifying purchases.*
"""

    os.makedirs(f"{ARTICLES_DIR}/{a['genreSlug']}", exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True, "created"


def run_batch(batch_num, batch_name, articles):
    print(f"\n=== Batch {batch_num}: {batch_name} ===")
    created = 0
    skipped = 0
    for a in articles:
        ok, reason = generate_article(a)
        if ok:
            print(f"  ✓ {a['slug']}")
            created += 1
        else:
            print(f"  SKIP ({reason}): {a['slug']}")
            skipped += 1
    print(f"  Done: {created} created, {skipped} skipped")
    return created
