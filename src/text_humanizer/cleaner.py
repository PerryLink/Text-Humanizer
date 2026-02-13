"""Text cleaning utilities to remove Markdown and other formatting."""

import re


class TextCleaner:
    """Clean text by removing Markdown syntax and other formatting."""

    def __init__(self):
        self.patterns = [
            (r'```[\s\S]*?```', ''),
            (r'`([^`]*)`', r'\1'),
            (r'#{1,6}\s+', ''),
            (r'\*\*([^\*]+)\*\*', r'\1'),
            (r'\*([^\*]+)\*', r'\1'),
            (r'__([^_]+)__', r'\1'),
            (r'_([^_]+)_', r'\1'),
            (r'\[([^\]]+)\]\([^\)]+\)', r'\1'),
            (r'!\[([^\]]*)\]\([^\)]+\)', ''),
            (r'^>\s+', '', re.MULTILINE),
            (r'^\s*[-*+]\s+', '', re.MULTILINE),
            (r'^\s*\d+\.\s+', '', re.MULTILINE),
            (r'---+', ''),
            (r'\|', ''),
        ]

    def clean(self, text: str) -> str:
        """
        Remove Markdown syntax and return clean text.

        Args:
            text: Raw text with potential Markdown formatting

        Returns:
            Cleaned text with Markdown removed
        """
        cleaned = text

        for pattern, replacement, *flags in self.patterns:
            flag = flags[0] if flags else 0
            cleaned = re.sub(pattern, replacement, cleaned, flags=flag)

        cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
        cleaned = re.sub(r' {2,}', ' ', cleaned)

        return cleaned.strip()
