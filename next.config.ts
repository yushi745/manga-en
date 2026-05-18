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
      // Stage 1: same slug, different genre (2026-05-18)
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
      // File move 2026-05-18: sci-fi/trigun → action/trigun-maximum
      { source: '/sci-fi/trigun', destination: '/action/trigun-maximum', permanent: true },
    ];
  },
};

export default nextConfig;
