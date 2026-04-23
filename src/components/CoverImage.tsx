"use client";

import { useState } from "react";

interface CoverImageProps {
  src: string;
  alt: string;
  className?: string;
}

export default function CoverImage({ src, alt, className }: CoverImageProps) {
  const [failed, setFailed] = useState(false);

  if (failed) {
    return (
      <div
        className={`flex items-center justify-center bg-gray-100 text-gray-400 text-xs text-center p-2 ${className ?? ""}`}
      >
        <span>{alt}</span>
      </div>
    );
  }

  return (
    <img
      src={src}
      alt={alt}
      className={className}
      onError={() => setFailed(true)}
    />
  );
}
