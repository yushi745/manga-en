export default function AffiliateButton({
  url,
  mangaTitle,
  showTeaser = false,
}: {
  url: string;
  mangaTitle: string;
  showTeaser?: boolean;
}) {
  return (
    <div className="my-6 text-center">
      {showTeaser && (
        <p className="mb-3 text-sm text-gray-600">
          Read the first volume. If it doesn&apos;t hook you, put it down. It&apos;ll hook you.
        </p>
      )}
      <a
        href={url}
        target="_blank"
        rel="noopener noreferrer nofollow"
        className="inline-block rounded-lg bg-orange-500 px-8 py-3 text-base font-bold text-white shadow transition hover:bg-orange-600"
      >
        Buy {mangaTitle} on Amazon →
      </a>
      <p className="mt-2 text-xs text-gray-400">
        *Affiliate link — I earn a small commission at no extra cost to you.
      </p>
    </div>
  );
}
