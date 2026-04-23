import { MetadataRoute } from "next";
import { getAllArticles } from "@/lib/articles";
import { SITE_CONFIG } from "@/lib/types";

export default function sitemap(): MetadataRoute.Sitemap {
  const articles = getAllArticles();

  const articleEntries = articles.map((article) => ({
    url: `${SITE_CONFIG.url}/${article.genreSlug}/${article.slug}`,
    lastModified: new Date(article.frontmatter.updatedAt || article.frontmatter.publishedAt),
    changeFrequency: "monthly" as const,
    priority: 0.7,
  }));

  return [
    { url: SITE_CONFIG.url, lastModified: new Date(), priority: 1 },
    { url: `${SITE_CONFIG.url}/about`, lastModified: new Date(), priority: 0.5 },
    ...articleEntries,
  ];
}
