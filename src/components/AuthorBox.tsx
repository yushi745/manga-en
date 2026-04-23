import { SITE_CONFIG } from "@/lib/types";

export default function AuthorBox() {
  const { author } = SITE_CONFIG;

  return (
    <div className="my-8 rounded-lg border border-gray-200 bg-white p-6">
      <div className="flex items-start gap-4">
        <div className="flex h-16 w-16 shrink-0 items-center justify-center rounded-full bg-red-100 text-2xl font-bold text-red-600">
          {author.name.charAt(0)}
        </div>
        <div>
          <p className="text-xs text-gray-500">Written by</p>
          <p className="text-lg font-bold text-gray-900">{author.name}</p>
          <p className="mt-1 text-sm text-gray-500">{author.job}</p>
          <p className="mt-2 text-sm leading-relaxed text-gray-600">
            {author.bio}
          </p>
        </div>
      </div>
    </div>
  );
}
