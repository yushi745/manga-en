import Link from "next/link";
import { Article } from "@/lib/types";
import CoverImage from "@/components/CoverImage";

export default function RelatedArticles({ articles }: { articles: Article[] }) {
  if (articles.length === 0) return null;

  return (
    <section className="mt-12 border-t border-gray-200 pt-8">
      <h2 className="mb-4 text-lg font-bold text-gray-900">
        More Manga You Might Like
      </h2>
      <div className="grid gap-3 sm:grid-cols-2">
        {articles.map((article) => (
          <Link
            key={`${article.genreSlug}/${article.slug}`}
            href={`/${article.genreSlug}/${article.slug}`}
            className="group flex gap-3 rounded-lg border border-gray-200 p-3 transition hover:border-red-300 hover:bg-red-50/30"
          >
            {article.frontmatter.coverImage ? (
              <div className="w-14 shrink-0">
                <CoverImage
                  src={article.frontmatter.coverImage}
                  alt={article.frontmatter.mangaTitle}
                  className="h-20 w-14 rounded object-cover"
                />
              </div>
            ) : (
              <div className="flex h-20 w-14 shrink-0 items-center justify-center rounded bg-gray-100 text-xs text-gray-400">
                No cover
              </div>
            )}
            <div className="min-w-0 flex-1">
              <p className="mb-1 text-xs text-gray-500">
                {article.frontmatter.genre}
              </p>
              <h3 className="line-clamp-2 text-sm font-semibold text-gray-900 group-hover:text-red-600">
                {article.frontmatter.mangaTitle}
              </h3>
              <p className="mt-1 line-clamp-2 text-xs text-gray-600">
                {article.frontmatter.description}
              </p>
            </div>
          </Link>
        ))}
      </div>
    </section>
  );
}
