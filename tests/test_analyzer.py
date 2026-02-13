"""Tests for text analyzer."""

import pytest
from text_humanizer.analyzer import TextAnalyzer


def test_analyzer_basic():
    """Test basic analysis functionality."""
    analyzer = TextAnalyzer()

    text = "This is a simple sentence. It is easy to read. Short and clear."
    results = analyzer.analyze(text)

    assert "humanity_score" in results
    assert "flesch_score" in results
    assert "avg_sentence_length" in results
    assert 0 <= results["humanity_score"] <= 100


def test_analyzer_complex_text():
    """Test analysis of complex academic text."""
    analyzer = TextAnalyzer()

    text = """
    The implementation of sophisticated algorithmic paradigms necessitates
    a comprehensive understanding of the underlying computational complexities
    inherent in distributed systems architecture.
    """
    results = analyzer.analyze(text)

    assert results["humanity_score"] < 50


def test_analyzer_simple_text():
    """Test analysis of simple conversational text."""
    analyzer = TextAnalyzer()

    text = """
    I love this tool. It helps me write better.
    My readers enjoy clear text. Short sentences work best.
    """
    results = analyzer.analyze(text)

    assert results["humanity_score"] > 60


def test_ai_word_detection():
    """Test detection of AI shame words."""
    analyzer = TextAnalyzer()

    text = "Let's delve into this topic. The landscape is changing."
    results = analyzer.analyze(text)

    assert len(results["ai_words"]) == 2
    assert any(word == "delve" for word, _ in results["ai_words"])
    assert any(word == "landscape" for word, _ in results["ai_words"])


def test_empty_text():
    """Test handling of empty text."""
    analyzer = TextAnalyzer()

    text = ""
    results = analyzer.analyze(text)

    assert results["total_sentences"] == 0
    assert results["total_words"] == 0


def test_sentence_length_penalty():
    """Test that long sentences reduce humanity score."""
    analyzer = TextAnalyzer()

    short_text = "Short sentence. Another one. And one more."
    long_text = "This is an extremely long sentence that contains many words and clauses and continues on and on without any breaks or pauses which makes it very difficult to read and understand for most people."

    short_results = analyzer.analyze(short_text)
    long_results = analyzer.analyze(long_text)

    assert short_results["humanity_score"] > long_results["humanity_score"]


def test_flesch_interpretation():
    """Test Flesch score interpretation."""
    analyzer = TextAnalyzer()

    assert analyzer.get_flesch_interpretation(95) == "Very Easy"
    assert analyzer.get_flesch_interpretation(75) == "Fairly Easy"
    assert analyzer.get_flesch_interpretation(55) == "Fairly Difficult"
    assert analyzer.get_flesch_interpretation(25) == "Very Difficult"


def test_status_messages():
    """Test status message generation."""
    analyzer = TextAnalyzer()

    high_score_status = analyzer._get_status(80)
    assert high_score_status["emoji"] == "✅"
    assert high_score_status["color"] == "green"

    mid_score_status = analyzer._get_status(45)
    assert mid_score_status["emoji"] == "⚠️"
    assert mid_score_status["color"] == "yellow"

    low_score_status = analyzer._get_status(20)
    assert low_score_status["emoji"] == "🤖"
    assert low_score_status["color"] == "red"
