#!/usr/bin/env python3
"""Batch 31 — 15 reviews: classic shojo + Tezuka deep cuts."""
import sys, os, random
from datetime import date, timedelta
sys.path.insert(0, os.path.dirname(__file__))
from batch_generator import run_batch

# Past-date randomization (rule: no future dates)
random.seed(20260429 + 31)
START = date(2024, 7, 18)
END = date(2026, 4, 28)
DAYS = (END - START).days
def pdate():
    return (START + timedelta(days=random.randint(0, DAYS))).isoformat()

ARTICLES = [
    {
        "slug": "swan-manga",
        "title": "Swan Review: The Ballet Manga That Set the Standard",
        "genre": "Drama / Sports", "genreSlug": "sports",
        "mangaTitle": "Swan", "mangaTitleJa": "SWAN -白鳥-",
        "mangaAuthor": "Kyoko Ariyoshi",
        "serialization": "Margaret", "publisher": "Shueisha",
        "volumes": 21, "status": "Completed",
        "englishVolumes": 15, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["mild-romance", "physical-injury"],
        "description": "A girl from Hokkaido fights to become a world-class ballerina in the manga that defined ballet shojo.",
        "tags": ["sports", "ballet", "shojo", "classic", "drama"],
        "rating": 5,
        "quickTake": [
            "The ballet manga every other ballet manga owes",
            "Masumi Hijiri is a genuine sports-shojo icon",
            "The dance sequences are still unmatched"
        ],
        "storyOverview": "Masumi Hijiri grows up in rural Hokkaido dancing alone in her room. When a touring Russian ballet company comes through, she's spotted by a master who tells her she has the bones to be great. She moves to Tokyo, joins a famous school, and competes against girls who have trained their entire lives. The manga follows her from awkward beginner to international stage.",
        "whyILoveIt": "Swan is one of the most rigorous sports manga ever made. Ariyoshi clearly knows ballet — every pose, every correction, every injury feels real. Masumi isn't gifted in any easy way; she works for everything. Watching her grow up, fall in love, and almost destroy her body for her art is one of shojo manga's great long arcs.",
        "publishedAt": pdate()
    },
    {
        "slug": "oniisama-e",
        "title": "Brother Dear Brother Review: Riyoko Ikeda's All-Girls School Tragedy",
        "genre": "Drama / Romance", "genreSlug": "romance",
        "mangaTitle": "Brother, Dear Brother", "mangaTitleJa": "おにいさまへ…",
        "mangaAuthor": "Riyoko Ikeda",
        "serialization": "Margaret", "publisher": "Shueisha",
        "volumes": 3, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["suicide", "drug-use", "mental-illness", "lgbtq-themes"],
        "description": "A new student at an elite girls' academy gets pulled into a sorority's poison politics in Riyoko Ikeda's haunting epic.",
        "tags": ["romance", "drama", "shojo", "lgbtq", "classic"],
        "rating": 5,
        "quickTake": [
            "Riyoko Ikeda's masterpiece of all-girls school drama",
            "Letters home to a 'dear brother' who is mostly silent",
            "Foundational influence on Class S and yuri storytelling"
        ],
        "storyOverview": "Nanako Misonoo enters Seiran Academy, an elite all-girls school dominated by the sorority and three impossibly cool upperclassmen — Saint Just, Rei Asaka, and Henmi. Through letters to a 'big brother' figure she barely knows, Nanako describes her year: the cruelty of the sorority, the love affairs that destroy people, the suicides that follow. Ikeda treats every character's pain with the seriousness of an opera.",
        "whyILoveIt": "Oniisama e is one of the saddest manga I've ever read. Ikeda doesn't soften any of the cruelty — the sorority politics are brutal, the upperclassmen are wounded, and the romances are doomed. But she also doesn't condescend to her characters. They're treated like real people whose pain matters. Reading it, I understood why it's a foundational text.",
        "publishedAt": pdate()
    },
    {
        "slug": "candy-candy",
        "title": "Candy Candy Review: The Shojo Phenomenon Locked Behind Lawsuits",
        "genre": "Romance / Drama", "genreSlug": "romance",
        "mangaTitle": "Candy Candy", "mangaTitleJa": "キャンディ・キャンディ",
        "mangaAuthor": "Kyoko Mizuki, Yumiko Igarashi",
        "serialization": "Nakayoshi", "publisher": "Kodansha",
        "volumes": 9, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "All Ages",
        "contentWarnings": ["death", "war"],
        "description": "An orphan girl growing up between Britain and America in one of shojo manga's most beloved — and most legally complicated — works.",
        "tags": ["romance", "shojo", "classic", "orphan"],
        "rating": 5,
        "quickTake": [
            "One of the most influential shojo manga ever made",
            "Effectively unavailable in print due to author lawsuit",
            "An entire generation grew up on this story"
        ],
        "storyOverview": "Candy White is an orphan raised at Pony's Home in early 20th century America. After being adopted, abandoned, and sent to school in England, she meets the boys who shape her life — Anthony, Terry, Albert. The story spans years and continents, through the First World War and beyond, as Candy survives every loss and refuses to stop loving.",
        "whyILoveIt": "Candy Candy is a manga that influenced generations even though most modern readers can never legally buy it. The legal battle between writer and artist froze it out of print. But its DNA is in every orphan-heroine shojo since. Candy's resilience — she cries, but she keeps going — is the template for so much that came after.",
        "publishedAt": pdate()
    },
    {
        "slug": "from-eroica-with-love",
        "title": "From Eroica with Love Review: Cold War Spies Meet Shojo Comedy",
        "genre": "Comedy / Action", "genreSlug": "action",
        "mangaTitle": "From Eroica with Love", "mangaTitleJa": "エロイカより愛をこめて",
        "mangaAuthor": "Yasuko Aoike",
        "serialization": "Princess", "publisher": "Akita Shoten",
        "volumes": 41, "status": "Ongoing",
        "englishVolumes": 15, "englishStatus": "Ongoing",
        "ageRating": "T (Teen)",
        "contentWarnings": ["mild-violence", "lgbtq-content"],
        "description": "A flamboyant art thief and a stoic NATO spy chase each other across Cold War Europe in one of shojo's longest-running adventures.",
        "tags": ["action", "comedy", "shojo", "spy", "classic"],
        "rating": 5,
        "quickTake": [
            "Shojo Cold War spy comedy — yes, that's a real genre",
            "Eroica is one of manga's great chaotic queer characters",
            "Major Klaus is shojo's most reluctant straight man"
        ],
        "storyOverview": "Eroica is a wealthy English art thief with telekinetic apprentices. Major Klaus is a German NATO spy who wants nothing to do with him. They keep crossing paths across the Cold War — in Berlin, in Moscow, in tiny Soviet republics — and slowly form one of manga's most reluctant working relationships. Each volume is a self-contained heist or spy mission with absurd twists.",
        "whyILoveIt": "From Eroica with Love is one of the funniest manga I know. Aoike clearly loves her premise — the gay art thief and the homophobic spy who keep ending up on the same team — and milks it for forty volumes without losing the joke. The Cold War details age in interesting ways. The relationships age perfectly.",
        "publishedAt": pdate()
    },
    {
        "slug": "aim-for-the-ace",
        "title": "Aim for the Ace! Review: The Tennis Manga That Defined a Genre",
        "genre": "Sports / Drama", "genreSlug": "sports",
        "mangaTitle": "Aim for the Ace!", "mangaTitleJa": "エースをねらえ！",
        "mangaAuthor": "Sumika Yamamoto",
        "serialization": "Weekly Margaret", "publisher": "Shueisha",
        "volumes": 18, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "All Ages",
        "contentWarnings": ["death", "intense-training"],
        "description": "An ordinary girl is plucked from her tennis club to train under a brutal coach in the manga that built sports shojo.",
        "tags": ["sports", "tennis", "shojo", "classic"],
        "rating": 5,
        "quickTake": [
            "Foundational sports shojo, period",
            "Hiromi's growth arc is the template for the genre",
            "Coach Munakata is one of manga's most haunting mentors"
        ],
        "storyOverview": "Hiromi Oka is an unremarkable freshman on her school's tennis team. The new coach, Jin Munakata, sees something in her that no one else does — including herself — and pushes her into a training regimen that breaks down her game and her body. As she rises through the ranks, she meets her idol Reika 'Ochoufujin' Ryuzaki and discovers that the cost of greatness is higher than she imagined.",
        "whyILoveIt": "Aim for the Ace is hard to describe to people who didn't grow up with sports shojo. Hiromi's training feels almost spiritual. Coach Munakata isn't just a coach — he's a force. The manga doesn't romanticize the cost; it acknowledges it. By the end, you've watched a girl become something she never wanted to be, and you understand why.",
        "publishedAt": pdate()
    },
    {
        "slug": "helter-skelter",
        "title": "Helter Skelter Review: Kyoko Okazaki's Devastating Beauty Industry Drama",
        "genre": "Drama / Horror", "genreSlug": "horror",
        "mangaTitle": "Helter Skelter", "mangaTitleJa": "ヘルタースケルター",
        "mangaAuthor": "Kyoko Okazaki",
        "serialization": "Feel Young", "publisher": "Shodensha",
        "volumes": 1, "status": "Completed",
        "englishVolumes": 1, "englishStatus": "Complete",
        "ageRating": "M (Mature)",
        "contentWarnings": ["body-horror", "drug-use", "sexual-content", "self-harm"],
        "description": "A model whose beauty was built entirely from cosmetic surgery starts to fall apart in Kyoko Okazaki's devastating final manga.",
        "tags": ["drama", "horror", "josei", "fashion"],
        "rating": 5,
        "quickTake": [
            "Okazaki's final completed work — and her best",
            "About the violence of the beauty industry",
            "Painful, glamorous, unforgettable"
        ],
        "storyOverview": "Liliko is the most famous model in Japan. Her face, her body, her aura — none of it is real. She was built from surgeries, and the surgeries are starting to fail. As her body falls apart, her career, her relationships, and her sense of self collapse with it. Okazaki, who would soon stop drawing manga after a serious accident, made this her last completed work.",
        "whyILoveIt": "Helter Skelter is a horror story dressed as fashion media. Okazaki understood the violence of being looked at — what it does to a person to be desired and disposable at once. Liliko's collapse isn't punishment; it's inevitable. The manga is hard to read, but it's one of the most honest works about beauty culture ever published.",
        "publishedAt": pdate()
    },
    {
        "slug": "don-dracula",
        "title": "Don Dracula Review: Tezuka's Slapstick Vampire Sitcom",
        "genre": "Comedy / Horror", "genreSlug": "horror",
        "mangaTitle": "Don Dracula", "mangaTitleJa": "ドン・ドラキュラ",
        "mangaAuthor": "Osamu Tezuka",
        "serialization": "Weekly Shonen Champion", "publisher": "Akita Shoten",
        "volumes": 3, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["comedic-violence", "supernatural"],
        "description": "Count Dracula moves to Tokyo with his daughter and tries to live a normal life — Tezuka's gentlest horror comedy.",
        "tags": ["comedy", "horror", "tezuka", "supernatural"],
        "rating": 4,
        "quickTake": [
            "Tezuka in pure-comedy mode",
            "A vampire sitcom decades before vampire sitcoms",
            "Charming if minor late-period Tezuka"
        ],
        "storyOverview": "Count Dracula moves from Transylvania to Tokyo with his daughter Chocola because the supply of fresh blood in Europe has gotten complicated. He tries to fit into Japanese society — paying taxes, dealing with neighbors, sending Chocola to school. Each chapter is a self-contained gag about the gap between vampire culture and salaryman Tokyo.",
        "whyILoveIt": "Don Dracula is Tezuka having fun. There's no big philosophical argument, no tragedy. Just a vampire trying to live in modern Japan and a daughter who's more capable than he is. It's gentler than most of his work. Reading it feels like a vacation in the Tezuka universe.",
        "publishedAt": pdate()
    },
    {
        "slug": "marvelous-melmo",
        "title": "Marvelous Melmo Review: Tezuka's Sex Education Manga for Kids",
        "genre": "Sci-Fi / Slice-of-Life", "genreSlug": "slice-of-life",
        "mangaTitle": "Marvelous Melmo", "mangaTitleJa": "ふしぎなメルモ",
        "mangaAuthor": "Osamu Tezuka",
        "serialization": "Shogaku Ichinensei", "publisher": "Shogakukan",
        "volumes": 3, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "All Ages",
        "contentWarnings": ["mild-sexual-themes", "death"],
        "description": "A girl uses magic candy to age forward and back — Tezuka's strangely tender attempt at biology education for children.",
        "tags": ["sci-fi", "slice-of-life", "tezuka", "kids"],
        "rating": 4,
        "quickTake": [
            "Tezuka's gentlest, weirdest educational manga",
            "Originally serialized for first graders",
            "Surprisingly heavy themes under the cute exterior"
        ],
        "storyOverview": "Melmo is a nine-year-old girl whose dead mother left her a jar of magic candies. Red candies make her older, blue candies make her younger. She uses the candies to take care of her younger brothers and to navigate adult problems. Along the way, Tezuka sneaks in lessons about biology, reproduction, and growing up — all aimed at children too young for that kind of conversation.",
        "whyILoveIt": "Marvelous Melmo is one of the most quietly strange manga in Tezuka's catalog. It's for kids, but it's about death, sex, and growing up. Melmo carries her mother's love through every transformation. The biology lessons are direct without being lurid. It's the kind of manga only Tezuka would have tried.",
        "publishedAt": pdate()
    },
    {
        "slug": "triton-of-the-sea",
        "title": "Triton of the Sea Review: Tezuka's Underwater Mythology",
        "genre": "Fantasy / Adventure", "genreSlug": "fantasy",
        "mangaTitle": "Triton of the Sea", "mangaTitleJa": "海のトリトン",
        "mangaAuthor": "Osamu Tezuka",
        "serialization": "Sankei Shimbun", "publisher": "Sankei",
        "volumes": 4, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "All Ages",
        "contentWarnings": ["violence", "death"],
        "description": "A boy raised on land discovers he's the last prince of an ancient sea kingdom — Tezuka's lost-mythology epic.",
        "tags": ["fantasy", "adventure", "tezuka", "mythology"],
        "rating": 4,
        "quickTake": [
            "Mid-period Tezuka mythology adventure",
            "Better known for the anime, but the manga is darker",
            "Underwater worldbuilding rare for the era"
        ],
        "storyOverview": "Triton is a boy raised by a fisherman after being washed ashore as an infant. He doesn't know he's the last surviving member of the Triton clan, sea people massacred by the cruel Poseidon and his army. As his powers awaken, he sets out to avenge his people and rebuild what was destroyed. The manga ending is far darker than the anime adaptation.",
        "whyILoveIt": "Triton of the Sea is a Tezuka adventure done right. The mythology is dense without being confusing, the underwater designs are gorgeous, and Triton himself is a more complicated hero than the anime version. The ending — quiet, tragic, ambiguous — is one of Tezuka's best.",
        "publishedAt": pdate()
    },
    {
        "slug": "boku-no-son-goku",
        "title": "Boku no Son Goku Review: Tezuka's Take on the Monkey King",
        "genre": "Fantasy / Adventure", "genreSlug": "fantasy",
        "mangaTitle": "Boku no Son Goku", "mangaTitleJa": "ぼくの孫悟空",
        "mangaAuthor": "Osamu Tezuka",
        "serialization": "Manga-Oh", "publisher": "Akita Shoten",
        "volumes": 8, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "All Ages",
        "contentWarnings": ["violence"],
        "description": "Tezuka's lifelong love affair with Sun Wukong — a Journey to the West retelling that influenced Toriyama directly.",
        "tags": ["fantasy", "adventure", "tezuka", "classic"],
        "rating": 4,
        "quickTake": [
            "Tezuka's reverent adaptation of Journey to the West",
            "Direct ancestor of Toriyama's Dragon Ball",
            "Long but rewarding for fans of Asian mythology"
        ],
        "storyOverview": "Tezuka adapts the classic Chinese epic Journey to the West, following Sun Wukong from his birth out of stone through his rebellion against heaven, his imprisonment, and his journey west with the monk Tripitaka. Tezuka was obsessed with Wukong his entire career — this was his definitive version. Toriyama acknowledged it as foundational influence on Dragon Ball.",
        "whyILoveIt": "Boku no Son Goku is Tezuka loving the source material. Every page feels like a tribute. Wukong is mischievous and powerful and lonely, all at once. Knowing how much this manga shaped Dragon Ball makes it doubly interesting — you can see Toriyama's instincts forming as you read.",
        "publishedAt": pdate()
    },
    {
        "slug": "crime-and-punishment-tezuka",
        "title": "Crime and Punishment Review: Tezuka Adapts Dostoevsky",
        "genre": "Drama / Historical", "genreSlug": "slice-of-life",
        "mangaTitle": "Crime and Punishment", "mangaTitleJa": "罪と罰",
        "mangaAuthor": "Osamu Tezuka",
        "serialization": "Tezuka Productions", "publisher": "Tobunsha",
        "volumes": 1, "status": "Completed",
        "englishVolumes": 1, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["murder", "violence", "psychological-distress"],
        "description": "Tezuka condenses Dostoevsky's novel into a single volume of breakneck moral urgency.",
        "tags": ["drama", "historical", "tezuka", "literature"],
        "rating": 4,
        "quickTake": [
            "Tezuka adapting Dostoevsky in one volume",
            "Faster, leaner, surprisingly faithful",
            "An unusual entry point to both Tezuka and Russian literature"
        ],
        "storyOverview": "Tezuka adapts Dostoevsky's Crime and Punishment into a single volume, following the impoverished student Raskolnikov as he murders an old pawnbroker, justifies it to himself, and slowly disintegrates under the weight of what he's done. Tezuka simplifies aggressively but keeps the moral architecture intact. It's a remarkable feat of compression.",
        "whyILoveIt": "Tezuka's Crime and Punishment is a fascinating exercise. He couldn't fit everything from the novel, so he had to choose — and the choices reveal what he thought mattered. Raskolnikov's guilt, Sonia's faith, Porfiry's quiet pursuit. It's Tezuka teaching himself adaptation, and it works.",
        "publishedAt": pdate()
    },
    {
        "slug": "nextworld-tezuka",
        "title": "Nextworld Review: Tezuka's Cold War Sci-Fi Allegory",
        "genre": "Sci-Fi / Drama", "genreSlug": "sci-fi",
        "mangaTitle": "Nextworld", "mangaTitleJa": "来るべき世界",
        "mangaAuthor": "Osamu Tezuka",
        "serialization": "Various", "publisher": "Fusosha",
        "volumes": 2, "status": "Completed",
        "englishVolumes": 2, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["nuclear-war", "violence", "death"],
        "description": "Two superpowers test bombs that mutate animals into intelligent beings — Tezuka's Cold War allegory drawn in 1951.",
        "tags": ["sci-fi", "tezuka", "cold-war", "classic"],
        "rating": 4,
        "quickTake": [
            "1951 Cold War sci-fi from Tezuka",
            "Surprising mature themes for early shonen-ish work",
            "Direct ancestor of countless mutant-future stories"
        ],
        "storyOverview": "Two world powers, Star and Uran, test nuclear weapons in a remote area. The radiation creates Furubuta — animal-derived beings with human intelligence. Both governments want to use them as weapons. The Furubuta want to be left alone. Caught between are scientists, soldiers, and ordinary people trying to figure out what to do with a new species.",
        "whyILoveIt": "Nextworld is Tezuka writing about the bomb in 1951, when the wounds were still fresh. The political allegory is barely disguised. The Furubuta are sympathetic in a way that makes the human characters look small. For an early Tezuka work, it's strikingly mature about war and prejudice.",
        "publishedAt": pdate()
    },
    {
        "slug": "lost-world-tezuka",
        "title": "Lost World Review: Tezuka's Early Sci-Fi Adventure",
        "genre": "Sci-Fi / Adventure", "genreSlug": "sci-fi",
        "mangaTitle": "Lost World", "mangaTitleJa": "ロストワールド",
        "mangaAuthor": "Osamu Tezuka",
        "serialization": "Standalone", "publisher": "Fusosha",
        "volumes": 2, "status": "Completed",
        "englishVolumes": 2, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["violence", "death"],
        "description": "Earth scientists travel to a planet of plant people and prehistoric beasts in Tezuka's foundational early sci-fi.",
        "tags": ["sci-fi", "tezuka", "adventure", "classic"],
        "rating": 4,
        "quickTake": [
            "One of Tezuka's earliest sci-fi epics",
            "Influenced by Edgar Rice Burroughs and pulp",
            "Crude in places, foundational in others"
        ],
        "storyOverview": "When a strange planet appears near Earth, a team of scientists is sent to explore it. They discover a world of intelligent plant people and prehistoric monsters — and a colonial conflict already in progress. Tezuka, drawing on the pulp adventure stories of his youth, fills the book with weird creatures, narrow escapes, and a moral arc about humans' tendency to spoil everything they touch.",
        "whyILoveIt": "Lost World is Tezuka stretching his legs in sci-fi. It's not as polished as later work, but the imagination is already there. The plant people are particularly memorable — sympathetic, alien, and doomed by human contact. Reading it next to Nextworld and Metropolis, you watch Tezuka inventing Japanese sci-fi manga in real time.",
        "publishedAt": pdate()
    },
    {
        "slug": "captain-ken",
        "title": "Captain Ken Review: Tezuka's Western on Mars",
        "genre": "Sci-Fi / Western", "genreSlug": "sci-fi",
        "mangaTitle": "Captain Ken", "mangaTitleJa": "キャプテンKen",
        "mangaAuthor": "Osamu Tezuka",
        "serialization": "Weekly Shonen Sunday", "publisher": "Shogakukan",
        "volumes": 2, "status": "Completed",
        "englishVolumes": 0, "englishStatus": "Unlicensed",
        "ageRating": "T (Teen)",
        "contentWarnings": ["violence", "indigenous-genocide-themes"],
        "description": "A masked gunslinger fights for the rights of Mars's indigenous people — Tezuka's allegory for the American West.",
        "tags": ["sci-fi", "western", "tezuka", "classic"],
        "rating": 4,
        "quickTake": [
            "Tezuka's space western from 1960",
            "Open allegory about colonization of the American West",
            "Featuring one of his more interesting young protagonists"
        ],
        "storyOverview": "On a colonized Mars, the indigenous Martians are being slaughtered by Earth settlers and the corporations behind them. A masked gunslinger named Captain Ken keeps appearing to save them. He's faster, smarter, and more ruthless than anyone — and his identity is the manga's central mystery. Tezuka uses every Western trope and turns most of them inside out.",
        "whyILoveIt": "Captain Ken is Tezuka taking on the Western. He uses the genre to talk about what colonization actually looks like — the casual murder, the bureaucratic cruelty, the way 'civilization' justifies its violence. Captain Ken himself is one of his more morally complex heroes. The mask hides more than identity.",
        "publishedAt": pdate()
    },
    {
        "slug": "paros-no-ken",
        "title": "The Sword of Paros Review: One of the Earliest Yuri Manga",
        "genre": "Romance / Fantasy", "genreSlug": "fantasy",
        "mangaTitle": "The Sword of Paros", "mangaTitleJa": "パロスの剣",
        "mangaAuthor": "Kaoru Kurimoto, Yumiko Igarashi",
        "serialization": "Asuka Comics", "publisher": "Kadokawa",
        "volumes": 1, "status": "Completed",
        "englishVolumes": 1, "englishStatus": "Complete",
        "ageRating": "T (Teen)",
        "contentWarnings": ["violence", "lgbtq-content"],
        "description": "A princess in love with her female slave — a foundational yuri text from 1986.",
        "tags": ["romance", "fantasy", "yuri", "lgbtq", "classic"],
        "rating": 4,
        "quickTake": [
            "One of the earliest yuri manga published",
            "Igarashi's Candy Candy art applied to a queer story",
            "Kurimoto's prose adapted into manga"
        ],
        "storyOverview": "Princess Erminia of Paros is supposed to marry a prince and continue her royal line. She's also in love with Fiona, a female slave from a fallen kingdom. As political pressure forces the marriage, Erminia disguises herself as a man, takes up a sword, and runs with Fiona. The story unfolds across one tight volume.",
        "whyILoveIt": "Sword of Paros is short and sharp. Kurimoto's prose chops, Igarashi's art is gorgeous in the Candy Candy way. The romance isn't tragic for the sake of it — Erminia and Fiona fight to make it work. For a manga published in 1986, the queerness is direct. It deserves to be more widely read.",
        "publishedAt": pdate()
    },
]

if __name__ == "__main__":
    run_batch(31, "classic shojo + Tezuka deep cuts", ARTICLES)
