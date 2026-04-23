import { notFound } from "next/navigation";
import { getArticle, getArticleSlugs } from "@/lib/articles";
import { GENRES, SITE_CONFIG } from "@/lib/types";
import { generateBookPageUrl, generateBookSearchUrl } from "@/lib/affiliate";
import Breadcrumb from "@/components/Breadcrumb";
import MarkdownContent from "@/components/MarkdownContent";
import AuthorBox from "@/components/AuthorBox";
import AffiliateButton from "@/components/AffiliateButton";
import type { Metadata } from "next";

interface Props {
  params: Promise<{ genre: string; slug: string }>;
}

export async function generateStaticParams() {
  return getArticleSlugs().map(({ genreSlug, slug }) => ({
    genre: genreSlug,
    slug,
  }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { genre, slug } = await params;
  const article = getArticle(genre, slug);
  if (!article) return {};

  const { frontmatter } = article;

  return {
    title: frontmatter.title,
    description: frontmatter.description,
    openGraph: {
      title: frontmatter.title,
      description: frontmatter.description,
      type: "article",
      publishedTime: frontmatter.publishedAt,
      modifiedTime: frontmatter.updatedAt,
      authors: [SITE_CONFIG.author.name],
    },
  };
}

export default async function ArticlePage({ params }: Props) {
  const { genre, slug } = await params;
  const article = getArticle(genre, slug);

  if (!article) notFound();

  const { frontmatter, content } = article;
  const genreName = GENRES[genre] || frontmatter.genre;

  const buyUrl = frontmatter.amazonASIN
    ? generateBookPageUrl(frontmatter.amazonASIN)
    : generateBookSearchUrl(frontmatter.mangaTitle);

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Review",
    name: frontmatter.title,
    description: frontmatter.description,
    author: {
      "@type": "Person",
      name: SITE_CONFIG.author.name,
    },
    datePublished: frontmatter.publishedAt,
    dateModified: frontmatter.updatedAt || frontmatter.publishedAt,
    reviewRating: {
      "@type": "Rating",
      ratingValue: frontmatter.rating,
      bestRating: 5,
    },
    itemReviewed: {
      "@type": "Book",
      name: frontmatter.mangaTitle,
      author: {
        "@type": "Person",
        name: frontmatter.mangaAuthor,
      },
      ...(frontmatter.coverImage && { image: frontmatter.coverImage }),
    },
    publisher: {
      "@type": "Organization",
      name: SITE_CONFIG.name,
    },
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />

      <article className="mx-auto max-w-3xl px-4 py-8">
        <Breadcrumb
          items={[
            { label: genreName, href: `/${genre}` },
            { label: frontmatter.mangaTitle },
          ]}
        />

        <header className="mb-8">
          <div className="flex gap-6">
            {frontmatter.coverImage && (
              <div className="shrink-0">
                <img
                  src={frontmatter.coverImage}
                  alt={frontmatter.mangaTitle}
                  className="h-40 w-28 rounded object-cover shadow"
                />
              </div>
            )}
            <div>
              <h1 className="mb-2 text-2xl font-bold leading-tight text-gray-900">
                {frontmatter.title}
              </h1>
              <p className="mb-1 text-sm text-gray-600">by {frontmatter.mangaAuthor}</p>
              <div className="flex flex-wrap items-center gap-3 text-sm">
                <span className="text-yellow-500">
                  {"★".repeat(Math.round(frontmatter.rating))}
                  {"☆".repeat(5 - Math.round(frontmatter.rating))}
                </span>
                {frontmatter.status && (
                  <span className={`rounded px-2 py-0.5 text-xs font-medium ${frontmatter.status === "Completed" ? "bg-green-100 text-green-700" : "bg-blue-100 text-blue-700"}`}>
                    {frontmatter.status}
                  </span>
                )}
                {frontmatter.ageRating && (
                  <span className="rounded bg-gray-100 px-2 py-0.5 text-xs text-gray-600">
                    {frontmatter.ageRating}
                  </span>
                )}
              </div>
              <div className="mt-2 flex items-center gap-3 text-xs text-gray-400">
                <span>Reviewed by {SITE_CONFIG.author.name}</span>
                <time dateTime={frontmatter.publishedAt}>
                  {new Date(frontmatter.publishedAt).toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" })}
                </time>
              </div>
            </div>
          </div>
        </header>

        <AffiliateButton url={buyUrl} mangaTitle={frontmatter.mangaTitle} />

        <MarkdownContent content={content} />

        <AffiliateButton url={buyUrl} mangaTitle={frontmatter.mangaTitle} />

        <AuthorBox />

        {frontmatter.hasAffiliate && (
          <p className="mt-4 text-xs text-gray-400">
            Disclosure: This post contains affiliate links. As an Amazon Associate,
            I earn from qualifying purchases at no extra cost to you.
          </p>
        )}
      </article>
    </>
  );
}
