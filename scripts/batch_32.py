#!/usr/bin/env python3
"""Batch 32 — 15 reviews: CLAMP shorts, Mizuki, Rumiko shorts, Urasawa shorts."""
import sys, os, random
from datetime import date, timedelta
sys.path.insert(0, os.path.dirname(__file__))
from batch_generator import run_batch

random.seed(20260429 + 32)
START = date(2024, 7, 18)
END = date(2026, 4, 28)
DAYS = (END - START).days
def pdate():
    return (START + timedelta(days=random.randint(0, DAYS))).isoformat()

ARTICLES = [
    {
        "slug": "miyuki-chan-wonderland",
        "title": "Miyuki-chan in Wonderland Review: CLAMP at Their Most Self-Indulgent",
        "genre": "Comedy / Fantasy", "genreSlug": "fantasy",
        "mangaTitle": "Miyuki-chan in Wonderland", "mangaTitleJa": "不思議の国の美幸ちゃん",
        "mangaAuthor": "CLAMP",
        "serialization": "Newtype", "publisher": "Kadokawa",
        "volumes": 1, "status": "Completed",
        "englishVolumes": 1, "englishStatus": "Complete",
        "ageRating": "M (Mature)",
        "contentWarnings": ["fanservice", "lgbtq-content", "sexual-themes"],
        "description": "CLAMP's sexy Alice-in-Wonderland fever dream — a single oversized volume of pure fanservice fantasy.",
        "tags": ["fantasy", "comedy", "clamp", "yuri", "lgbtq"],
        "rating": 3,
        "quickTake": [
            "CLAMP's most unapologetically horny work",
            "Yuri Alice in Wonderland with no plot to speak of",
            "Beautiful art in service of pure self-indulgence"
        ],
        "storyOverview": "Miyuki is a regular Japanese schoolgirl who keeps falling into alternate dimensions populated by gorgeous women trying to seduce her. Wonderland. The Looking Glass. The TV. Each chapter sends her into a new fantasy world where the tropes are recognizable but the cast is entirely women. CLAMP plays it straight as parody and beautifully as art.",
        "whyILoveIt": "Miyuki-chan is what happens when CLAMP decides to just have fun. The art is gorgeous, the gags are silly, and the whole thing knows exactly what it is. There's no deep meaning — it's a sketchbook of fantasies in manga form. As an experiment in genre, it's surprisingly committed.",
        "publishedAt": pdate()
    },
    {
        "slug": "shirahime-syo",
        "title": "Shirahime-Syo Review: CLAMP Goes Folkloric and Heartbreaking",
        "genre": "Drama / Fantasy", "genreSlug": "fantasy",
        "mangaTitle": "Shirahime-Syo: Snow Goddess Tales", "mangaTitleJa": "白姫抄",
        "mangaAuthor": "CLAMP",
        "serialization": "Various", "publisher": "Kodansha",
        "volumes": 1, "status": "Completed",
        "englishVolumes": 1, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["death", "tragedy"],
        "description": "Five Japanese folk tales reimagined by CLAMP as quiet tragedies of love, loss, and snow.",
        "tags": ["fantasy", "drama", "clamp", "anthology", "folklore"],
        "rating": 5,
        "quickTake": [
            "CLAMP's most underrated work",
            "Five short folk tales with breathtaking ink art",
            "Painterly, melancholy, perfect"
        ],
        "storyOverview": "Five short stories set in feudal Japan, each centered on snow. A hunter who loses his mother. A samurai who loves a woman who isn't human. A village priest who breaks his vow. Children who play games that go wrong. CLAMP draws each in monochrome ink-wash, with text laid out like classical poetry. The thread that binds them is the snow goddess Shirahime, who watches without judgment.",
        "whyILoveIt": "Shirahime-Syo is the most beautiful thing CLAMP has ever made. The art is restrained — almost no detail, just suggestion — and the stories are devastating. Each one is the size of a poem. I read it once a winter. It changes how you think about CLAMP, who we usually think of as maximalists. Here, they're masters of less.",
        "publishedAt": pdate()
    },
    {
        "slug": "suki-dakara-suki",
        "title": "Suki Dakara Suki Review: CLAMP's Pure Romance Side",
        "genre": "Romance / Slice-of-Life", "genreSlug": "romance",
        "mangaTitle": "Suki: A Like Story", "mangaTitleJa": "好き。だから好き",
        "mangaAuthor": "CLAMP",
        "serialization": "Cheese!", "publisher": "Shogakukan",
        "volumes": 3, "status": "Completed",
        "englishVolumes": 3, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["mild-romance", "mystery-elements"],
        "description": "A teacher and a student. A mysterious past. CLAMP's quietest romance — and one of their strangest.",
        "tags": ["romance", "shojo", "clamp", "mystery"],
        "rating": 4,
        "quickTake": [
            "CLAMP doing pure shojo romance",
            "Three-volume mystery box",
            "Surprisingly gentle for the studio"
        ],
        "storyOverview": "Hina is a sheltered high school girl who lives with her three teddy bears and rarely leaves the house. When the new homeroom teacher Asou Shiro moves in next door, Hina starts to feel something she's never felt before. But Asou has a secret about Hina's past — and the longer he stays close to her, the more dangerous things become for both of them.",
        "whyILoveIt": "Suki: A Like Story is CLAMP at their most contained. There's no apocalypse, no magic. Just a romance with a slowly unfolding mystery. Hina is sweet without being saccharine; Asou's secrets are revealed at exactly the right pace. It's a small story, perfectly told.",
        "publishedAt": pdate()
    },
    {
        "slug": "drug-and-drop",
        "title": "Drug and Drop Review: The CLAMP Sequel That Never Quite Ended",
        "genre": "Romance / Supernatural", "genreSlug": "fantasy",
        "mangaTitle": "Drug and Drop", "mangaTitleJa": "ドラッグ＆ドロップ",
        "mangaAuthor": "CLAMP",
        "serialization": "Young Ace", "publisher": "Kadokawa",
        "volumes": 2, "status": "Hiatus",
        "englishVolumes": 2, "englishStatus": "Ongoing",
        "ageRating": "T (Teen)",
        "contentWarnings": ["lgbtq-themes", "supernatural-violence"],
        "description": "The continuation of CLAMP's Legal Drug — Kazahaya and Rikuo are back, and the stakes are finally rising.",
        "tags": ["fantasy", "supernatural", "clamp", "lgbtq", "sequel"],
        "rating": 3,
        "quickTake": [
            "Legal Drug picks up after a 13-year hiatus",
            "On hold again — possibly forever",
            "Beautiful but frustrating for fans waiting on resolution"
        ],
        "storyOverview": "Kazahaya and Rikuo, the two pharmacy clerks with supernatural side jobs from CLAMP's earlier Legal Drug, return after a thirteen-year hiatus. The cases get bigger; the truth about Kazahaya's past starts surfacing. The dynamic between them deepens. And then CLAMP put it on hiatus again. As of writing, no signs of a continuation.",
        "whyILoveIt": "Drug and Drop is what CLAMP does when they want to revisit a beloved story. The art is more refined; the pacing is slower. The relationship between Kazahaya and Rikuo gets the breathing room it always needed. The frustration is just that it stops mid-arc. But the time we have with them is good.",
        "publishedAt": pdate()
    },
    {
        "slug": "akuma-kun",
        "title": "Akuma-kun Review: Mizuki's Demon-Summoning Boy Genius",
        "genre": "Supernatural / Adventure", "genreSlug": "horror",
        "mangaTitle": "Akuma-kun", "mangaTitleJa": "悪魔くん",
        "mangaAuthor": "Shigeru Mizuki",
        "serialization": "Various", "publisher": "Kodansha",
        "volumes": 8, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["supernatural-violence", "death", "occult-themes"],
        "description": "A boy genius summons demons to make a better world — Mizuki's other masterpiece besides Kitaro.",
        "tags": ["supernatural", "horror", "mizuki", "classic"],
        "rating": 5,
        "quickTake": [
            "Mizuki's other major series alongside Kitaro",
            "A genius child trying to fix the world via demons",
            "Multiple iterations across decades"
        ],
        "storyOverview": "Akuma-kun is a child prodigy who believes that humans alone can't fix the world. He summons Mephistopheles and uses occult knowledge to confront injustice. Across multiple iterations of the series — '60s, '80s, modern — the basic question remains the same: if our tools to fix things are evil, do we use them anyway? Mizuki revisits the character throughout his career.",
        "whyILoveIt": "Akuma-kun is one of Mizuki's most ambitious works. The premise — child genius using demons for good — is wild, but Mizuki treats the moral question seriously. Each iteration of the series engages with its time. Reading them in order is a tour through how Mizuki's worldview changed across decades.",
        "publishedAt": pdate()
    },
    {
        "slug": "hitler-mizuki",
        "title": "Hitler Review: Shigeru Mizuki's Biographical Manga",
        "genre": "Historical / Drama", "genreSlug": "slice-of-life",
        "mangaTitle": "Hitler", "mangaTitleJa": "劇画ヒットラー",
        "mangaAuthor": "Shigeru Mizuki",
        "serialization": "Big Comic", "publisher": "Shogakukan",
        "volumes": 1, "status": "Completed",
        "englishVolumes": 1, "englishStatus": "Complete",
        "ageRating": "M (Mature)",
        "contentWarnings": ["war", "antisemitism", "violence", "historical-atrocity"],
        "description": "Shigeru Mizuki tells the life of Adolf Hitler in a single restrained volume.",
        "tags": ["historical", "biography", "mizuki", "war"],
        "rating": 5,
        "quickTake": [
            "Mizuki tells the life of Hitler — quietly, terrifyingly",
            "From struggling artist to dictator",
            "An unsettling, essential biographical manga"
        ],
        "storyOverview": "Mizuki tells the life of Adolf Hitler from his time as a struggling Vienna painter to his suicide in the bunker. The book is unusually restrained — Mizuki refuses to caricature Hitler, even when it would be easier. He shows a small, defeated young man slowly transforming through ideology and luck. The horror comes from how plausible the rise feels.",
        "whyILoveIt": "Mizuki's Hitler is one of the most quietly disturbing manga I've read. Mizuki, who served in the Imperial Japanese Army and lost his arm in the war, wasn't writing this for excitement. He wanted to understand. The result is a biography that treats Hitler as a human being — which makes the trajectory all the more chilling.",
        "publishedAt": pdate()
    },
    {
        "slug": "kappa-no-sanpei",
        "title": "Kappa no Sanpei Review: Mizuki Goes Riverside",
        "genre": "Supernatural / Adventure", "genreSlug": "fantasy",
        "mangaTitle": "Kappa no Sanpei", "mangaTitleJa": "河童の三平",
        "mangaAuthor": "Shigeru Mizuki",
        "serialization": "Weekly Shonen Sunday", "publisher": "Shogakukan",
        "volumes": 7, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "All Ages",
        "contentWarnings": ["mild-supernatural-themes"],
        "description": "Mizuki's gentle yokai story about a country boy who befriends a kappa — and the death god watching them both.",
        "tags": ["supernatural", "yokai", "mizuki", "classic"],
        "rating": 4,
        "quickTake": [
            "Mizuki's gentlest yokai work",
            "Country-river setting feels deeply autobiographical",
            "Surprisingly philosophical for a kid-friendly series"
        ],
        "storyOverview": "Sanpei is a country boy who befriends Kappa Sanpei — a river spirit who looks just like him. Together, they navigate the spirit world, country life, and the attentions of a death god named Tanuki. Each volume is a gentle adventure, but the underlying themes — death, nature, what we owe each other — give it weight.",
        "whyILoveIt": "Kappa no Sanpei is Mizuki at his most pastoral. The country setting feels like the same place as NonNonBa. The kappa friendship is sweet without being syrupy. And the looming death god is one of Mizuki's most charming antagonists — patient, funny, never quite cruel. It's a perfect introduction to his work for younger readers.",
        "publishedAt": pdate()
    },
    {
        "slug": "rumic-world",
        "title": "Rumic World Review: Rumiko Takahashi's Short Story Collection",
        "genre": "Drama / Slice-of-Life", "genreSlug": "slice-of-life",
        "mangaTitle": "Rumic World", "mangaTitleJa": "るーみっくわーるど",
        "mangaAuthor": "Rumiko Takahashi",
        "serialization": "Various", "publisher": "Shogakukan",
        "volumes": 3, "status": "Completed",
        "englishVolumes": 3, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["mild-violence", "mature-themes"],
        "description": "Takahashi's early short stories collected — from comedy to horror to domestic drama.",
        "tags": ["drama", "slice-of-life", "takahashi", "anthology"],
        "rating": 4,
        "quickTake": [
            "Three volumes of Takahashi's early shorts",
            "Range from horror to slapstick comedy",
            "Reveals Takahashi as more versatile than her famous series suggest"
        ],
        "storyOverview": "Three volumes collecting Rumiko Takahashi's shorter work from her early career. The stories range widely: a horror about a lighthouse keeper, a comedy about a salaryman in a love hotel, a domestic drama about an aging couple. Reading them together, you see a Takahashi most people don't know — interested in mood, craft, and economy of storytelling.",
        "whyILoveIt": "Rumic World is the Takahashi I wish more people read. Without the long-running series structure, she gets to be precise. The horror story is quietly chilling. The comedy is sharper than Lum or Ranma. Every story ends exactly when it should. It changed how I think about her as an artist.",
        "publishedAt": pdate()
    },
    {
        "slug": "rumic-theater",
        "title": "Rumic Theater Review: Takahashi's Adult Drama Anthology",
        "genre": "Drama / Slice-of-Life", "genreSlug": "slice-of-life",
        "mangaTitle": "Rumic Theater", "mangaTitleJa": "Pの悲劇 / 1 OR W",
        "mangaAuthor": "Rumiko Takahashi",
        "serialization": "Big Comic Original", "publisher": "Shogakukan",
        "volumes": 2, "status": "Completed",
        "englishVolumes": 2, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["domestic-issues", "mature-themes"],
        "description": "Takahashi's serialized adult dramas, mostly about women navigating marriage, infidelity, and ordinary life.",
        "tags": ["drama", "slice-of-life", "josei", "takahashi"],
        "rating": 4,
        "quickTake": [
            "Takahashi writing for adult women",
            "Themes of marriage, work, and aging",
            "Underrated late entry in her bibliography"
        ],
        "storyOverview": "Two volumes of one-shot stories Takahashi wrote for Big Comic Original — a magazine for adult readers. Each story features a woman navigating a moment of ordinary crisis. A wife discovers her husband's affair. A widow rediscovers herself. A new mother questions everything. Takahashi treats every situation with the same generous, ironic eye.",
        "whyILoveIt": "Rumic Theater is what Takahashi does when she's allowed to write about adults. The stories are quieter than her famous series, but they're more emotionally precise. Watching her capture middle age — the disappointments, the small joys, the way the world stops looking at you — is a treat. It's an essential part of her catalog.",
        "publishedAt": pdate()
    },
    {
        "slug": "one-pound-glass",
        "title": "One Pound Glass Review: Boxing Drama with a Twist",
        "genre": "Sports / Drama", "genreSlug": "sports",
        "mangaTitle": "One Pound Glass", "mangaTitleJa": "1ポンドのガラス",
        "mangaAuthor": "Tetsuyuki Asakawa",
        "serialization": "Big Comic Spirits", "publisher": "Shogakukan",
        "volumes": 5, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["violence", "physical-injury", "mental-illness"],
        "description": "A boxer with a glass jaw decides to keep fighting anyway — and discovers the cost of refusing to quit.",
        "tags": ["sports", "boxing", "drama", "seinen"],
        "rating": 4,
        "quickTake": [
            "Boxing manga about resilience without glamour",
            "Kept fighting after a doctor told him to stop",
            "Quiet but powerful seinen entry"
        ],
        "storyOverview": "Touya is a promising young boxer with one fatal flaw — his jaw is glass. A single solid hit, and he goes down. After a serious injury, doctors tell him to quit. He doesn't. The manga follows what happens to a person who decides their body's limit is a suggestion. It's not triumphant. It's careful, painful, and honest.",
        "whyILoveIt": "One Pound Glass is the boxing manga I wish more people knew. It's quieter than Hajime no Ippo, more vulnerable than Ashita no Joe. Touya isn't a chosen one. He's a stubborn person making questionable choices, and the manga refuses to romanticize them. The ending earns its complications.",
        "publishedAt": pdate()
    },
    {
        "slug": "mujirushi",
        "title": "Mujirushi Review: Naoki Urasawa Goes to the Louvre",
        "genre": "Mystery / Drama", "genreSlug": "sci-fi",
        "mangaTitle": "Mujirushi: The Sign of Dreams", "mangaTitleJa": "夢印-MUJIRUSHI-",
        "mangaAuthor": "Naoki Urasawa",
        "serialization": "Big Comic Original", "publisher": "Shogakukan",
        "volumes": 1, "status": "Completed",
        "englishVolumes": 1, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["family-issues", "mild-violence"],
        "description": "Urasawa's commissioned love letter to the Louvre — and his most playful one-shot in years.",
        "tags": ["mystery", "drama", "urasawa", "art"],
        "rating": 4,
        "quickTake": [
            "Urasawa's contribution to the Louvre manga series",
            "Playful, compact, full of his usual structural surprises",
            "A treat for fans of his quieter mode"
        ],
        "storyOverview": "Kamoda is a small businessman whose life is collapsing — the pyramid scheme he ran has imploded, his wife has left, and he's stuck with his bizarre daughter. A mysterious man offers him a job: steal a Vermeer from the Louvre. Across one tight volume, Urasawa lets his playful side run wild. Cameos from old characters. Visual gags. A heart that sneaks up on you.",
        "whyILoveIt": "Mujirushi is Urasawa relaxing. The pressure of Monster or 20th Century Boys is gone. He gets to play. Kamoda is one of his most likable losers, and Kasumi is one of his most charming child characters. The Louvre setting gives him an excuse to draw beautiful interiors. It's a perfect minor work.",
        "publishedAt": pdate()
    },
    {
        "slug": "mister-pink",
        "title": "Mister Pink Review: Naoki Urasawa's Almost-Forgotten Early Work",
        "genre": "Drama / Comedy", "genreSlug": "slice-of-life",
        "mangaTitle": "Mister Pink", "mangaTitleJa": "Mr.PINK",
        "mangaAuthor": "Naoki Urasawa",
        "serialization": "Big Comic Original", "publisher": "Shogakukan",
        "volumes": 2, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["mild-violence"],
        "description": "Pre-Monster Urasawa writing a quiet salaryman comedy — a fascinating glimpse into his early style.",
        "tags": ["drama", "comedy", "urasawa", "seinen"],
        "rating": 4,
        "quickTake": [
            "Early Urasawa, before he became Urasawa",
            "Salaryman comedy with subtle craft",
            "Foundational reading for serious Urasawa fans"
        ],
        "storyOverview": "Mr. Pink follows a middle manager at a Japanese company through small humiliations and quiet victories. The plots are bigger than the average salaryman manga — there are mysteries, escapes, and minor adventures — but the emotional register is grounded. You can feel Urasawa figuring out the rhythm of long-form storytelling that would define his later work.",
        "whyILoveIt": "Mister Pink isn't Urasawa's best, but reading it is illuminating. You can see the seeds of everything he'd do later — the warm protagonists, the conspiracy plots, the obsession with ordinary people pushed into extraordinary situations. For fans, it's essential. For new readers, it's a different door into his world.",
        "publishedAt": pdate()
    },
    {
        "slug": "legend-of-mother-sarah",
        "title": "Legend of Mother Sarah Review: Otomo's Post-Apocalyptic Western",
        "genre": "Sci-Fi / Action", "genreSlug": "sci-fi",
        "mangaTitle": "Legend of Mother Sarah", "mangaTitleJa": "母-サラ-の伝説",
        "mangaAuthor": "Katsuhiro Otomo, Takumi Nagayasu",
        "serialization": "Comic Afternoon", "publisher": "Kodansha",
        "volumes": 11, "status": "Completed",
        "englishVolumes": 6, "englishStatus": "Ongoing",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "war", "child-endangerment"],
        "description": "After Earth shatters, a mother walks across the wasteland to find her children — Otomo's other apocalypse epic.",
        "tags": ["sci-fi", "action", "post-apocalyptic", "otomo"],
        "rating": 4,
        "quickTake": [
            "Otomo's other major sci-fi series after Akira",
            "Drawn by Nagayasu, written by Otomo",
            "Quieter, more grounded than Akira's chaos"
        ],
        "storyOverview": "After a catastrophic event, Earth's surface is shattered into fragments. Sarah, separated from her children in the chaos, walks across the wasteland looking for them. She fights cults, slavers, and warlords. Each settlement she crosses gives her a piece of information — and forces a choice about what kind of person she's becoming. Otomo's structural patience is on full display.",
        "whyILoveIt": "Legend of Mother Sarah is what Otomo does when he doesn't have to draw every panel himself. Nagayasu's art is gorgeous in a different way than Akira — softer, more painterly. Sarah is one of the most quietly determined protagonists in any apocalypse manga. The story takes its time. The payoff is worth the wait.",
        "publishedAt": pdate()
    },
    {
        "slug": "akira-club",
        "title": "Akira Club Review: The Otomo Companion You Didn't Know You Needed",
        "genre": "Sci-Fi / Art Book", "genreSlug": "sci-fi",
        "mangaTitle": "Akira Club", "mangaTitleJa": "AKIRA CLUB",
        "mangaAuthor": "Katsuhiro Otomo",
        "serialization": "Standalone", "publisher": "Kodansha",
        "volumes": 1, "status": "Completed",
        "englishVolumes": 1, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["mild-violence"],
        "description": "Otomo's behind-the-scenes companion to Akira — sketches, notes, and unused pages from one of manga's most ambitious works.",
        "tags": ["sci-fi", "art-book", "otomo", "akira"],
        "rating": 4,
        "quickTake": [
            "Companion to Akira from Otomo himself",
            "Sketches, character designs, abandoned scenes",
            "Essential for serious Akira fans"
        ],
        "storyOverview": "Akira Club is Otomo's behind-the-scenes look at his magnum opus. It collects character design sheets, backgrounds, panels that didn't make it into the final book, and Otomo's own notes about why certain decisions were made. It's part art book, part oral history. It's also a rare chance to watch one of manga's great craftsmen explain his own process.",
        "whyILoveIt": "Akira Club is the kind of book that changes how you reread Akira. Seeing the discarded character designs, the early concepts for Tetsuo and Kaneda, the architectural studies for Neo-Tokyo — it makes the final manga feel like the survivor of a much larger imagined world. For fans, it's a treasure.",
        "publishedAt": pdate()
    },
    {
        "slug": "chronos-ruler",
        "title": "Chronos Ruler Review: The Time Demon Hunter Manga You Missed",
        "genre": "Action / Supernatural", "genreSlug": "action",
        "mangaTitle": "Chronos Ruler", "mangaTitleJa": "時間の支配者",
        "mangaAuthor": "Daiki Igarashi",
        "serialization": "Shonen Gangan", "publisher": "Square Enix",
        "volumes": 8, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["supernatural-violence", "horror-elements"],
        "description": "Time-eating demons feed on regret. A pair of immortal hunters fight them across the years.",
        "tags": ["action", "supernatural", "shonen", "time-travel"],
        "rating": 3,
        "quickTake": [
            "Underloved Square Enix shonen series",
            "Time-eating demons make for unique villains",
            "Got an anime that didn't land — manga is better"
        ],
        "storyOverview": "Demons called Horologues feed on people's regret, eating their time and reducing them to children. Victor and Kiri are immortal hunters who travel the world stopping the Horologues. Each case forces the victim to confront what they wish they'd done differently. The hunting itself is just the start; the real work is helping people decide if they want their time back.",
        "whyILoveIt": "Chronos Ruler has a more interesting premise than its anime adaptation suggested. The Horologues' feeding mechanism — eating regret — gives every case emotional weight. Victor and Kiri are likable, the cases are varied, and the eight-volume length means it doesn't outstay its welcome. A solid hidden gem.",
        "publishedAt": pdate()
    },
]

if __name__ == "__main__":
    run_batch(32, "CLAMP/Mizuki/Rumiko/Urasawa shorts", ARTICLES)
