import Link from "next/link";
import { Guide } from "@/lib/types";

export default function RelatedGuides({ guides }: { guides: Guide[] }) {
  if (guides.length === 0) return null;

  return (
    <section className="mt-10 rounded-lg border border-gray-200 bg-gray-50 p-5">
      <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-gray-500">
        Reading Guides
      </h2>
      <ul className="space-y-2">
        {guides.map((guide) => (
          <li key={guide.slug}>
            <Link
              href={`/guides/${guide.slug}`}
              className="group flex items-start gap-2 text-sm"
            >
              <span className="mt-0.5 text-red-400">→</span>
              <span className="text-gray-800 group-hover:text-red-600 group-hover:underline">
                {guide.frontmatter.title}
              </span>
            </Link>
          </li>
        ))}
      </ul>
    </section>
  );
}
