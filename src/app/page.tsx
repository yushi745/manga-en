import Link from "next/link";
import { getAllArticles, getGenresWithCount } from "@/lib/articles";
import { SITE_CONFIG } from "@/lib/types";
import ArticleCard from "@/components/ArticleCard";

export default function Home() {
  const articles = getAllArticles();
  const genres = getGenresWithCount();
  const latestArticles = articles.slice(0, 10);

  return (
    <div className="mx-auto max-w-4xl px-4 py-8">
      {/* Hero */}
      <section className="mb-12 text-center">
        <h1 className="mb-2 text-3xl font-bold text-gray-900">
          {SITE_CONFIG.name}
        </h1>
        <p className="mb-4 text-sm font-medium text-red-500">
          {SITE_CONFIG.subtitle}
        </p>
        <p className="mx-auto max-w-2xl text-base leading-relaxed text-gray-600">
          {SITE_CONFIG.description}
        </p>
      </section>

      {/* Genre Navigation */}
      {genres.length > 0 && (
        <section className="mb-10">
          <h2 className="mb-4 text-lg font-bold text-gray-900">Browse by Genre</h2>
          <div className="flex flex-wrap gap-2">
            {genres.map((genre) => (
              <Link
                key={genre.slug}
                href={`/${genre.slug}`}
                className="rounded-full border border-gray-200 bg-white px-4 py-2 text-sm text-gray-700 transition hover:border-red-300 hover:bg-red-50 hover:text-red-700"
              >
                {genre.name}
                <span className="ml-1 text-xs text-gray-400">({genre.count})</span>
              </Link>
            ))}
          </div>
        </section>
      )}

      {/* Latest Reviews */}
      <section>
        <h2 className="mb-4 text-lg font-bold text-gray-900">Latest Reviews</h2>
        {latestArticles.length > 0 ? (
          <div className="grid gap-4">
            {latestArticles.map((article) => (
              <ArticleCard
                key={`${article.genreSlug}/${article.slug}`}
                article={article}
              />
            ))}
          </div>
        ) : (
          <p className="rounded-lg bg-gray-50 p-8 text-center text-gray-500">
            Reviews coming soon. Stay tuned!
          </p>
        )}
      </section>
    </div>
  );
}
