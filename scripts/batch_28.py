#!/usr/bin/env python3
"""Batch 28 — 15 classic action/sci-fi reviews."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from batch_generator import run_batch

ARTICLES = [
    {
        "slug": "mazinger-z",
        "title": "Mazinger Z Review: The Giant Robot That Started It All",
        "genre": "Action / Mecha", "genreSlug": "action",
        "mangaTitle": "Mazinger Z", "mangaTitleJa": "マジンガーZ",
        "mangaAuthor": "Go Nagai",
        "serialization": "Weekly Shonen Jump", "publisher": "Shueisha",
        "volumes": 5, "status": "Completed",
        "englishVolumes": 5, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["violence", "fanservice"],
        "description": "Go Nagai's foundational mecha epic about a teenage pilot and the giant robot that defined a genre.",
        "tags": ["mecha", "classic", "action", "go-nagai", "super-robot"],
        "rating": 4,
        "quickTake": [
            "The work that invented the pilot-inside-the-robot genre",
            "Pulpy, fast-paced, and unapologetically over the top",
            "Essential reading for anyone curious about mecha history"
        ],
        "storyOverview": "Koji Kabuto inherits a giant robot built by his grandfather, designed from a metal called Japanium that only exists in Japan. He becomes the only person who can pilot Mazinger Z against Dr. Hell, a mad scientist commanding an army of mechanical beasts. Every battle escalates, every villain is bigger than the last, and Koji learns that being a hero costs more than he expected.",
        "whyILoveIt": "I read Mazinger Z late, after I already loved Evangelion and Gundam. What surprised me was how *fun* it is. There's no irony, no deconstruction. Just a kid in a giant robot punching evil in the face. I love that the genre's foundational text is this confident, this loud, this full of joy. You can feel why it inspired generations.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "cutey-honey",
        "title": "Cutey Honey Review: Go Nagai's Trailblazing Magical Girl",
        "genre": "Action / Sci-Fi", "genreSlug": "action",
        "mangaTitle": "Cutey Honey", "mangaTitleJa": "キューティーハニー",
        "mangaAuthor": "Go Nagai",
        "serialization": "Weekly Shonen Champion", "publisher": "Akita Shoten",
        "volumes": 2, "status": "Completed",
        "englishVolumes": 2, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["nudity", "violence", "fanservice"],
        "description": "An android schoolgirl who can transform into anything she wants — the manga that helped invent the magical girl battle genre.",
        "tags": ["action", "magical-girl", "classic", "go-nagai"],
        "rating": 4,
        "quickTake": [
            "Pioneer of the transformation-sequence magical girl",
            "Funny, fast, and surprisingly emotional in the right places",
            "A clear ancestor of Sailor Moon and everything after"
        ],
        "storyOverview": "Honey Kisaragi looks like a normal high school student, but she's actually an android built by her father — and the only thing standing between humanity and Panther Claw, a criminal organization hunting for her secret. With a phrase she can transform into different forms: a biker, a singer, a warrior. She fights to honor her father's memory and protect a world that doesn't know what she is.",
        "whyILoveIt": "Cutey Honey is so confident about what it is. Go Nagai isn't trying to be subtle — Honey transforms by tearing her own clothes off, fights with a sword, and cracks jokes mid-battle. But underneath the wildness, there's real grief. She lost her father. She's not sure what she is. That tension makes the action mean something.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "violence-jack",
        "title": "Violence Jack Review: Go Nagai's Bleakest Post-Apocalyptic Epic",
        "genre": "Action / Horror", "genreSlug": "action",
        "mangaTitle": "Violence Jack", "mangaTitleJa": "バイオレンスジャック",
        "mangaAuthor": "Go Nagai",
        "serialization": "Weekly Shonen Magazine", "publisher": "Kodansha",
        "volumes": 18, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "sexual-violence", "gore", "disturbing-themes"],
        "description": "Go Nagai's brutal post-apocalyptic saga following a giant warrior wandering a Japan destroyed by earthquake.",
        "tags": ["action", "post-apocalyptic", "horror", "go-nagai", "classic"],
        "rating": 4,
        "quickTake": [
            "One of the bleakest manga ever published",
            "Wanderer-meets-warlords structure, all drenched in violence",
            "Shares a continuity with Devilman and Mazinger"
        ],
        "storyOverview": "After a massive earthquake destroys Japan, the country fractures into warlord-controlled territories where the strong prey on the weak. From this wreckage emerges Violence Jack, a towering swordsman with no clear past, who walks from settlement to settlement helping survivors and crushing tyrants. As the story unfolds, his identity ties back to characters from Devilman and the broader Nagai universe.",
        "whyILoveIt": "Violence Jack is hard to read. Nagai doesn't flinch from anything — the cruelty, the despair, the small moments of kindness that make it all bearable. But what stuck with me is how each chapter is almost a self-contained morality play. Jack walks in, sees what humans have become, and reminds them they can still choose differently. It's brutal hope.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "genocyber",
        "title": "Genocyber Review: Cyberpunk Horror at Its Most Extreme",
        "genre": "Action / Sci-Fi", "genreSlug": "action",
        "mangaTitle": "Genocyber", "mangaTitleJa": "ジェノサイバー",
        "mangaAuthor": "Tony Takezaki",
        "serialization": "Comic B Tan", "publisher": "Kadokawa Shoten",
        "volumes": 2, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "body-horror", "gore"],
        "description": "Two psychic sisters fused into a weapon of mass destruction in a cyberpunk world that doesn't deserve them.",
        "tags": ["sci-fi", "cyberpunk", "horror", "action"],
        "rating": 3,
        "quickTake": [
            "Cyberpunk filtered through pure horror sensibility",
            "Visually stunning, narratively brutal",
            "Famous for its uncompromising tone"
        ],
        "storyOverview": "In a near-future cyberpunk Tokyo, scientists fuse two telepathic sisters — one mentally damaged, one full of rage — into a single bio-mechanical weapon called Genocyber. When she escapes, she leaves a trail of destruction across continents. The story is less about plot and more about consequence: what happens when humans build a god they can't control.",
        "whyILoveIt": "Genocyber is uncomfortable in a way that feels intentional. It doesn't ask you to root for anyone. The military are monsters. The civilians are pawns. The weapon at the center has no agency. What I love is that it's honest about its nihilism. It's a horror story dressed in cyberpunk clothes, and it earns its darkness.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "riki-oh",
        "title": "Riki-Oh Review: The Bloodiest Prison Manga Ever Made",
        "genre": "Action / Martial Arts", "genreSlug": "action",
        "mangaTitle": "Riki-Oh", "mangaTitleJa": "力王",
        "mangaAuthor": "Tetsuya Saruwatari, Masahiko Takajo",
        "serialization": "Business Jump", "publisher": "Shueisha",
        "volumes": 12, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "gore", "torture", "disturbing-themes"],
        "description": "A superhuman prisoner takes on a corrupt prison system using his fists and an unbreakable will.",
        "tags": ["action", "martial-arts", "prison", "violence"],
        "rating": 4,
        "quickTake": [
            "Famously over-the-top brutal — the inspiration for the cult film",
            "Shockingly emotional under all the chaos",
            "Riki himself is one of manga's purest heroes"
        ],
        "storyOverview": "Riki Oh is sentenced to a privatized prison run by sadistic guards and gang lords. He's also superhumanly strong, trained in deadly martial arts, and absolutely incapable of standing by while others suffer. Each arc pits him against another monster, but the real villain is the system: a society that gave up on its prisoners and let cruelty take over.",
        "whyILoveIt": "Riki-Oh is famous for being violent. Heads explode. Bodies bend wrong. But what surprised me reading it is how *kind* Riki is. He helps strangers. He listens. He cries for people he barely knows. The contrast between his gentleness and the violence around him is what makes the manga work. He's hope wrapped in horror.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "apocalypse-zero",
        "title": "Apocalypse Zero Review: Body Horror Meets Tokusatsu",
        "genre": "Action / Horror", "genreSlug": "action",
        "mangaTitle": "Apocalypse Zero", "mangaTitleJa": "黙示録ゼロ",
        "mangaAuthor": "Takayuki Yamaguchi",
        "serialization": "Weekly Shonen Champion", "publisher": "Akita Shoten",
        "volumes": 12, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "M (Mature)",
        "contentWarnings": ["body-horror", "graphic-violence", "gore", "disturbing-imagery"],
        "description": "After Tokyo collapses, a young man inherits a living suit of armor and fights monsters that should not exist.",
        "tags": ["action", "horror", "body-horror", "post-apocalyptic"],
        "rating": 3,
        "quickTake": [
            "Body horror cranked to absurd levels",
            "Imaginative monster designs that haunt you",
            "Tokusatsu structure with gore-film aesthetics"
        ],
        "storyOverview": "After a great quake destroys Tokyo, mutants and monsters fill the streets. Kakugo Hagakure inherits the Zero armor — a living suit forged from human spirits — and uses it to fight the chaos. His older brother wears the opposite armor and slowly slips into evil. The two brothers' clash drives the story while the monsters get progressively stranger.",
        "whyILoveIt": "What I love about Apocalypse Zero is how committed it is to its weirdness. The monsters aren't just scary — they're absurd, sometimes funny, sometimes sad. Yamaguchi clearly loves drawing impossible bodies, and the manga becomes an exhibition of imagination. The brothers' relationship gives it a heart that the gore alone couldn't carry.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "3x3-eyes",
        "title": "3x3 Eyes Review: An Immortal Boy and the Last of Her Kind",
        "genre": "Action / Fantasy", "genreSlug": "action",
        "mangaTitle": "3x3 Eyes", "mangaTitleJa": "3×3 EYES サザンアイズ",
        "mangaAuthor": "Yuzo Takada",
        "serialization": "Young Magazine", "publisher": "Kodansha",
        "volumes": 40, "status": "Completed",
        "englishVolumes": 8, "englishStatus": "Complete",
        "ageRating": "M (Mature)",
        "contentWarnings": ["violence", "nudity", "horror"],
        "description": "A boy bound to a three-eyed immortal goddess searches the world for a way to make her human.",
        "tags": ["action", "fantasy", "supernatural", "classic", "90s"],
        "rating": 4,
        "quickTake": [
            "One of the great urban-fantasy epics of the '90s",
            "Pai is one of manga's most charming protagonists",
            "Builds slowly into an enormous mythological journey"
        ],
        "storyOverview": "Pai is the last surviving member of the Sanjiyan, a three-eyed immortal race. Yakumo is an ordinary high school student who, after dying in her arms, becomes her bonded servant — also immortal. Together they travel from Tokyo to the Himalayas, hunting for a ritual that can make Pai human. Along the way, they meet ancient demons, rival immortals, and people who want what Pai has.",
        "whyILoveIt": "I love Pai. She's bright, scared, and trying so hard to be brave even though she's basically alone in the world. Yakumo is loyal in a way that costs him constantly. Their relationship is the heart of the series, and Takada lets it grow over decades of in-story time. It's a love story disguised as a fantasy epic.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "ninku",
        "title": "Ninku Review: A Forgotten '90s Battle Manga Worth Rediscovering",
        "genre": "Action / Martial Arts", "genreSlug": "action",
        "mangaTitle": "Ninku", "mangaTitleJa": "忍空",
        "mangaAuthor": "Koji Kiriyama",
        "serialization": "Weekly Shonen Jump", "publisher": "Shueisha",
        "volumes": 9, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["violence"],
        "description": "Goofy-looking ninja warriors fight a corrupt empire in a manga that mixed comedy and martial arts before Naruto did.",
        "tags": ["action", "martial-arts", "ninja", "90s", "shonen"],
        "rating": 4,
        "quickTake": [
            "Pre-Naruto ninja battle manga with a unique tone",
            "Fuusuke's goofy face hides terrifying combat skills",
            "An underrated entry in '90s Shonen Jump history"
        ],
        "storyOverview": "After a war ends, the Ninku — ninja-martial-artists who fought for the rebels — are scattered and hunted by the new government. Fuusuke, the leader of Squad One, looks like a clown and acts like a child, but he's one of the most dangerous fighters alive. He sets out to gather his old comrades and bring down the empire that betrayed them.",
        "whyILoveIt": "Ninku is a strange, lovable manga. Fuusuke's design — round eyes, runny nose, missing teeth — is so disarming that the violence hits harder when it comes. The fighting is creative, the comrades are memorable, and the emotional beats sneak up on you. It deserves more attention than it gets.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "karate-master",
        "title": "Karate Master Review: The Manga That Made Bruce Lee Look Restrained",
        "genre": "Action / Martial Arts", "genreSlug": "action",
        "mangaTitle": "Karate Master", "mangaTitleJa": "空手バカ一代",
        "mangaAuthor": "Ikki Kajiwara, Jiro Tsunoda",
        "serialization": "Weekly Shonen Magazine", "publisher": "Kodansha",
        "volumes": 29, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["violence", "animal-violence"],
        "description": "A semi-fictionalized biography of Mas Oyama, the founder of Kyokushin karate — and one of the most influential martial arts manga ever.",
        "tags": ["martial-arts", "biographical", "classic", "kajiwara"],
        "rating": 5,
        "quickTake": [
            "Biographical manga of real karate legend Mas Oyama",
            "Helped popularize karate worldwide",
            "Foundational text for sports/martial arts manga"
        ],
        "storyOverview": "Mas Oyama trains alone on a mountain to forge an unbreakable spirit. He fights bulls with his bare hands. He travels the world to test himself against every fighter willing to face him. Karate Master takes the real life of Oyama and amplifies every moment until it becomes legend. By the end, you understand why Kyokushin karate exists.",
        "whyILoveIt": "I grew up hearing stories about Oyama from my uncle, who practiced karate. Reading this manga was like meeting the man behind the myths. Yes, it's exaggerated, but the core is true: a man who believed that the body could be trained to do almost anything. It's a love letter to discipline.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "eden-its-an-endless-world",
        "title": "Eden It's an Endless World Review: Cyberpunk Without Compromise",
        "genre": "Sci-Fi / Action", "genreSlug": "sci-fi",
        "mangaTitle": "Eden: It's an Endless World!", "mangaTitleJa": "EDEN It's an Endless World!",
        "mangaAuthor": "Hiroki Endo",
        "serialization": "Afternoon", "publisher": "Kodansha",
        "volumes": 18, "status": "Completed",
        "englishVolumes": 13, "englishStatus": "Ongoing",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "drug-use", "sexual-content", "torture"],
        "description": "A virus collapses civilization, and what comes next is messier and more human than any standard apocalypse story.",
        "tags": ["sci-fi", "cyberpunk", "post-apocalyptic", "seinen"],
        "rating": 5,
        "quickTake": [
            "One of the smartest cyberpunk manga ever made",
            "Time-skips that completely transform the story",
            "Refuses easy answers about technology, religion, or violence"
        ],
        "storyOverview": "A pandemic kills most of the world. The survivors are either resistant, mutated, or running. Eden follows a generational story across decades: a boy on a mountaintop, a smuggler in South America, a hacker fighting corporations, and the slow rebuilding of something that might be worse than what fell. Endo refuses to simplify any of it.",
        "whyILoveIt": "Eden is one of those manga where every time-skip changes what the series is about. The first volumes feel like religious allegory. The middle becomes a noir thriller. The end is a meditation on whether civilization is worth saving. I love that Endo trusts his readers to follow him through every shift. There's nothing else like it.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "biomeat",
        "title": "BioMeat Review: Imagine Junji Ito Wrote a Hunger Manga",
        "genre": "Horror / Sci-Fi", "genreSlug": "horror",
        "mangaTitle": "BioMeat: Nectar", "mangaTitleJa": "BIO-MEAT NECTAR",
        "mangaAuthor": "Yuki Fujisawa",
        "serialization": "Weekly Shonen Champion", "publisher": "Akita Shoten",
        "volumes": 12, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "M (Mature)",
        "contentWarnings": ["body-horror", "graphic-violence", "gore", "disturbing-themes"],
        "description": "Genetically engineered creatures called BM solve Japan's food problem — until they get loose.",
        "tags": ["horror", "sci-fi", "survival", "body-horror"],
        "rating": 4,
        "quickTake": [
            "A survival horror premise pushed to its limit",
            "BM creatures are unforgettable nightmare fuel",
            "Mostly student-perspective, which makes it scarier"
        ],
        "storyOverview": "BioMeat (BM) are bioengineered animals designed to consume garbage and turn it into protein. They solve Japan's food and waste crisis overnight. Then a containment failure releases them. They breed exponentially, eat anything organic, and have no instinct except hunger. The story follows middle schoolers trying to survive in a city that's becoming a food court.",
        "whyILoveIt": "BioMeat is genuinely terrifying in a way that surprised me. The creatures aren't supernatural — they're a logical extrapolation of bioengineering, and that makes them worse. Fujisawa stays close to ordinary people: kids, teachers, parents. The horror works because the perspective never gets more powerful than the threat.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "mai-psychic-girl",
        "title": "Mai the Psychic Girl Review: Cold War Telekinesis",
        "genre": "Sci-Fi / Action", "genreSlug": "sci-fi",
        "mangaTitle": "Mai the Psychic Girl", "mangaTitleJa": "舞 (魔物語愛しのベティ)",
        "mangaAuthor": "Kazuya Kudo, Ryoichi Ikegami",
        "serialization": "Big Comic Spirits", "publisher": "Shogakukan",
        "volumes": 4, "status": "Completed",
        "englishVolumes": 4, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["violence", "implied-sexual-content"],
        "description": "A 14-year-old psychic girl runs from a global conspiracy in one of the first manga to break out in the West.",
        "tags": ["sci-fi", "psychic", "classic", "ikegami"],
        "rating": 4,
        "quickTake": [
            "Among the first manga translated for American audiences",
            "Ikegami's photo-realistic art is stunning",
            "Cold War paranoia in a coming-of-age frame"
        ],
        "storyOverview": "Mai Kuju is fourteen, awkward, and a telekinetic. A secret global organization wants to recruit her — or destroy her if they can't. As she runs from agents around the world, she discovers other psychic children like herself, and slowly understands that her power is part of a much larger inheritance.",
        "whyILoveIt": "Ikegami's art is what hooked me first — the realism gives every scene weight, especially the quiet moments where Mai just looks scared. But what kept me reading is the way the story trusts her vulnerability. She isn't a power fantasy. She's a kid trying to figure out who to trust.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "yuyu-hakusho",
        "title": "YuYu Hakusho Review: The Spirit Detective Who Defined a Generation",
        "genre": "Action / Supernatural", "genreSlug": "action",
        "mangaTitle": "YuYu Hakusho", "mangaTitleJa": "幽☆遊☆白書",
        "mangaAuthor": "Yoshihiro Togashi",
        "serialization": "Weekly Shonen Jump", "publisher": "Shueisha",
        "volumes": 19, "status": "Completed",
        "englishVolumes": 19, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["violence"],
        "description": "A delinquent dies saving a child and becomes a Spirit Detective for the underworld in Togashi's '90s classic.",
        "tags": ["action", "supernatural", "shonen", "classic", "togashi"],
        "rating": 5,
        "quickTake": [
            "The blueprint for tournament-arc shonen done right",
            "Togashi's character writing was already exceptional here",
            "The Dark Tournament is one of shonen's all-time peaks"
        ],
        "storyOverview": "Yusuke Urameshi is a teenage delinquent who dies pushing a child out of traffic. The afterlife wasn't expecting him — he wasn't supposed to be the kind of person who died saving someone. Given a second chance, he becomes a Spirit Detective, investigating cases involving demons, psychic powers, and the boundaries between worlds.",
        "whyILoveIt": "YuYu Hakusho is the manga that taught me what character growth looks like in action stories. Yusuke starts unlikable. He earns every relationship by changing. By the Chapter Black arc, he's a different person — not because the story said so, but because you watched it happen. Togashi was already a master here.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "bobobo-bo-bo-bobo",
        "title": "Bobobo-bo Bo-bobo Review: Manga That Refuses to Make Sense",
        "genre": "Comedy / Action", "genreSlug": "action",
        "mangaTitle": "Bobobo-bo Bo-bobo", "mangaTitleJa": "ボボボーボ・ボーボボ",
        "mangaAuthor": "Yoshio Sawai",
        "serialization": "Weekly Shonen Jump", "publisher": "Shueisha",
        "volumes": 21, "status": "Completed",
        "englishVolumes": 7, "englishStatus": "Ongoing",
        "ageRating": "T (Teen)",
        "contentWarnings": ["surreal-violence", "comedy"],
        "description": "An afro-haired warrior fights with his nose hairs in the most committed nonsense manga ever serialized in Jump.",
        "tags": ["comedy", "action", "absurd", "shonen"],
        "rating": 4,
        "quickTake": [
            "One of the strangest manga Shonen Jump ever ran",
            "Pure absurdist humor — almost no logic, all jokes",
            "Surprisingly emotional when it lets itself be"
        ],
        "storyOverview": "In a future where the Hair Hunters shave everyone bald, Bobobo-bo Bo-bobo fights back with the powers of nose hair. He picks up companions — a girl named Beauty, a fishcake-headed warrior, a noodle ninja — and battles increasingly bizarre enemies. Plot exists, but only as a delivery system for jokes that refuse to make sense.",
        "whyILoveIt": "Bobobo is what happens when a manga commits 100% to its bit. There's no winking at the audience, no acknowledgment that it's weird. It just is. I love manga that respect their reader enough to be incomprehensible. Every page is a dare: keep reading or don't, but we won't slow down.",
        "publishedAt": "2026-04-29"
    },
    {
        "slug": "magic-knight-rayearth-2",
        "title": "Magic Knight Rayearth 2 Review: CLAMP Subverts Their Own Story",
        "genre": "Fantasy / Action", "genreSlug": "fantasy",
        "mangaTitle": "Magic Knight Rayearth 2", "mangaTitleJa": "魔法騎士レイアース2",
        "mangaAuthor": "CLAMP",
        "serialization": "Nakayoshi", "publisher": "Kodansha",
        "volumes": 3, "status": "Completed",
        "englishVolumes": 3, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["violence", "trauma"],
        "description": "The sequel that asks: what if the magical girls came back, and everything was their fault?",
        "tags": ["fantasy", "magical-girl", "clamp", "sequel"],
        "rating": 4,
        "quickTake": [
            "A sequel that recontextualizes the first series",
            "Darker, more thoughtful, more tragic",
            "CLAMP at their most willing to break their own story"
        ],
        "storyOverview": "After the first series ended with the three girls leaving Cephiro, they're pulled back. Cephiro is collapsing because the Pillar system they unknowingly broke has no replacement. Three nations want to claim the role. The girls find themselves in a war they accidentally started, forced to choose between worlds, friendships, and their own definitions of victory.",
        "whyILoveIt": "Rayearth 2 is brave in a way most sequels aren't. CLAMP looked at their own ending and said: this was actually a tragedy. The girls have to live with what they did. The new characters are written with sympathy even when they're enemies. It's one of the most emotionally honest magical girl stories ever told.",
        "publishedAt": "2026-04-29"
    },
]

if __name__ == "__main__":
    run_batch(28, "classic action/sci-fi", ARTICLES)
