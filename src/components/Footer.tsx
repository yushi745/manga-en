import Link from "next/link";
import { SITE_CONFIG } from "@/lib/types";

export default function Footer() {
  return (
    <footer className="mt-auto border-t border-gray-200 bg-gray-50">
      <div className="mx-auto max-w-4xl px-4 py-8">
        <div className="flex flex-col items-center gap-4 text-center">
          <Link href="/" className="text-lg font-bold text-gray-900">
            {SITE_CONFIG.name}
          </Link>
          <p className="max-w-md text-sm text-gray-500">
            {SITE_CONFIG.description}
          </p>
          <nav className="flex gap-6 text-sm">
            <Link href="/" className="text-gray-500 hover:text-gray-700">
              Home
            </Link>
            <Link href="/about" className="text-gray-500 hover:text-gray-700">
              About
            </Link>
          </nav>
          <p className="max-w-xl text-xs text-gray-400">
            This site contains affiliate links. As an Amazon Associate, I earn
            from qualifying purchases. This comes at no extra cost to you.
          </p>
          <p className="text-xs text-gray-400">
            &copy; {new Date().getFullYear()} {SITE_CONFIG.name}
          </p>
        </div>
      </div>
    </footer>
  );
}
