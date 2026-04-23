import Link from "next/link";
import { Article } from "@/lib/types";

export default function ArticleCard({ article }: { article: Article }) {
  const { frontmatter, genreSlug, slug } = article;

  return (
    <article className="group rounded-lg border border-gray-200 bg-white p-4 transition hover:shadow-md">
      <Link href={`/${genreSlug}/${slug}`} className="block">
        <div className="flex gap-4">
          {frontmatter.coverImage && (
            <div className="w-20 shrink-0">
              <img
                src={frontmatter.coverImage}
                alt={frontmatter.mangaTitle}
                className="h-28 w-20 rounded object-cover"
              />
            </div>
          )}
          <div className="min-w-0 flex-1">
            <span className="mb-1 inline-block rounded bg-red-50 px-2 py-0.5 text-xs text-red-700">
              {frontmatter.genre}
            </span>
            <h2 className="mb-1 line-clamp-2 text-base font-bold text-gray-900 group-hover:text-red-600">
              {frontmatter.title}
            </h2>
            <p className="mb-1 text-xs text-gray-500">
              by {frontmatter.mangaAuthor}
            </p>
            <p className="line-clamp-2 text-sm text-gray-600">
              {frontmatter.description}
            </p>
            <div className="mt-2 flex items-center gap-3">
              <span className="text-xs text-yellow-500">
                {"★".repeat(Math.round(frontmatter.rating))}
                {"☆".repeat(5 - Math.round(frontmatter.rating))}
              </span>
              {frontmatter.status && (
                <span className={`text-xs font-medium ${frontmatter.status === "Completed" ? "text-green-600" : "text-blue-600"}`}>
                  {frontmatter.status}
                </span>
              )}
              <time className="text-xs text-gray-400" dateTime={frontmatter.publishedAt}>
                {new Date(frontmatter.publishedAt).toLocaleDateString("en-US", { year: "numeric", month: "short", day: "numeric" })}
              </time>
            </div>
          </div>
        </div>
      </Link>
    </article>
  );
}
