import { MetadataRoute } from "next";
import { getAllArticles } from "@/lib/articles";
import { getAllGuides } from "@/lib/guides";
import { SITE_CONFIG } from "@/lib/types";

export default function sitemap(): MetadataRoute.Sitemap {
  const articles = getAllArticles();
  const guides = getAllGuides();

  // Only include articles Yu has actually read (`read: true`) and not explicitly noindex'd.
  // Articles without verified reading are noindex per CLAUDE-article.md and excluded here.
  const indexableArticles = articles.filter(
    (a) => a.frontmatter.read === true && a.frontmatter.noindex !== true
  );

  const articleEntries = indexableArticles.map((article) => ({
    url: `${SITE_CONFIG.url}/${article.genreSlug}/${article.slug}`,
    lastModified: new Date(article.frontmatter.updatedAt || article.frontmatter.publishedAt),
    changeFrequency: "monthly" as const,
    priority: 0.7,
  }));

  const guideEntries = guides
    .filter((g) => g.frontmatter.noindex !== true)
    .map((guide) => ({
      url: `${SITE_CONFIG.url}/guides/${guide.slug}`,
      lastModified: new Date(guide.frontmatter.updatedAt || guide.frontmatter.publishedAt),
      changeFrequency: "monthly" as const,
      priority: 0.8,
    }));

  return [
    { url: SITE_CONFIG.url, lastModified: new Date(), priority: 1 },
    { url: `${SITE_CONFIG.url}/guides`, lastModified: new Date(), priority: 0.6 },
    { url: `${SITE_CONFIG.url}/about`, lastModified: new Date(), priority: 0.5 },
    ...guideEntries,
    ...articleEntries,
  ];
}
