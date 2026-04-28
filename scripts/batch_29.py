#!/usr/bin/env python3
"""Batch 29 — 15 shojo/romance/drama reviews."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from batch_generator import run_batch

ARTICLES = [
    {
        "slug": "hana-yori-dango",
        "title": "Hana yori Dango Review: The Shojo That Defined an Era",
        "genre": "Romance / Drama", "genreSlug": "romance",
        "mangaTitle": "Hana yori Dango", "mangaTitleJa": "花より男子",
        "mangaAuthor": "Yoko Kamio",
        "serialization": "Margaret", "publisher": "Shueisha",
        "volumes": 37, "status": "Completed",
        "englishVolumes": 36, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["bullying", "violence", "sexual-content"],
        "description": "A working-class girl crashes into the lives of four impossibly rich boys in the manga that became a cultural touchstone across Asia.",
        "tags": ["romance", "shojo", "school", "classic"],
        "rating": 5,
        "quickTake": [
            "The shojo manga that launched countless drama adaptations",
            "Tsukushi is one of manga's most stubborn heroines",
            "Brutal at times, but earns every emotional payoff"
        ],
        "storyOverview": "Tsukushi Makino is a scholarship student at an elite school dominated by F4 — four heirs to the country's wealthiest families. When she stands up to them, the leader Tsukasa Doumyouji declares war on her. What starts as bullying turns into something neither of them expected. Across thirty-seven volumes, the story refuses to let any character take the easy way out.",
        "whyILoveIt": "Hana yori Dango taught me what shojo manga could do. Tsukushi never folds. She gets bullied, threatened, betrayed — and she keeps showing up. Her relationship with Tsukasa is messy and uncomfortable in ways the story acknowledges. By the end, you've watched both of them grow into people who actually deserve each other.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "yamato-nadeshiko",
        "title": "The Wallflower Review: A Beauty-and-the-Beast Story With Four Beasts",
        "genre": "Romance / Comedy", "genreSlug": "romance",
        "mangaTitle": "The Wallflower", "mangaTitleJa": "ヤマトナデシコ七変化",
        "mangaAuthor": "Tomoko Hayakawa",
        "serialization": "Bessatsu Friend", "publisher": "Kodansha",
        "volumes": 36, "status": "Completed",
        "englishVolumes": 35, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["mild-violence", "bullying"],
        "description": "Four gorgeous boys must transform a horror-loving recluse into a proper lady — or pay rent for life.",
        "tags": ["romance", "comedy", "shojo", "reverse-harem"],
        "rating": 4,
        "quickTake": [
            "Reverse-harem comedy with genuine heart",
            "Sunako is a refreshing protagonist who refuses to change",
            "Ridiculous setup that earns its emotional moments"
        ],
        "storyOverview": "Four impossibly beautiful boys live rent-free in a mansion — on one condition. They must turn the owner's niece, Sunako, into a refined young lady. Sunako is a horror-obsessed recluse who recoils from anything beautiful. The boys try every trick. Sunako mostly ignores them. Slowly, in spite of everyone, real friendship grows.",
        "whyILoveIt": "What I love about The Wallflower is that Sunako never really 'reforms.' She stays weird. She stays uncomfortable around bright lights and pretty faces. The boys learn to love her as she is — and she lets them in, slowly, without giving up who she is. That's a rare romance message in shojo manga of its era.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "bokura-ga-ita",
        "title": "We Were There Review: A Romance That Refuses to Let You Off Easy",
        "genre": "Romance / Drama", "genreSlug": "romance",
        "mangaTitle": "We Were There", "mangaTitleJa": "僕等がいた",
        "mangaAuthor": "Yuki Obata",
        "serialization": "Betsucomi", "publisher": "Shogakukan",
        "volumes": 16, "status": "Completed",
        "englishVolumes": 16, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["death", "depression", "mental-health"],
        "description": "A high school love story that follows its couple deep into adulthood and everything that breaks them along the way.",
        "tags": ["romance", "drama", "shojo", "josei"],
        "rating": 5,
        "quickTake": [
            "One of shojo's most realistic adult romances",
            "Goes places most school romances refuse to",
            "Long-form storytelling that pays off completely"
        ],
        "storyOverview": "Nanami Takahashi enters high school determined to make friends. Yano Motoharu is the most popular boy in class, charming but emotionally guarded. They fall in love. Then his past — the dead ex-girlfriend, the unresolved guilt — slowly pulls them apart. The story follows them through college, separation, jobs, and the work of maybe finding each other again as adults.",
        "whyILoveIt": "I cried a lot reading this. Bokura ga Ita doesn't romanticize first love. It says: yes, it's beautiful, and yes, it might not be enough. Watching Nanami grow up — make mistakes, build a career, become her own person — is one of the truest things shojo manga has done. The ending earns every page.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "backstage-prince",
        "title": "Backstage Prince Review: A Quiet Romance Behind Kabuki Curtains",
        "genre": "Romance / Slice-of-Life", "genreSlug": "romance",
        "mangaTitle": "Backstage Prince", "mangaTitleJa": "歌舞伎堂のオモテとウラ",
        "mangaAuthor": "Kanoko Sakurakouji",
        "serialization": "Cheese!", "publisher": "Shogakukan",
        "volumes": 2, "status": "Completed",
        "englishVolumes": 2, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["mild-romantic-content"],
        "description": "A high school girl meets a young kabuki actor who can only relax around her — and his cat.",
        "tags": ["romance", "shojo", "kabuki", "slice-of-life"],
        "rating": 4,
        "quickTake": [
            "Gentle, low-stakes romance done well",
            "Kabuki setting feels lived-in and authentic",
            "Two volumes that say exactly what they need to"
        ],
        "storyOverview": "Akari is a regular high schooler. Ryusei Horiuchi is a young kabuki actor who can't stand other people — except, somehow, her. Their relationship grows quietly between her schoolwork and his rehearsals. The kabuki theater becomes a third character: a place that demands sacrifice but also gives meaning.",
        "whyILoveIt": "Backstage Prince is short, and it knows exactly what it is. The kabuki details are what hooked me — the costumes, the discipline, the loneliness. Sakurakouji draws Ryusei's exhaustion in a way that feels real, and the romance never asks Akari to fix him. They just choose each other.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "forbidden-dance",
        "title": "Forbidden Dance Review: Ballet, Ambition, and First Love",
        "genre": "Romance / Drama", "genreSlug": "romance",
        "mangaTitle": "Forbidden Dance", "mangaTitleJa": "禁断のダンス",
        "mangaAuthor": "Hinako Ashihara",
        "serialization": "Sho-Comi", "publisher": "Shogakukan",
        "volumes": 5, "status": "Completed",
        "englishVolumes": 4, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["mild-romantic-content"],
        "description": "A ballet hopeful falls for a dancer with secrets — a gentle '90s romance from the author of Sand Chronicles.",
        "tags": ["romance", "shojo", "ballet", "dance"],
        "rating": 4,
        "quickTake": [
            "Hinako Ashihara before Sand Chronicles",
            "Ballet world rendered with care and detail",
            "Compact five-volume romance that doesn't waste a chapter"
        ],
        "storyOverview": "Aya Fujii is determined to become a professional ballerina. When she sees Akira Hibiya dance, she's certain she's met someone special — and certain she'll never reach his level. Their pas de deux on stage becomes one off the stage too, complicated by Akira's unspoken past and the brutal economics of professional dance.",
        "whyILoveIt": "What I love about Forbidden Dance is how seriously Ashihara treats the work of dance. Aya doesn't get there through love — she gets there through practice. The romance grows alongside her career, not instead of it. It's an early sign of the kind of complete, character-driven storytelling that would make Ashihara famous.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "crayon-days",
        "title": "Crayon Days Review: Mio Chizuru's Quiet Drama of Adolescence",
        "genre": "Romance / Drama", "genreSlug": "romance",
        "mangaTitle": "Crayon Days", "mangaTitleJa": "クレヨン王国",
        "mangaAuthor": "Mio Chizuru",
        "serialization": "Hana to Yume", "publisher": "Hakusensha",
        "volumes": 3, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["mild-romance"],
        "description": "A quiet shojo about color, art, and growing up — from a rising voice in josei manga.",
        "tags": ["romance", "art", "slice-of-life", "shojo"],
        "rating": 3,
        "quickTake": [
            "Gentle, art-school setting",
            "Watercolor sensibility throughout",
            "Three-volume length suits the story perfectly"
        ],
        "storyOverview": "A high school student joins her school's art club and discovers that the way she sees color is different from everyone else around her. As she works on paintings, she meets classmates who help her understand what she's looking at — and what she might want to make. The romance is small, the art is everything.",
        "whyILoveIt": "Crayon Days doesn't try to be epic. It's about the moments when you realize how you see the world is your own — and someone else might be willing to learn it. I love manga that respect quiet stories. This one stays with you because of what it doesn't say.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "gentlemens-alliance-cross",
        "title": "The Gentlemen's Alliance Cross Review: Arina Tanemura at Her Wildest",
        "genre": "Romance / Drama", "genreSlug": "romance",
        "mangaTitle": "The Gentlemen's Alliance Cross", "mangaTitleJa": "紳士同盟†",
        "mangaAuthor": "Arina Tanemura",
        "serialization": "Ribon", "publisher": "Shueisha",
        "volumes": 11, "status": "Completed",
        "englishVolumes": 11, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["family-trauma", "implied-sexual-content"],
        "description": "A girl is sold to a powerful family and tangled in school politics, broken siblings, and impossible love triangles.",
        "tags": ["romance", "drama", "shojo", "tanemura"],
        "rating": 4,
        "quickTake": [
            "Tanemura's most ambitious romance",
            "Sparkly art with surprisingly dark family drama",
            "Plot twists that almost dare you to keep up"
        ],
        "storyOverview": "Haine Otomiya is sold to the Otomiya family as repayment for her father's debt. At her elite school, she's surrounded by political maneuvering, secret siblings, and a boy named Shizumasa who may not be who she thinks he is. Tanemura piles on twist after twist, and somehow the emotional core holds.",
        "whyILoveIt": "Gentlemen's Alliance is everything a Tanemura series should be: sparkles, frilly clothes, devastating family secrets. I read it as a teenager and reread it as an adult, and the second time I appreciated how committed she is to her ridiculous plot. It's drama at its most operatic, and it's not embarrassed to be exactly that.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "after-school-nightmare",
        "title": "After School Nightmare Review: A Body Horror Romance Like No Other",
        "genre": "Romance / Horror", "genreSlug": "horror",
        "mangaTitle": "After School Nightmare", "mangaTitleJa": "放課後保健室",
        "mangaAuthor": "Setona Mizushiro",
        "serialization": "Princess GOLD", "publisher": "Akita Shoten",
        "volumes": 10, "status": "Completed",
        "englishVolumes": 10, "englishStatus": "Complete",
        "ageRating": "M (Mature)",
        "contentWarnings": ["body-horror", "gender-dysphoria", "sexual-violence", "psychological-horror"],
        "description": "A student who is half boy and half girl must confront classmates' worst selves in shared dreams every week.",
        "tags": ["horror", "romance", "psychological", "lgbtq"],
        "rating": 5,
        "quickTake": [
            "One of manga's most thoughtful explorations of gender",
            "Dream-sequence horror that means something",
            "Honest about the violence of self-discovery"
        ],
        "storyOverview": "Mashiro Ichijo's body is half male, half female. Every week, in a dream class, students confront their hidden selves — and the only one who can graduate is the one who finds the key to themselves first. As Mashiro is pulled toward two classmates, the dreams reveal more than they're ready to face.",
        "whyILoveIt": "After School Nightmare is one of the most surprising manga I've ever read. It uses horror tropes — body distortion, dream logic, ritual violence — to talk about something most romance manga avoid: how scary it is to be honest about who you are. Mashiro's journey doesn't end where you expect. It earns its pain.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "petshop-of-horrors",
        "title": "Petshop of Horrors Review: Be Careful What You Buy",
        "genre": "Horror / Supernatural", "genreSlug": "horror",
        "mangaTitle": "Petshop of Horrors", "mangaTitleJa": "ペットショップ・オブ・ホラーズ",
        "mangaAuthor": "Matsuri Akino",
        "serialization": "Mystery Bonita", "publisher": "Akita Shoten",
        "volumes": 10, "status": "Completed",
        "englishVolumes": 10, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["body-horror", "implied-violence", "psychological-horror"],
        "description": "Count D sells exotic pets in Chinatown — each one perfect, each one with a contract that the buyer always breaks.",
        "tags": ["horror", "supernatural", "anthology", "classic"],
        "rating": 5,
        "quickTake": [
            "Tales-from-the-crypt structure with a Chinese mythology twist",
            "Count D is one of horror manga's great enigmas",
            "Each chapter a self-contained morality play"
        ],
        "storyOverview": "Count D's pet shop sells animals that look like animals — but might be something else. Each customer buys a creature suited to their deepest desire. Each receives three rules. Almost all break them. Detective Leon Orcot suspects the shop is connected to a series of strange deaths and starts dropping by, both to investigate and because something about D pulls him back.",
        "whyILoveIt": "Petshop of Horrors is everything I love about anthology horror manga. Each story is short, complete, and ends with a moment that recontextualizes everything before it. Count D is genuinely scary, but also melancholy — he sells these creatures because humans deserve them. The relationship with Leon gives the series its spine.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "mink",
        "title": "Mink Review: The Idol Manga Where the Idol Is Software",
        "genre": "Romance / Sci-Fi", "genreSlug": "romance",
        "mangaTitle": "Mink", "mangaTitleJa": "ミンク",
        "mangaAuthor": "Megumi Tachikawa",
        "serialization": "Nakayoshi", "publisher": "Kodansha",
        "volumes": 6, "status": "Completed",
        "englishVolumes": 6, "englishStatus": "Complete",
        "ageRating": "All Ages",
        "contentWarnings": ["mild-romance"],
        "description": "A schoolgirl uses computer software to become a virtual idol — predicting Vocaloid by a decade.",
        "tags": ["romance", "shojo", "magical-girl", "music"],
        "rating": 3,
        "quickTake": [
            "Surprisingly prescient about virtual idols",
            "Magical-girl framework with computer aesthetics",
            "All-ages friendly with real charm"
        ],
        "storyOverview": "Mink is a regular schoolgirl until she gets a piece of software that lets her transform into a pop idol. As 'Mink,' she becomes a sensation. The challenge: balance her two lives, keep the secret, and figure out what she actually wants from fame. The boy she likes is one of her biggest fans — without knowing.",
        "whyILoveIt": "Mink is fun in a way that feels nostalgic now. The 'idol made of software' premise was way ahead of its time, and the all-ages tone makes the romance sweet rather than dramatic. It's a comfort read for anyone who grew up on early-2000s shojo.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "ribbon-no-kishi",
        "title": "Princess Knight Review: The Manga That Invented the Magical Girl",
        "genre": "Fantasy / Action", "genreSlug": "fantasy",
        "mangaTitle": "Princess Knight", "mangaTitleJa": "リボンの騎士",
        "mangaAuthor": "Osamu Tezuka",
        "serialization": "Shojo Club", "publisher": "Kodansha",
        "volumes": 3, "status": "Completed",
        "englishVolumes": 2, "englishStatus": "Complete",
        "ageRating": "All Ages",
        "contentWarnings": ["mild-violence"],
        "description": "Tezuka's foundational work that gave shojo manga its template — a princess raised as a prince, fighting for her kingdom and her heart.",
        "tags": ["fantasy", "shojo", "classic", "tezuka"],
        "rating": 5,
        "quickTake": [
            "The manga that made modern shojo possible",
            "Tezuka writing for girls in a way no one else was",
            "Foundational text for the magical girl genre"
        ],
        "storyOverview": "Princess Sapphire was born with two hearts — one boy, one girl — and is raised as a prince so she can inherit the kingdom. When her gender is exposed, she's hunted. She fights, falls in love, and travels to find a way to live as both halves of herself in a world that wants her to be one thing. Tezuka treats every transformation, every duel, every kiss with the same care.",
        "whyILoveIt": "Reading Princess Knight as an adult, I realized how much later shojo manga owes to it. The dueling identities, the secret love, the ridiculously dramatic fights — Tezuka invented the template that Sailor Moon and Utena would inherit. He took girls' adventures seriously when almost no one else did.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "ghost-sweeper-mikami",
        "title": "Ghost Sweeper Mikami Review: Exorcism for Money",
        "genre": "Action / Comedy", "genreSlug": "action",
        "mangaTitle": "Ghost Sweeper Mikami", "mangaTitleJa": "GS美神 極楽大作戦!!",
        "mangaAuthor": "Takashi Shiina",
        "serialization": "Weekly Shonen Sunday", "publisher": "Shogakukan",
        "volumes": 39, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["fanservice", "supernatural-violence"],
        "description": "A glamorous exorcist runs a ghost-busting business with her hapless apprentice in '90s Sunday's most reliable comedy.",
        "tags": ["action", "comedy", "supernatural", "90s"],
        "rating": 4,
        "quickTake": [
            "One of the great '90s Shonen Sunday comedies",
            "Mikami's mercenary attitude makes every job funny",
            "Strong worldbuilding under the gags"
        ],
        "storyOverview": "Reiko Mikami runs GS Mikami, a ghost-sweeping business that takes any case as long as the price is right. Her assistant Yokoshima is hopeless, perverted, and somehow indispensable. Every chapter introduces a new ghost, demon, or curse, and every chapter Mikami either defeats it or charges extra for the trouble. Underneath the gags, the world becomes increasingly real.",
        "whyILoveIt": "Mikami doesn't pretend to be a hero. She's good at what she does because she charges for it. That cynical streak is what makes the comedy work — when she does occasionally help someone for free, you actually feel it. Shiina's worldbuilding sneaks up on you over thirty-nine volumes.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "patalliro",
        "title": "Patalliro! Review: Manga's Longest Running Comedy Fever Dream",
        "genre": "Comedy / Action", "genreSlug": "action",
        "mangaTitle": "Patalliro!", "mangaTitleJa": "パタリロ!",
        "mangaAuthor": "Mineo Maya",
        "serialization": "Hana to Yume", "publisher": "Hakusensha",
        "volumes": 100, "status": "Ongoing",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["sexual-humor", "violence", "lgbtq-themes"],
        "description": "A child king runs a tiny country with the help of MI6 assassins, BL romance subplots, and absolute chaos.",
        "tags": ["comedy", "action", "lgbtq", "shojo", "long-running"],
        "rating": 5,
        "quickTake": [
            "One of manga's longest-running shojo series",
            "Foundational text for both BL and absurdist comedy",
            "Patalliro is one of manga's most chaotic characters"
        ],
        "storyOverview": "Patalliro Du Malyner VIII is the ten-year-old king of Marinella, a tiny country that produces 80% of the world's diamonds. His bodyguards are MI6 agents, including a tragic British man named Bancoran who attracts every beautiful boy in his orbit. The plots range from spy thrillers to musical numbers to fourth-wall-breaking comedy. Mineo Maya has been doing this for fifty years.",
        "whyILoveIt": "Patalliro is a foundational manga for me, even though I came to it late. It's where so much of modern absurdist humor comes from. Bancoran's romances helped shape what BL would become. And Patalliro himself — chaotic, brilliant, completely amoral — is one of the best characters in any genre.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "sailor-v",
        "title": "Codename Sailor V Review: Sailor Moon's Forgotten Older Sister",
        "genre": "Action / Magical Girl", "genreSlug": "fantasy",
        "mangaTitle": "Codename: Sailor V", "mangaTitleJa": "コードネームはセーラーV",
        "mangaAuthor": "Naoko Takeuchi",
        "serialization": "RunRun", "publisher": "Kodansha",
        "volumes": 3, "status": "Completed",
        "englishVolumes": 2, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["mild-violence"],
        "description": "Before Sailor Moon was a phenomenon, Naoko Takeuchi made Sailor V — the prototype that became part of the legend.",
        "tags": ["magical-girl", "shojo", "classic", "takeuchi"],
        "rating": 4,
        "quickTake": [
            "The series that became the Sailor Moon prologue",
            "Lighter and goofier than the main series",
            "Essential for any Sailor Moon fan"
        ],
        "storyOverview": "Minako Aino is a regular middle schooler until she meets Artemis, a talking white cat who tells her she's actually Sailor V — defender of justice and love. Each chapter introduces a new monster of the day, a new boy crush, and a slowly building mythology that Sailor Moon would inherit. By the end, the reader knows they've been reading prologue.",
        "whyILoveIt": "Sailor V is a delight precisely because it's smaller than what came after. It's funny, low-stakes, and full of the kind of teenage joy that the main Sailor Moon series sometimes had to set aside for war. Reading it feels like meeting Minako before she became one of five — and seeing her shine on her own.",
        "publishedAt": "2026-04-30"
    },
    {
        "slug": "from-far-away",
        "title": "From Far Away Review: A Quiet Isekai From Before Isekai Was a Thing",
        "genre": "Fantasy / Romance", "genreSlug": "fantasy",
        "mangaTitle": "From Far Away", "mangaTitleJa": "ふしぎ遊戯",
        "mangaAuthor": "Kyoko Hikawa",
        "serialization": "LaLa", "publisher": "Hakusensha",
        "volumes": 14, "status": "Completed",
        "englishVolumes": 14, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["violence", "war"],
        "description": "A modern Tokyo girl is pulled into a fantasy world where she's prophesied to be the Awakening — a force of unimaginable destruction.",
        "tags": ["fantasy", "isekai", "romance", "shojo"],
        "rating": 4,
        "quickTake": [
            "Isekai shojo from the '90s, before the trend",
            "Language barrier is treated seriously and beautifully",
            "Slow-burn romance built on real trust"
        ],
        "storyOverview": "Noriko Tachiki is on her way home from school when an explosion sends her to another world. Izark, a wandering mercenary, finds her. Neither speaks the other's language. As they travel together, she slowly learns his words and his world — but she's also being hunted as the Awakening, a prophesied figure whose power will change everything.",
        "whyILoveIt": "From Far Away is one of the most quietly beautiful shojo manga I've read. The language barrier between Noriko and Izark is handled with such patience — every word she learns matters. By the time she can have a real conversation with him, you've watched both of them earn it. The romance never rushes.",
        "publishedAt": "2026-04-30"
    },
]

if __name__ == "__main__":
    run_batch(29, "shojo/romance/drama", ARTICLES)
