import fs from "fs";
import path from "path";
import matter from "gray-matter";
import { Guide, GuideFrontmatter } from "./types";

const guidesDirectory = path.join(process.cwd(), "src/content/guides");

export function getGuideSlugs(): string[] {
  if (!fs.existsSync(guidesDirectory)) return [];
  return fs
    .readdirSync(guidesDirectory)
    .filter((f) => f.endsWith(".md") || f.endsWith(".mdx"))
    .map((f) => f.replace(/\.mdx?$/, ""));
}

export function getGuide(slug: string): Guide | null {
  const mdxPath = path.join(guidesDirectory, `${slug}.mdx`);
  const mdPath = path.join(guidesDirectory, `${slug}.md`);
  const filePath = fs.existsSync(mdxPath) ? mdxPath : fs.existsSync(mdPath) ? mdPath : null;
  if (!filePath) return null;

  const { data, content } = matter(fs.readFileSync(filePath, "utf8"));
  return { frontmatter: data as GuideFrontmatter, content, slug };
}

export function getAllGuides(): Guide[] {
  return getGuideSlugs()
    .map((slug) => getGuide(slug))
    .filter((g): g is Guide => g !== null)
    .sort(
      (a, b) =>
        new Date(b.frontmatter.publishedAt).getTime() -
        new Date(a.frontmatter.publishedAt).getTime()
    );
}

export function getGuidesByGenre(genreSlug: string): Guide[] {
  return getAllGuides().filter((g) => g.frontmatter.genreSlugs.includes(genreSlug));
}
