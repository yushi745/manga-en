import { getAllGuides } from "@/lib/guides";
import { SITE_CONFIG } from "@/lib/types";
import Link from "next/link";
import Breadcrumb from "@/components/Breadcrumb";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: `Manga Guides & Best-of Lists | ${SITE_CONFIG.name}`,
  description:
    "Curated manga reading guides and best-of lists by Yu. Find the best manga by genre, mood, or what to read next.",
};

export default function GuidesPage() {
  const guides = getAllGuides();

  return (
    <div className="mx-auto max-w-4xl px-4 py-8">
      <Breadcrumb items={[{ label: "Guides" }]} />

      <h1 className="mb-2 text-2xl font-bold text-gray-900">Manga Guides & Best-of Lists</h1>
      <p className="mb-8 text-sm text-gray-500">
        Not sure what to read next? Start here.
      </p>

      {guides.length > 0 ? (
        <div className="grid gap-4">
          {guides.map((guide) => (
            <Link
              key={guide.slug}
              href={`/guides/${guide.slug}`}
              className="group block rounded-lg border border-gray-200 bg-white p-5 transition hover:shadow-md"
            >
              <h2 className="mb-1 text-base font-bold text-gray-900 group-hover:text-red-600">
                {guide.frontmatter.title}
              </h2>
              <p className="mb-2 text-sm text-gray-600">{guide.frontmatter.description}</p>
              <time className="text-xs text-gray-400" dateTime={guide.frontmatter.publishedAt}>
                {new Date(guide.frontmatter.publishedAt).toLocaleDateString("en-US", {
                  year: "numeric",
                  month: "short",
                  day: "numeric",
                })}
              </time>
            </Link>
          ))}
        </div>
      ) : (
        <p className="rounded-lg bg-gray-50 p-8 text-center text-gray-500">
          Guides coming soon.
        </p>
      )}
    </div>
  );
}
