import fs from "fs";
import path from "path";
import matter from "gray-matter";
import { Article, ArticleFrontmatter, GENRES } from "./types";

const articlesDirectory = path.join(process.cwd(), "src/content/articles");

export function getArticleSlugs(): { genreSlug: string; slug: string }[] {
  if (!fs.existsSync(articlesDirectory)) return [];

  const genres = fs
    .readdirSync(articlesDirectory, { withFileTypes: true })
    .filter((d) => d.isDirectory());

  const slugs: { genreSlug: string; slug: string }[] = [];

  for (const genre of genres) {
    const genrePath = path.join(articlesDirectory, genre.name);
    const files = fs
      .readdirSync(genrePath)
      .filter((f) => f.endsWith(".md") || f.endsWith(".mdx"));

    for (const file of files) {
      slugs.push({
        genreSlug: genre.name,
        slug: file.replace(/\.mdx?$/, ""),
      });
    }
  }

  return slugs;
}

export function getArticle(genreSlug: string, slug: string): Article | null {
  const mdxPath = path.join(articlesDirectory, genreSlug, `${slug}.mdx`);
  const mdPath = path.join(articlesDirectory, genreSlug, `${slug}.md`);

  const filePath = fs.existsSync(mdxPath)
    ? mdxPath
    : fs.existsSync(mdPath)
      ? mdPath
      : null;

  if (!filePath) return null;

  const fileContents = fs.readFileSync(filePath, "utf8");
  const { data, content } = matter(fileContents);

  return {
    frontmatter: data as ArticleFrontmatter,
    content,
    slug,
    genreSlug,
  };
}

export function getAllArticles(): Article[] {
  const slugs = getArticleSlugs();
  const articles = slugs
    .map(({ genreSlug, slug }) => getArticle(genreSlug, slug))
    .filter((a): a is Article => a !== null);

  return articles.sort(
    (a, b) =>
      new Date(b.frontmatter.publishedAt).getTime() -
      new Date(a.frontmatter.publishedAt).getTime()
  );
}

export function getArticlesByGenre(genreSlug: string): Article[] {
  return getAllArticles().filter((a) => a.genreSlug === genreSlug);
}

export function getRelatedArticles(
  current: Article,
  limit: number = 6
): Article[] {
  const all = getAllArticles().filter(
    (a) =>
      a.slug !== current.slug &&
      !a.frontmatter.noindex
  );

  const currentTags = new Set(current.frontmatter.tags || []);

  const scored = all.map((a) => {
    const sameGenre = a.genreSlug === current.genreSlug ? 1 : 0;
    const tagOverlap = (a.frontmatter.tags || []).filter((t) =>
      currentTags.has(t)
    ).length;
    // Genre match weighted 3, each tag overlap = 1, rating adds tiebreaker
    const score = sameGenre * 3 + tagOverlap + (a.frontmatter.rating || 0) * 0.01;
    return { article: a, score };
  });

  return scored
    .filter((s) => s.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, limit)
    .map((s) => s.article);
}

export function getTitleToUrlMap(): Map<string, string> {
  const map = new Map<string, string>();
  for (const article of getAllArticles()) {
    if (article.frontmatter.noindex) continue;
    const title = article.frontmatter.mangaTitle;
    if (title) {
      map.set(title.toLowerCase(), `/${article.genreSlug}/${article.slug}`);
    }
  }
  return map;
}

export function getGenresWithCount(): { slug: string; name: string; count: number }[] {
  const articles = getAllArticles();
  const genreCounts: Record<string, number> = {};

  for (const article of articles) {
    genreCounts[article.genreSlug] = (genreCounts[article.genreSlug] || 0) + 1;
  }

  return Object.entries(GENRES)
    .map(([slug, name]) => ({
      slug,
      name,
      count: genreCounts[slug] || 0,
    }))
    .filter((g) => g.count > 0)
    .sort((a, b) => b.count - a.count);
}
