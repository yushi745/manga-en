import { notFound } from "next/navigation";
import { getArticlesByGenre, getGenresWithCount } from "@/lib/articles";
import { GENRES } from "@/lib/types";
import ArticleCard from "@/components/ArticleCard";
import Breadcrumb from "@/components/Breadcrumb";
import type { Metadata } from "next";

interface Props {
  params: Promise<{ genre: string }>;
}

export async function generateStaticParams() {
  const genres = getGenresWithCount();
  return genres.map((g) => ({ genre: g.slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { genre } = await params;
  const genreName = GENRES[genre];
  if (!genreName) return {};

  return {
    title: `${genreName} Manga Reviews`,
    description: `Reviews and guides for the best ${genreName} manga. Find your next favorite series with Yu's honest picks.`,
  };
}

export default async function GenrePage({ params }: Props) {
  const { genre } = await params;
  const genreName = GENRES[genre];

  if (!genreName) notFound();

  const articles = getArticlesByGenre(genre);

  return (
    <div className="mx-auto max-w-4xl px-4 py-8">
      <Breadcrumb items={[{ label: genreName }]} />

      <h1 className="mb-2 text-2xl font-bold text-gray-900">
        {genreName} Manga Reviews
      </h1>
      <p className="mb-8 text-sm text-gray-500">
        {articles.length} review{articles.length !== 1 ? "s" : ""} in this genre
      </p>

      {articles.length > 0 ? (
        <div className="grid gap-4">
          {articles.map((article) => (
            <ArticleCard
              key={`${article.genreSlug}/${article.slug}`}
              article={article}
            />
          ))}
        </div>
      ) : (
        <p className="rounded-lg bg-gray-50 p-8 text-center text-gray-500">
          Reviews for this genre are coming soon!
        </p>
      )}
    </div>
  );
}
