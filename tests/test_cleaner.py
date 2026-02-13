"""Tests for text cleaner."""

import pytest
from text_humanizer.cleaner import TextCleaner


def test_cleaner_basic():
    """Test basic Markdown removal."""
    cleaner = TextCleaner()

    text = "# Heading\n\nThis is **bold** and *italic* text."
    cleaned = cleaner.clean(text)

    assert "Heading" in cleaned
    assert "bold" in cleaned
    assert "italic" in cleaned
    assert "#" not in cleaned
    assert "**" not in cleaned
    assert "*" not in cleaned


def test_cleaner_links():
    """Test link removal."""
    cleaner = TextCleaner()

    text = "Check out [this link](https://example.com) for more info."
    cleaned = cleaner.clean(text)

    assert "this link" in cleaned
    assert "https://example.com" not in cleaned
    assert "[" not in cleaned
    assert "]" not in cleaned


def test_cleaner_code_blocks():
    """Test code block removal."""
    cleaner = TextCleaner()

    text = """
    Here is some text.

    ```python
    def hello():
        print("world")
    ```

    More text here.
    """
    cleaned = cleaner.clean(text)

    assert "Here is some text" in cleaned
    assert "More text here" in cleaned
    assert "def hello" not in cleaned
    assert "```" not in cleaned


def test_cleaner_inline_code():
    """Test inline code removal."""
    cleaner = TextCleaner()

    text = "Use the `check-human` command to analyze text."
    cleaned = cleaner.clean(text)

    assert "Use the" in cleaned
    assert "command to analyze text" in cleaned
    assert "`" not in cleaned


def test_cleaner_lists():
    """Test list marker removal."""
    cleaner = TextCleaner()

    text = """
    - Item one
    - Item two
    * Item three
    + Item four
    1. Numbered item
    2. Another numbered item
    """
    cleaned = cleaner.clean(text)

    assert "Item one" in cleaned
    assert "Item two" in cleaned
    assert "Numbered item" in cleaned
    assert "-" not in cleaned.replace("Item", "")
    assert "*" not in cleaned
    assert "1." not in cleaned


def test_cleaner_blockquotes():
    """Test blockquote removal."""
    cleaner = TextCleaner()

    text = "> This is a quote\n> Another line"
    cleaned = cleaner.clean(text)

    assert "This is a quote" in cleaned
    assert "Another line" in cleaned
    assert ">" not in cleaned


def test_cleaner_images():
    """Test image removal."""
    cleaner = TextCleaner()

    text = "Here is an image: ![alt text](image.png) and more text."
    cleaned = cleaner.clean(text)

    assert "Here is an image" in cleaned
    assert "and more text" in cleaned
    assert "![" not in cleaned
    assert "image.png" not in cleaned


def test_cleaner_horizontal_rules():
    """Test horizontal rule removal."""
    cleaner = TextCleaner()

    text = "Section one\n\n---\n\nSection two"
    cleaned = cleaner.clean(text)

    assert "Section one" in cleaned
    assert "Section two" in cleaned
    assert "---" not in cleaned


def test_cleaner_tables():
    """Test table pipe removal."""
    cleaner = TextCleaner()

    text = "| Column 1 | Column 2 |\n|----------|----------|\n| Data 1   | Data 2   |"
    cleaned = cleaner.clean(text)

    assert "Column 1" in cleaned
    assert "Column 2" in cleaned
    assert "|" not in cleaned


def test_cleaner_whitespace_normalization():
    """Test excessive whitespace removal."""
    cleaner = TextCleaner()

    text = "Too    many     spaces.\n\n\n\nToo many newlines."
    cleaned = cleaner.clean(text)

    assert "Too many spaces" in cleaned
    assert "Too many newlines" in cleaned
    assert "    " not in cleaned
    assert "\n\n\n" not in cleaned


def test_cleaner_empty_text():
    """Test handling of empty text."""
    cleaner = TextCleaner()

    text = ""
    cleaned = cleaner.clean(text)

    assert cleaned == ""


def test_cleaner_complex_markdown():
    """Test complex Markdown document."""
    cleaner = TextCleaner()

    text = """
    # Main Title

    This is a paragraph with **bold**, *italic*, and `code`.

    ## Subsection

    - List item one
    - List item two

    > A blockquote with [a link](https://example.com)

    ```python
    # This code should be removed
    print("hello")
    ```

    Final paragraph.
    """
    cleaned = cleaner.clean(text)

    assert "Main Title" in cleaned
    assert "paragraph with bold, italic, and code" in cleaned
    assert "Subsection" in cleaned
    assert "List item one" in cleaned
    assert "blockquote with a link" in cleaned
    assert "Final paragraph" in cleaned
    assert "#" not in cleaned
    assert "**" not in cleaned
    assert "`" not in cleaned
    assert "print" not in cleaned
