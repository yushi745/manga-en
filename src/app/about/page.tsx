import { SITE_CONFIG } from "@/lib/types";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "About",
  description: `About ${SITE_CONFIG.author.name} and ${SITE_CONFIG.name} — a manga review site by a Japanese fan for English-speaking readers.`,
};

export default function AboutPage() {
  return (
    <div className="mx-auto max-w-3xl px-4 py-12">
      <h1 className="mb-8 text-2xl font-bold text-gray-900">About {SITE_CONFIG.name}</h1>

      <div className="mb-8 flex items-start gap-6">
        <div className="flex h-20 w-20 shrink-0 items-center justify-center rounded-full bg-red-100 text-3xl font-bold text-red-600">
          Y
        </div>
        <div>
          <h2 className="text-xl font-bold text-gray-900">Hi, I&apos;m Yu.</h2>
          <p className="mt-1 text-sm text-gray-500">{SITE_CONFIG.author.job}</p>
        </div>
      </div>

      <div className="prose prose-gray max-w-none">
        <p>
          When I was in elementary school, I was bullied. I had no friends. Every day
          felt lonely and long. The only thing that made me feel better was manga.
        </p>
        <p>
          I would come home, lock myself in my room, and read for hours. Naruto taught
          me to never give up. One Piece showed me what true friendship looks like.
          Those stories didn&apos;t just entertain me — they saved me.
        </p>
        <p>
          Now I&apos;m grown up, and I want to share that feeling with the world.
          I created {SITE_CONFIG.name} to introduce Japanese manga to English-speaking
          readers who might not know where to start.
        </p>
        <p>
          My English is not perfect. I know that. But my love for manga is real, and
          I will do my best to deliver that passion to you — one review at a time.
        </p>
        <h2>Why trust my reviews?</h2>
        <p>
          I grew up reading manga in Japanese. I understand the cultural context,
          the original nuances, and the things that often get lost in translation.
          I write these reviews to bridge that gap — to help you fully appreciate
          what makes Japanese manga so special.
        </p>
        <h2>Affiliate Disclosure</h2>
        <p>
          Some links on this site are affiliate links. As an Amazon Associate, I earn
          a small commission when you purchase through these links, at no extra cost
          to you. This helps me keep the site running. I only recommend manga I
          genuinely love.
        </p>
      </div>
    </div>
  );
}
