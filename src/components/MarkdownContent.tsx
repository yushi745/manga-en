import { remark } from "remark";
import remarkGfm from "remark-gfm";
import html from "remark-html";

function escapeHtml(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function escapeRegex(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function autoLinkSimilarManga(
  htmlContent: string,
  titleMap: Map<string, string>
): string {
  if (titleMap.size === 0) return htmlContent;

  // Sort titles by length descending so longer titles match first
  const titles = Array.from(titleMap.keys()).sort(
    (a, b) => b.length - a.length
  );

  // Process each <td> cell in the document; only link the first occurrence per cell
  return htmlContent.replace(/<td>([^<]*)<\/td>/g, (_match, cellContent) => {
    // Already linked or empty
    if (!cellContent || cellContent.includes("<a ")) return _match;

    const lower = cellContent.toLowerCase();
    for (const title of titles) {
      // Match the title only if it appears at the start of the cell
      // followed by either end-of-string or a non-alphanumeric delimiter
      const pattern = new RegExp(
        `^(\\s*)(${escapeRegex(title)})(?=$|[\\s/,(.:;-]|&)`,
        "i"
      );
      const match = cellContent.match(pattern);
      if (match) {
        const url = titleMap.get(title)!;
        const before = match[1];
        const matchedText = match[2];
        const after = cellContent.slice(before.length + matchedText.length);
        return `<td>${before}<a href="${url}">${escapeHtml(matchedText)}</a>${after}</td>`;
      }
    }
    return _match;
  });
}

interface Props {
  content: string;
  titleMap?: Map<string, string>;
}

export default async function MarkdownContent({ content, titleMap }: Props) {
  const result = await remark().use(remarkGfm).use(html).process(content);
  let htmlContent = result.toString();

  if (titleMap && titleMap.size > 0) {
    htmlContent = autoLinkSimilarManga(htmlContent, titleMap);
  }

  return (
    <div
      className="prose prose-gray mx-auto max-w-none prose-headings:text-gray-900 prose-h2:mt-10 prose-h2:border-b prose-h2:border-gray-200 prose-h2:pb-2 prose-h2:text-xl prose-h3:text-lg prose-p:leading-relaxed prose-a:text-red-600 prose-strong:text-gray-900 prose-ul:my-4 prose-li:my-1 prose-table:my-4 prose-th:bg-gray-50 prose-th:px-4 prose-th:py-2 prose-td:px-4 prose-td:py-2"
      dangerouslySetInnerHTML={{ __html: htmlContent }}
    />
  );
}
