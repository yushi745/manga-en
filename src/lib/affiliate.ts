const AMAZON_TAG = process.env.NEXT_PUBLIC_AMAZON_ASSOCIATE_TAG || "";

export function generateBookPageUrl(asin: string): string {
  const baseUrl = `https://www.amazon.com/dp/${asin}`;
  return AMAZON_TAG ? `${baseUrl}?tag=${AMAZON_TAG}` : baseUrl;
}

export function generateBookSearchUrl(mangaTitle: string): string {
  const baseUrl = `https://www.amazon.com/s?k=${encodeURIComponent(mangaTitle)}&i=stripbooks`;
  return AMAZON_TAG ? `${baseUrl}&tag=${AMAZON_TAG}` : baseUrl;
}

export function getAmazonTag(): string {
  return AMAZON_TAG;
}
