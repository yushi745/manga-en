import Link from "next/link";
import { SITE_CONFIG } from "@/lib/types";

export default function Header() {
  return (
    <header className="border-b border-gray-200 bg-white">
      <div className="mx-auto max-w-4xl px-4 py-4">
        <div className="flex items-center justify-between">
          <Link href="/" className="group">
            <span className="text-xl font-bold text-gray-900 group-hover:text-red-600">
              {SITE_CONFIG.name}
            </span>
            <span className="ml-2 text-xs text-gray-400">
              {SITE_CONFIG.subtitle}
            </span>
          </Link>
          <nav className="flex items-center gap-6 text-sm">
            <Link href="/" className="text-gray-600 hover:text-gray-900">
              Home
            </Link>
            <Link href="/about" className="text-gray-600 hover:text-gray-900">
              About
            </Link>
          </nav>
        </div>
      </div>
    </header>
  );
}
