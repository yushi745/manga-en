import { notFound } from "next/navigation";
import { getGuide, getGuideSlugs } from "@/lib/guides";
import { SITE_CONFIG } from "@/lib/types";
import Breadcrumb from "@/components/Breadcrumb";
import MarkdownContent from "@/components/MarkdownContent";
import AuthorBox from "@/components/AuthorBox";
import type { Metadata } from "next";

interface Props {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return getGuideSlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const guide = getGuide(slug);
  if (!guide) return {};

  const { frontmatter } = guide;
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

export default async function GuidePage({ params }: Props) {
  const { slug } = await params;
  const guide = getGuide(slug);

  if (!guide) notFound();

  const { frontmatter, content } = guide;

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: frontmatter.title,
    description: frontmatter.description,
    author: {
      "@type": "Person",
      name: SITE_CONFIG.author.name,
    },
    datePublished: frontmatter.publishedAt,
    dateModified: frontmatter.updatedAt || frontmatter.publishedAt,
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
        <Breadcrumb items={[{ label: "Guides", href: "/guides" }, { label: frontmatter.title }]} />

        <header className="mb-8">
          <h1 className="mb-3 text-2xl font-bold leading-tight text-gray-900">
            {frontmatter.title}
          </h1>
          <p className="text-base text-gray-600">{frontmatter.description}</p>
          <div className="mt-3 flex items-center gap-3 text-xs text-gray-400">
            <span>by {SITE_CONFIG.author.name}</span>
            <time dateTime={frontmatter.publishedAt}>
              {new Date(frontmatter.publishedAt).toLocaleDateString("en-US", {
                year: "numeric",
                month: "long",
                day: "numeric",
              })}
            </time>
          </div>
        </header>

        <MarkdownContent content={content} />

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
