export interface ArticleFrontmatter {
  title: string;
  slug: string;
  genre: string;
  genreSlug: string;
  mangaTitle: string;
  mangaAuthor: string;
  serialization?: string;
  publisher?: string;
  volumes?: number;
  status?: "Completed" | "Ongoing" | "Hiatus";
  englishVolumes?: number;
  englishStatus?: "Complete" | "Ongoing" | "Unlicensed";
  ageRating?: string;
  contentWarnings?: string[];
  description: string;
  coverImage?: string;
  amazonASIN?: string;
  publishedAt: string;
  updatedAt?: string;
  tags: string[];
  rating: number;
  hasAffiliate?: boolean;
}

export interface Article {
  frontmatter: ArticleFrontmatter;
  content: string;
  slug: string;
  genreSlug: string;
}

export const GENRES: Record<string, string> = {
  action: "Action / Adventure",
  romance: "Romance",
  fantasy: "Fantasy",
  horror: "Horror / Thriller",
  "slice-of-life": "Slice of Life",
  sports: "Sports",
  "sci-fi": "Sci-Fi",
};

export const SITE_CONFIG = {
  name: "DearManga",
  subtitle: "Japanese Manga Reviews & Guides",
  description:
    "Yu, a manga fan from Japan, reviews Japanese manga for English-speaking readers. Honest reviews, cultural context, and everything you need to start reading.",
  url: "https://www.dearmanga.com",
  author: {
    name: "Yu",
    job: "Manga Enthusiast from Japan",
    bio: "I grew up in Japan and manga literally saved me during a tough time in elementary school. My English isn't perfect, but my love for manga is real — and I want to share it with you.",
  },
};
