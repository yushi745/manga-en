import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "m.media-amazon.com" },
      { protocol: "https", hostname: "images-na.ssl-images-amazon.com" },
      { protocol: "https", hostname: "covers.openlibrary.org" },
      { protocol: "https", hostname: "cdn.myanimelist.net" },
      { protocol: "https", hostname: "uploads.mangadex.org" },
    ],
  },
  async redirects() {
    return [
      // === File move 2026-05-18 ===
      { source: '/sci-fi/trigun', destination: '/action/trigun-maximum', permanent: true },

      // === Stage 1: same slug, different genre (2026-05-18) ===
      { source: '/action/talentless-nana', destination: '/horror/talentless-nana', permanent: true },
      { source: '/slice-of-life/happiness', destination: '/horror/happiness', permanent: true },
      { source: '/sports/a-drifting-life', destination: '/slice-of-life/a-drifting-life', permanent: true },
      { source: '/sci-fi/shangri-la-frontier', destination: '/action/shangri-la-frontier', permanent: true },
      { source: '/sci-fi/i-am-a-hero', destination: '/horror/i-am-a-hero', permanent: true },
      { source: '/sci-fi/choujin-x', destination: '/action/choujin-x', permanent: true },
      { source: '/horror/dororo', destination: '/action/dororo', permanent: true },
      { source: '/action/gleipnir', destination: '/horror/gleipnir', permanent: true },
      { source: '/fantasy/sengoku-youko', destination: '/action/sengoku-youko', permanent: true },
      { source: '/horror/pumpkin-scissors', destination: '/action/pumpkin-scissors', permanent: true },
      { source: '/sci-fi/kaiju-no-8', destination: '/action/kaiju-no-8', permanent: true },
      { source: '/romance/maison-ikkoku', destination: '/slice-of-life/maison-ikkoku', permanent: true },
      { source: '/sci-fi/log-horizon', destination: '/fantasy/log-horizon', permanent: true },
      { source: '/romance/wotakoi', destination: '/slice-of-life/wotakoi', permanent: true },
      { source: '/sci-fi/dusk-maiden-of-amnesia', destination: '/horror/dusk-maiden-of-amnesia', permanent: true },

      // === Stage 2: slug renames (2026-05-18) ===
      { source: '/fantasy/natsume-yuujinchou', destination: '/fantasy/natsumes-book-of-friends', permanent: true },
      { source: '/slice-of-life/daily-lives-high-school-boys', destination: '/slice-of-life/daily-lives-of-high-school-boys', permanent: true },
      { source: '/slice-of-life/yotsubato', destination: '/slice-of-life/yotsuba', permanent: true },
      { source: '/action/blade-of-immortal', destination: '/action/blade-of-the-immortal', permanent: true },
      { source: '/slice-of-life/moyasimon', destination: '/slice-of-life/moyashimon', permanent: true },
      { source: '/sports/ranma-half', destination: '/action/ranma', permanent: true },
      { source: '/fantasy/mahou-shoujo-ore', destination: '/action/magical-girl-ore', permanent: true },
      { source: '/slice-of-life/yuruyuri', destination: '/slice-of-life/yuru-yuri', permanent: true },
      { source: '/horror/kurosagi-corpse-delivery', destination: '/horror/kurosagi-corpse-delivery-service', permanent: true },
      { source: '/romance/senryuu-girl', destination: '/romance/senryu-girl', permanent: true },
      { source: '/romance/is-katsura', destination: '/romance/i-s', permanent: true },
      { source: '/fantasy/dungeon-of-black-company', destination: '/fantasy/the-dungeon-of-black-company', permanent: true },
      { source: '/romance/phantom-thief-jeanne', destination: '/romance/kamikaze-kaitou-jeanne', permanent: true },
      { source: '/sports/ookiku-furikabutte', destination: '/sports/big-windup', permanent: true },
      { source: '/sci-fi/certain-magical-index', destination: '/sci-fi/a-certain-magical-index', permanent: true },
      { source: '/fantasy/hayate-no-gotoku', destination: '/slice-of-life/hayate-the-combat-butler', permanent: true },
      { source: '/slice-of-life/gakuen-babysitters', destination: '/slice-of-life/school-babysitters', permanent: true },
      { source: '/romance/snow-white-red-hair', destination: '/romance/snow-white-with-the-red-hair', permanent: true },
      { source: '/sports/aim-for-ace', destination: '/sports/aim-for-the-ace', permanent: true },
      { source: '/romance/gotoubun', destination: '/romance/the-quintessential-quintuplets', permanent: true },
      { source: '/romance/citrus', destination: '/romance/citrus-manga', permanent: true },
      { source: '/action/summit-of-gods', destination: '/horror/the-summit-of-the-gods', permanent: true },
      { source: '/action/tenjo-tenge', destination: '/action/tenjho-tenge', permanent: true },
      { source: '/romance/rental-girlfriend', destination: '/romance/rent-a-girlfriend', permanent: true },
      { source: '/sci-fi/gunnm-last-order', destination: '/sci-fi/battle-angel-alita-last-order', permanent: true },
      { source: '/slice-of-life/himouto-umaru', destination: '/slice-of-life/himouto-umaru-chan', permanent: true },
      { source: '/action/classroom-of-elite', destination: '/action/classroom-of-the-elite', permanent: true },
      { source: '/fantasy/death-march', destination: '/fantasy/death-march-rhapsody', permanent: true },
      { source: '/fantasy/worlds-finest-assassin', destination: '/fantasy/worlds-finest-assassin-reincarnated', permanent: true },
      { source: '/romance/hirunaka-no-ryuusei', destination: '/romance/daytime-shooting-star', permanent: true },
      { source: '/slice-of-life/tonari-no-seki', destination: '/slice-of-life/my-neighbor-seki', permanent: true },
      { source: '/romance/world-god-only-knows', destination: '/romance/the-world-god-only-knows', permanent: true },
      { source: '/action/four-knights-of-apocalypse', destination: '/fantasy/four-knights-of-the-apocalypse', permanent: true },
      { source: '/sci-fi/evangelion-manga', destination: '/sci-fi/neon-genesis-evangelion', permanent: true },
      { source: '/romance/kodomo-no-omocha', destination: '/slice-of-life/kodocha', permanent: true },
      { source: '/romance/ceres-celestial', destination: '/romance/ceres-celestial-legend', permanent: true },
      { source: '/slice-of-life/showa', destination: '/slice-of-life/showa-history', permanent: true },
      { source: '/fantasy/the-beginning-after-the-end', destination: '/fantasy/beginning-after-the-end', permanent: true },
      { source: '/sports/real', destination: '/sports/real-manga', permanent: true },
      { source: '/romance/full-moon-sagashite', destination: '/romance/full-moon', permanent: true },
      { source: '/romance/sono-bisque', destination: '/romance/my-dress-up-darling', permanent: true },
      { source: '/action/full-metal-panic', destination: '/sci-fi/fullmetal-panic', permanent: true },
      { source: '/romance/nozaki-kun', destination: '/slice-of-life/monthly-girls-nozaki-kun', permanent: true },
      { source: '/action/brave10', destination: '/action/brave-10', permanent: true },
      { source: '/fantasy/omniscient-reader', destination: '/action/omniscient-readers-viewpoint', permanent: true },
      { source: '/sports/kuroko-basketball', destination: '/sports/kuroko-no-basket', permanent: true },
      { source: '/slice-of-life/miss-kobayashi-dragon-maid', destination: '/slice-of-life/miss-kobayashis-dragon-maid', permanent: true },
      { source: '/romance/dear-brother', destination: '/romance/oniisama-e', permanent: true },
      { source: '/sports/h2', destination: '/sports/h2-manga', permanent: true },
      { source: '/romance/uzaki-chan', destination: '/slice-of-life/uzaki-chan-wants-to-hang-out', permanent: true },
      { source: '/action/reborn', destination: '/action/katekyo-hitman-reborn', permanent: true },
      { source: '/fantasy/drugstore-another-world', destination: '/fantasy/drugstore-in-another-world', permanent: true },
      { source: '/horror/afterschool-nightmare', destination: '/horror/after-school-nightmare', permanent: true },
      { source: '/slice-of-life/shimanami-tasogare', destination: '/slice-of-life/our-dreams-at-dusk', permanent: true },
      { source: '/slice-of-life/oyasumi-punpun', destination: '/horror/goodnight-punpun', permanent: true },
      { source: '/fantasy/campfire-cooking-another-world', destination: '/fantasy/campfire-cooking-in-another-world', permanent: true },
      { source: '/fantasy/isekai-shokudou', destination: '/slice-of-life/restaurant-to-another-world', permanent: true },
      { source: '/romance/clannad', destination: '/romance/clannad-manga', permanent: true },
      { source: '/fantasy/phoenix-manga', destination: '/sci-fi/phoenix', permanent: true },
      { source: '/fantasy/wise-man-grandchild', destination: '/fantasy/wise-mans-grandchild', permanent: true },
      { source: '/slice-of-life/sweetness-lightning', destination: '/slice-of-life/sweetness-and-lightning', permanent: true },
      { source: '/romance/given', destination: '/romance/given-manga', permanent: true },
      { source: '/romance/we-were-there', destination: '/romance/bokura-ga-ita', permanent: true },
      { source: '/slice-of-life/grand-blue', destination: '/slice-of-life/grand-blue-dreaming', permanent: true },
      { source: '/fantasy/mushoku-tensei-jobless', destination: '/fantasy/mushoku-tensei', permanent: true },
      { source: '/action/pokemon-manga', destination: '/action/pokemon-adventures', permanent: true },
      { source: '/romance/ore-monogatari', destination: '/romance/my-love-story', permanent: true },
      // Additional verified renames
      { source: '/sports/kenichi-mightiest-disciple', destination: '/action/history-strongest-disciple-kenichi', permanent: true },
      { source: '/romance/shikimori', destination: '/romance/shikimori-not-just-a-cutie', permanent: true },
      { source: '/sports/how-heavy-are-dumbbells', destination: '/sports/how-heavy-are-the-dumbbells', permanent: true },
      { source: '/sports/danberu', destination: '/sports/how-heavy-are-the-dumbbells', permanent: true },
      { source: '/fantasy/kumo-desu-ga', destination: '/fantasy/im-a-spider', permanent: true },
      { source: '/slice-of-life/yokohama-kaidashi', destination: '/slice-of-life/yokohama-shopping-log', permanent: true },
      { source: '/fantasy/accomplishments-of-duke', destination: '/fantasy/accomplishments-of-the-dukes-daughter', permanent: true },
      { source: '/slice-of-life/angel-beats', destination: '/sci-fi/angel-beats-manga', permanent: true },
      { source: '/action/neuro', destination: '/horror/majin-neuro', permanent: true },
      { source: '/romance/the-ice-guy', destination: '/slice-of-life/ice-guy-cool-female-colleague', permanent: true },
      { source: '/fantasy/d-n-angel', destination: '/romance/dn-angel', permanent: true },
      { source: '/slice-of-life/komi-san', destination: '/slice-of-life/komi-cant-communicate', permanent: true },
      { source: '/action/origin', destination: '/sci-fi/origin-boichi', permanent: true },

      // === Stage 3: additional renames (2026-05-18) ===
      { source: '/fantasy/is-it-wrong-pick-up-girls', destination: '/fantasy/danmachi', permanent: true },
      { source: '/fantasy/dungeon-ni-deai', destination: '/fantasy/danmachi', permanent: true },
      { source: '/slice-of-life/otoyomegatari', destination: '/romance/brides-story', permanent: true },

      // Articles that existed as duplicates (deleted commit 46a1a55), canonical version found:
      { source: '/sports/march-comes-in-like-a-lion', destination: '/slice-of-life/3-gatsu-no-lion', permanent: true },
      { source: '/romance/march-comes-in-like-a-lion', destination: '/slice-of-life/3-gatsu-no-lion', permanent: true },
      { source: '/horror/junji-ito-collection', destination: '/horror/shiver-junji-ito', permanent: true },
      { source: '/fantasy/sergeant-frog', destination: '/action/sgt-frog', permanent: true },
      { source: '/fantasy/x-clamp', destination: '/fantasy/x1999', permanent: true },

      // === Genuinely missing articles (7 URLs) — will 404 naturally and drop from Google's index ===
      // - /sci-fi/darker-than-black + /action/darker-than-black-manga (both duplicates deleted, no replacement)
      // - /sci-fi/ran-and-the-gray-world
      // - /fantasy/maou-gakuin
      // - /fantasy/hero-is-overpowered-cautious
      // - /sci-fi/gundam (too generic — gundam-wing, gundam-seed, gundam-the-origin all exist)
      // - /romance/kare-kano (Kareshi Kanojo no Jijou — never written)
    ];
  },
};

export default nextConfig;
