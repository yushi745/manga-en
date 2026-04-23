import { remark } from "remark";
import remarkGfm from "remark-gfm";
import html from "remark-html";

export default async function MarkdownContent({ content }: { content: string }) {
  const result = await remark().use(remarkGfm).use(html).process(content);
  const htmlContent = result.toString();

  return (
    <div
      className="prose prose-gray mx-auto max-w-none prose-headings:text-gray-900 prose-h2:mt-10 prose-h2:border-b prose-h2:border-gray-200 prose-h2:pb-2 prose-h2:text-xl prose-h3:text-lg prose-p:leading-relaxed prose-a:text-red-600 prose-strong:text-gray-900 prose-ul:my-4 prose-li:my-1 prose-table:my-4 prose-th:bg-gray-50 prose-th:px-4 prose-th:py-2 prose-td:px-4 prose-td:py-2"
      dangerouslySetInnerHTML={{ __html: htmlContent }}
    />
  );
}
