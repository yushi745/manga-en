#!/usr/bin/env python3
"""Batch 33 — 15 reviews: horror, seinen, Nagai catalog deep cuts."""
import sys, os, random
from datetime import date, timedelta
sys.path.insert(0, os.path.dirname(__file__))
from batch_generator import run_batch

random.seed(20260429 + 33)
START = date(2024, 7, 18)
END = date(2026, 4, 28)
DAYS = (END - START).days
def pdate():
    return (START + timedelta(days=random.randint(0, DAYS))).isoformat()

ARTICLES = [
    {
        "slug": "yamishibai-manga",
        "title": "Yamishibai Review: The Anime Got Big — The Manga Is Quietly Better",
        "genre": "Horror / Anthology", "genreSlug": "horror",
        "mangaTitle": "Yamishibai", "mangaTitleJa": "闇芝居",
        "mangaAuthor": "Various",
        "serialization": "Web serialization", "publisher": "Takeshobo",
        "volumes": 5, "status": "Ongoing",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["psychological-horror", "supernatural", "disturbing-imagery"],
        "description": "The kamishibai-style horror anime adapted into manga — paper theater terrors in a more permanent form.",
        "tags": ["horror", "anthology", "supernatural", "psychological"],
        "rating": 3,
        "quickTake": [
            "Manga adaptation of the cult horror anime",
            "Each chapter a self-contained urban legend",
            "Quieter than the anime, in some ways scarier"
        ],
        "storyOverview": "Yamishibai began as a horror anime drawn in the kamishibai (paper theater) style. The manga adaptations work through similar territory — modern Japanese urban legends, ghosts in apartment hallways, things that follow you home. Each chapter is short, punchy, and built around a single image you'll wish you hadn't seen.",
        "whyILoveIt": "Yamishibai's manga form lets you sit with the images in a way the anime doesn't. The pacing is yours. You can linger on the panel where the figure first appears, decide when to turn the page, decide whether you want to. That control makes the horror more intimate — and somehow worse.",
        "publishedAt": pdate()
    },
    {
        "slug": "ushiro-no-hyakutarou",
        "title": "Ushiro no Hyakutarou Review: The Boy Who Carries 100 Spirits",
        "genre": "Horror / Supernatural", "genreSlug": "horror",
        "mangaTitle": "Ushiro no Hyakutarou", "mangaTitleJa": "うしろの百太郎",
        "mangaAuthor": "Tsunoda Jiro",
        "serialization": "Weekly Shonen Magazine", "publisher": "Kodansha",
        "volumes": 8, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["supernatural-horror", "death", "exorcism-themes"],
        "description": "A boy whose protective spirit is named Hyakutaro fights ghosts and curses across postwar Japan — the foundational paranormal horror manga.",
        "tags": ["horror", "supernatural", "classic", "tsunoda-jiro"],
        "rating": 5,
        "quickTake": [
            "Foundational psychic horror manga from the 70s",
            "Tsunoda Jiro practically invented the genre",
            "Haunting in ways modern horror manga can't replicate"
        ],
        "storyOverview": "Ichiro is a boy with a guardian spirit named Hyakutaro who stands behind him at all times. Together they investigate hauntings, curses, and the mysteries of the spirit world across postwar Japan. Tsunoda was one of the godfathers of paranormal horror manga, and Hyakutaro was his most enduring creation. Each chapter blends folklore with genuine ghost-story dread.",
        "whyILoveIt": "Ushiro no Hyakutarou is the kind of manga that gave a generation of Japanese kids nightmares. Tsunoda's art has a distinct rough edge that reads as real. His ghosts aren't designed for shock; they're designed for the back of your mind. Reading it now, you can see the seeds of every horror manga that came after.",
        "publishedAt": pdate()
    },
    {
        "slug": "shibito-no-koe",
        "title": "Shibito no Koe wo Kiku ga Yoi Review: Detective Stories with Ghosts",
        "genre": "Horror / Mystery", "genreSlug": "horror",
        "mangaTitle": "Shibito no Koe wo Kiku ga Yoi", "mangaTitleJa": "死人の声をきくがよい",
        "mangaAuthor": "Hiyodori Uneji",
        "serialization": "Champion Tap!", "publisher": "Akita Shoten",
        "volumes": 17, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "psychological-horror", "death", "gore"],
        "description": "A regular high schooler can see the dead — and they want him to solve their murders. Sometimes brutally.",
        "tags": ["horror", "mystery", "supernatural", "seinen"],
        "rating": 4,
        "quickTake": [
            "Horror-mystery with a dark sense of humor",
            "Each case puts the protagonist in real physical danger",
            "Builds an unexpectedly emotional long arc"
        ],
        "storyOverview": "Hayama is a regular high school boy who can see ghosts. At first the dead just want to be acknowledged. Then they start asking him to solve their murders. As the cases pile up, Hayama's life gets more dangerous — the killers don't appreciate the investigation, and the ghosts aren't always kind. Across seventeen volumes, the manga builds a surprisingly tight long arc.",
        "whyILoveIt": "Shibito no Koe is a horror-mystery hybrid that does both well. The cases are genuinely creepy. The protagonist's relationship with his ghost girlfriend grows in unexpected directions. And the manga isn't afraid to put real consequences on its lead — he gets hurt, and the injuries matter. It deserves more attention.",
        "publishedAt": pdate()
    },
    {
        "slug": "souboutei",
        "title": "Souboutei Kowasu Beshi Review: Kazuhiro Fujita Goes Full Nightmare",
        "genre": "Horror / Action", "genreSlug": "horror",
        "mangaTitle": "Souboutei Kowasu Beshi", "mangaTitleJa": "双亡亭壊すべし",
        "mangaAuthor": "Kazuhiro Fujita",
        "serialization": "Weekly Shonen Sunday", "publisher": "Shogakukan",
        "volumes": 25, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "M (Mature)",
        "contentWarnings": ["body-horror", "graphic-violence", "psychological-horror", "death"],
        "description": "Ushio and Tora's creator returns with his bleakest, most ambitious horror — a haunted mansion that swallows everyone who enters.",
        "tags": ["horror", "action", "supernatural", "fujita"],
        "rating": 5,
        "quickTake": [
            "Kazuhiro Fujita's most ambitious work",
            "A haunted mansion as cosmic horror",
            "Builds slowly and pays off massively"
        ],
        "storyOverview": "Souboutei is a mansion that has stood for over a hundred years, eating anyone who enters. The government has tried everything. Now they assemble a team — psychic children, reformed criminals, occult experts — to enter the mansion together and destroy whatever is inside. The deeper they go, the stranger and worse it gets. Fujita uses every trick he developed over decades to make the dread land.",
        "whyILoveIt": "Souboutei is Fujita at the height of his powers. The mansion is one of the great horror settings in any manga — claustrophobic, fractal, alive. The team dynamics are vintage Fujita: damaged people becoming a family. The cosmic horror angle is earned. By the end, you've read one of the great horror manga of the 2010s.",
        "publishedAt": pdate()
    },
    {
        "slug": "shimauma",
        "title": "Shimauma Review: Vengeance, Slow and Brutal",
        "genre": "Horror / Crime", "genreSlug": "horror",
        "mangaTitle": "Shimauma", "mangaTitleJa": "シマウマ",
        "mangaAuthor": "Junji Kojima",
        "serialization": "Young King", "publisher": "Shonen Gahosha",
        "volumes": 21, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "torture", "sexual-violence", "drug-use"],
        "description": "A man wakes up wearing a zebra mask, told he's now a hitman until his target finds him. A live-action film made it briefly famous.",
        "tags": ["horror", "crime", "thriller", "seinen"],
        "rating": 4,
        "quickTake": [
            "Brutal underworld revenge thriller",
            "Got a notorious live-action film adaptation",
            "Not for the squeamish — earns its violence"
        ],
        "storyOverview": "Tatsuo wakes up in a hotel room wearing a zebra mask. A voice on the phone tells him he's now a 'shimauma' — a Zebra. He has 24 hours to find the woman who hired the agency, who knows his identity, and the world will collapse on him before then. As he hunts, he uncovers a vast underworld of shimauma — disposable assassins forced to work or die.",
        "whyILoveIt": "Shimauma is hard to read but hard to put down. Kojima's art has a specific kind of ugly realism that makes the violence feel weighty. Tatsuo's situation is a perfect noir engine — he can never trust anyone, and every mistake costs. The world feels lived-in, and the eventual revelations earn the journey.",
        "publishedAt": pdate()
    },
    {
        "slug": "old-boy",
        "title": "Old Boy Review: The Manga That Inspired the Iconic Korean Film",
        "genre": "Crime / Mystery", "genreSlug": "horror",
        "mangaTitle": "Old Boy", "mangaTitleJa": "ルーズ戦記オールドボーイ",
        "mangaAuthor": "Garon Tsuchiya, Nobuaki Minegishi",
        "serialization": "Weekly Manga Action", "publisher": "Futabasha",
        "volumes": 8, "status": "Completed",
        "englishVolumes": 8, "englishStatus": "Complete",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "psychological-trauma", "abuse"],
        "description": "A man is locked in a private prison for ten years. When he's released, he wants to know why — and Park Chan-wook turned this manga into one of cinema's great revenge films.",
        "tags": ["crime", "mystery", "thriller", "seinen"],
        "rating": 5,
        "quickTake": [
            "Source material for Park Chan-wook's film",
            "Slower and quieter than the movie — and rewarding",
            "One of the great revenge manga"
        ],
        "storyOverview": "Shinichi Goto wakes up imprisoned in a private cell with no idea why. For ten years, he sees only a small TV and a slot in the wall where food appears. Then, without warning, he's released into a world that has moved on without him. He sets out to find his captor — and the truth turns out to be far stranger than vengeance.",
        "whyILoveIt": "Old Boy as manga is different from the film. Quieter. More patient. Tsuchiya gives Goto time to feel the disorientation of release, the small joys of a cigarette or sunlight, before the hunt begins. Minegishi's art is restrained, almost documentary. The mystery's resolution is structurally similar to the film but emotionally different. Both are essential.",
        "publishedAt": pdate()
    },
    {
        "slug": "lone-wolf-2100",
        "title": "Lone Wolf 2100 Review: Cyberpunk Reboot of the Samurai Classic",
        "genre": "Sci-Fi / Action", "genreSlug": "sci-fi",
        "mangaTitle": "Lone Wolf 2100", "mangaTitleJa": "Lone Wolf 2100",
        "mangaAuthor": "Mike Kennedy, Francisco Ruiz Velasco",
        "serialization": "Various", "publisher": "Dark Horse",
        "volumes": 3, "status": "Completed",
        "englishVolumes": 3, "englishStatus": "Complete",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "child-endangerment"],
        "description": "Dark Horse's American reimagining of Lone Wolf and Cub — a cyborg ronin and a child, in 2100.",
        "tags": ["sci-fi", "action", "cyberpunk", "western-comic"],
        "rating": 3,
        "quickTake": [
            "American reboot of Lone Wolf and Cub in cyberpunk",
            "Beautifully painted but uneven",
            "Curiosity for fans of the original"
        ],
        "storyOverview": "In 2100, the world is run by megacorps and the few humans left make do however they can. A cyborg called Itto Ogami escapes his corporate masters with a young girl named Daisy who carries the secret to a virus killing humanity. Together they walk the wasteland with one weapon and one purpose. Velasco's painted art elevates the material throughout.",
        "whyILoveIt": "Lone Wolf 2100 isn't as good as the original, but it's a fascinating experiment. Velasco's painted art makes every page feel like a movie still. The cyberpunk setting forces the basic samurai story to mutate in interesting ways. As a tribute and a transformation, it's worth reading once.",
        "publishedAt": pdate()
    },
    {
        "slug": "devilman-lady",
        "title": "Devilman Lady Review: Go Nagai Goes Even Bleaker",
        "genre": "Horror / Action", "genreSlug": "horror",
        "mangaTitle": "Devilman Lady", "mangaTitleJa": "デビルマンレディー",
        "mangaAuthor": "Go Nagai",
        "serialization": "Morning", "publisher": "Kodansha",
        "volumes": 17, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "sexual-violence", "body-horror", "gore"],
        "description": "Devilman's apocalypse, retold from a woman's perspective — Go Nagai going even darker than the original.",
        "tags": ["horror", "action", "go-nagai", "supernatural"],
        "rating": 5,
        "quickTake": [
            "Devilman's spiritual sequel from a different angle",
            "Even bleaker than the original — almost unbearably so",
            "Some of Nagai's most committed late-period work"
        ],
        "storyOverview": "Jun Fudo is a model who discovers she can transform into a demon. The government tries to control her; the demons want to recruit her. As demons start awakening across the world, Jun is forced to choose what side she's on — and learns that there isn't a side that survives. The story moves in parallel to the original Devilman but reaches an even darker place.",
        "whyILoveIt": "Devilman Lady is Nagai revisiting his bleakest material with the perspective of someone who survived to write more. Jun is a different protagonist than Akira — she's already an adult, already complicit, already broken in different ways. The body horror hits harder because of the female-bodied focus. The ending is one of the most devastating in any manga.",
        "publishedAt": pdate()
    },
    {
        "slug": "mao-dante",
        "title": "Mao Dante Review: The Manga Where Devilman Was Born",
        "genre": "Horror / Action", "genreSlug": "horror",
        "mangaTitle": "Mao Dante", "mangaTitleJa": "魔王ダンテ",
        "mangaAuthor": "Go Nagai",
        "serialization": "Boku Magazine", "publisher": "Asahi Sonorama",
        "volumes": 4, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "religious-themes", "body-horror"],
        "description": "The unfinished demon king manga that became Devilman — Go Nagai's first attempt at his lifetime obsession.",
        "tags": ["horror", "action", "go-nagai", "classic"],
        "rating": 4,
        "quickTake": [
            "Unfinished prototype for Devilman",
            "Already shows the apocalyptic ambition",
            "Essential context for Nagai fans"
        ],
        "storyOverview": "Ryo Utsugi is a teenager who becomes possessed by Dante, the demon king. As Dante, he discovers that the truth of religious history is the opposite of what humans believe — angels are the cruel ones, demons fled from oppression. The manga was cancelled before completion, but Nagai would mine these ideas for years afterward, eventually producing Devilman.",
        "whyILoveIt": "Mao Dante is fascinating because you can see Devilman trying to be born inside it. The themes — possession, religious inversion, war between humans and the supernatural — are all here, just not yet refined. The unfinished status makes it feel raw. Reading it after Devilman, you understand how long Nagai had been chasing this story.",
        "publishedAt": pdate()
    },
    {
        "slug": "shutendoji",
        "title": "Shutendoji Review: Go Nagai's Demon King Folktale",
        "genre": "Horror / Fantasy", "genreSlug": "horror",
        "mangaTitle": "Shutendoji", "mangaTitleJa": "手天童子",
        "mangaAuthor": "Go Nagai",
        "serialization": "Weekly Shonen Magazine", "publisher": "Kodansha",
        "volumes": 4, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "supernatural-horror"],
        "description": "Go Nagai retells the legend of Shuten-doji, the legendary demon king of Mount Oe — with all of his usual ferocity.",
        "tags": ["horror", "fantasy", "go-nagai", "folklore"],
        "rating": 4,
        "quickTake": [
            "Nagai adapts a classic Japanese demon legend",
            "His most folklore-inflected horror",
            "Brutal but mythic"
        ],
        "storyOverview": "Shuten-doji is born to a human family but is actually the reincarnation of an ancient oni king. As his powers awaken, he's pulled toward Mount Oe — the mountain where his demon ancestors ruled. The story balances the original folklore with Nagai's interest in the violence between humans and supernatural beings, neither side easy to root for.",
        "whyILoveIt": "Shutendoji is Nagai mining Japanese mythology directly, and it works. The folkloric setting gives him a different palette than his contemporary horror. The brutality fits — these are myths about monsters, after all. As a less-known Nagai work, it's worth seeking out for fans of the genre.",
        "publishedAt": pdate()
    },
    {
        "slug": "susanoo-manga",
        "title": "Susanoo Review: Go Nagai's Storm-God Apocalypse",
        "genre": "Action / Mythology", "genreSlug": "action",
        "mangaTitle": "Susanoo", "mangaTitleJa": "スサノオ",
        "mangaAuthor": "Go Nagai",
        "serialization": "Various", "publisher": "Various",
        "volumes": 5, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "religious-themes", "death"],
        "description": "Nagai retells the myth of Susanoo, the storm god, in his usual maximalist horror-action mode.",
        "tags": ["action", "mythology", "go-nagai", "japanese-mythology"],
        "rating": 4,
        "quickTake": [
            "Nagai's take on Shinto mythology",
            "The storm god as cosmic-scale antihero",
            "Less famous than his other Nagai mythology works"
        ],
        "storyOverview": "Susanoo is the storm god of Japanese mythology — chaotic, violent, repeatedly punished by his fellow gods. Nagai retells his story with the same energy he brought to demons and devils. From his banishment from heaven to his fight with the eight-headed serpent Yamata-no-Orochi, the manga renders Shinto myths in action-horror language.",
        "whyILoveIt": "Susanoo is Nagai applied to a different mythology, and the results are characteristically intense. The storm god's contradictions — destroyer and protector, exiled and worshipped — fit Nagai's interest in morally complex figures. The action sequences are some of his most kinetic. For fans of his mythology phase, it's essential.",
        "publishedAt": pdate()
    },
    {
        "slug": "heat-buronson",
        "title": "Heat Review: Buronson and Ikegami's Crime Epic",
        "genre": "Crime / Drama", "genreSlug": "horror",
        "mangaTitle": "Heat", "mangaTitleJa": "HEAT-灼熱-",
        "mangaAuthor": "Buronson, Ryoichi Ikegami",
        "serialization": "Big Comic Superior", "publisher": "Shogakukan",
        "volumes": 17, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "M (Mature)",
        "contentWarnings": ["graphic-violence", "sexual-content", "death", "crime"],
        "description": "From the writer of Fist of the North Star and the artist of Crying Freeman — a club hostess and a fixer take on Tokyo's underworld.",
        "tags": ["crime", "drama", "ikegami", "buronson", "seinen"],
        "rating": 4,
        "quickTake": [
            "Buronson and Ikegami pairing is always worth attention",
            "Tokyo nightlife rendered in painted realism",
            "More restrained than their other collaborations"
        ],
        "storyOverview": "Karasawa is a fixer in Kabukicho with connections everywhere. When a cabaret hostess named Karen comes to him for protection, he gets pulled into a war between yakuza, politicians, and old debts. Ikegami's painted-realistic art makes every face count. Buronson's plotting moves the chess pieces of Tokyo's underworld with patience.",
        "whyILoveIt": "Heat is what Buronson and Ikegami do when they're not in pure pulp mode. There's still violence, there's still sex, but the structure is more carefully built. Karasawa is a more morally compromised protagonist than their previous collaborations, which gives every move he makes weight. It deserves to be better known in English.",
        "publishedAt": pdate()
    },
    {
        "slug": "cool-doji-danshi",
        "title": "Cool Doji Danshi Review: Cool Boys Who Are Hopelessly Clumsy",
        "genre": "Comedy / Slice-of-Life", "genreSlug": "slice-of-life",
        "mangaTitle": "Play It Cool, Guys", "mangaTitleJa": "クールドジ男子",
        "mangaAuthor": "Kokone Nata",
        "serialization": "Comic Pixiv", "publisher": "Square Enix",
        "volumes": 8, "status": "Ongoing",
        "englishVolumes": 6, "englishStatus": "Ongoing",
        "ageRating": "T (Teen)",
        "contentWarnings": ["mild-comedy"],
        "description": "Four impossibly cool-looking boys are also impossibly clumsy — and refuse to let it show in this gentle comedy hit.",
        "tags": ["comedy", "slice-of-life", "shojo"],
        "rating": 4,
        "quickTake": [
            "Pure comfort comedy",
            "Cool boys whose clumsiness is hidden by composure",
            "A surprise hit that earned its anime"
        ],
        "storyOverview": "Hayate, Mima, Futaba, and Shiki all look like impossibly cool young men. They're also clumsy disasters who fall, drop things, and embarrass themselves constantly — while maintaining their cool exteriors. Each chapter is a self-contained comedy about the gap between how they look and how they actually are.",
        "whyILoveIt": "Cool Doji Danshi is one of the most pleasant manga I've read in years. The premise is silly but the execution is precise. Each character has their specific kind of clumsiness, and watching them recover with poker faces is endlessly funny. It's the manga equivalent of comfort food.",
        "publishedAt": pdate()
    },
    {
        "slug": "legendz",
        "title": "Legendz Review: The Pokemon Knockoff That's Better Than It Should Be",
        "genre": "Action / Fantasy", "genreSlug": "fantasy",
        "mangaTitle": "Legendz", "mangaTitleJa": "LEGENDZ",
        "mangaAuthor": "Makoto Haruno, Rin Hirai",
        "serialization": "Comic BomBom", "publisher": "Kodansha",
        "volumes": 4, "status": "Completed",
        "englishVolumes": 4, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["mild-violence"],
        "description": "Mythological creatures in capsules, schoolboys with destinies, and a surprising amount of heart.",
        "tags": ["action", "fantasy", "shonen", "monster-collecting"],
        "rating": 3,
        "quickTake": [
            "Pokemon-adjacent monster-collecting manga",
            "Better written than the genre usually deserves",
            "Tied to a card game and toy line"
        ],
        "storyOverview": "Ken is a regular schoolboy who finds a soul figure — a capsule containing the spirit of a mythological creature called Shiron, a baby dragon. As more soul figures are released into the world, Ken is pulled into a tournament structure with bigger stakes than the marketing suggests. The mythological creatures are drawn from world cultures, not just Western D&D fare.",
        "whyILoveIt": "Legendz is more interesting than its monster-of-the-week premise suggests. The mythology is broad — pulling from Japanese, Norse, and South American traditions. The character writing is better than the format requires. As a brief, finished entry in the genre, it's worth a look for nostalgic readers.",
        "publishedAt": pdate()
    },
    {
        "slug": "umizaru",
        "title": "Umizaru Review: Coast Guard Drama Done Right",
        "genre": "Drama / Action", "genreSlug": "slice-of-life",
        "mangaTitle": "Umizaru", "mangaTitleJa": "海猿",
        "mangaAuthor": "Shuho Sato",
        "serialization": "Big Comic Spirits", "publisher": "Shogakukan",
        "volumes": 12, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["death", "physical-danger", "trauma"],
        "description": "A young man trains to become a Japan Coast Guard rescue diver in Sato's painstakingly researched workplace drama.",
        "tags": ["drama", "action", "seinen", "rescue"],
        "rating": 4,
        "quickTake": [
            "Coast Guard rescue diver workplace drama",
            "Inspired a successful film series",
            "Sato's research is what makes it land"
        ],
        "storyOverview": "Daisuke Senzaki enters the Japan Coast Guard's rescue diver training program. The training is brutal. The actual job is worse — going into freezing water to pull people from sinking ships, finding bodies in container holds, accepting losses. The manga follows Senzaki across years as he becomes the kind of person who can do this work, and stays human while doing it.",
        "whyILoveIt": "Umizaru is one of the great workplace manga. Sato did the research — every drill, every piece of gear, every emotional cost is real. Senzaki isn't a chosen one; he's a stubborn person who learns to be useful. By the time he leads his first rescue, you've earned the moment with him. It's quietly heroic.",
        "publishedAt": pdate()
    },
]

if __name__ == "__main__":
    run_batch(33, "horror/seinen + Nagai catalog", ARTICLES)
