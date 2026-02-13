"""Text analysis using textstat library."""

from typing import Dict, List, Tuple
import re
import textstat


class TextAnalyzer:
    """Analyze text readability and detect AI-generated patterns."""

    AI_SHAME_WORDS = [
        "delve",
        "testament",
        "tapestry",
        "landscape",
        "foster",
        "robust",
        "leverage",
        "paradigm",
        "synergy",
        "holistic",
    ]

    def __init__(self):
        self.ai_words = self.AI_SHAME_WORDS

    def analyze(self, text: str) -> Dict:
        """
        Analyze text and return comprehensive metrics.

        Args:
            text: Clean text to analyze

        Returns:
            Dictionary containing all analysis results
        """
        flesch_score = textstat.flesch_reading_ease(text)

        sentences = textstat.sentence_count(text)
        words = textstat.lexicon_count(text, removepunct=True)
        avg_sentence_length = words / sentences if sentences > 0 else 0

        humanity_score = self._calculate_humanity_score(
            flesch_score, avg_sentence_length
        )

        ai_words_found = self._detect_ai_words(text)

        status = self._get_status(humanity_score)

        return {
            "humanity_score": humanity_score,
            "flesch_score": flesch_score,
            "avg_sentence_length": avg_sentence_length,
            "total_sentences": sentences,
            "total_words": words,
            "ai_words": ai_words_found,
            "status": status,
        }

    def _calculate_humanity_score(
        self, flesch_score: float, avg_sentence_length: float
    ) -> int:
        """
        Calculate humanity score based on readability metrics.

        Args:
            flesch_score: Flesch Reading Ease score
            avg_sentence_length: Average words per sentence

        Returns:
            Humanity score from 0-100
        """
        base_score = flesch_score

        if avg_sentence_length > 25:
            penalty = (avg_sentence_length - 25) * 2
            base_score -= penalty

        score = max(0, min(100, base_score))

        return int(score)

    def _detect_ai_words(self, text: str) -> List[Tuple[str, List[int]]]:
        """
        Detect AI shame words in text.

        Args:
            text: Text to analyze

        Returns:
            List of tuples (word, [line_numbers])
        """
        found_words = []
        lines = text.split('\n')

        for word in self.ai_words:
            pattern = r'\b' + re.escape(word) + r'\b'
            line_numbers = []

            for i, line in enumerate(lines, 1):
                if re.search(pattern, line, re.IGNORECASE):
                    line_numbers.append(i)

            if line_numbers:
                found_words.append((word, line_numbers))

        return found_words

    def _get_status(self, humanity_score: int) -> Dict[str, str]:
        """
        Get status message based on humanity score.

        Args:
            humanity_score: Score from 0-100

        Returns:
            Dictionary with status emoji and message
        """
        if humanity_score >= 60:
            return {
                "emoji": "✅",
                "message": "Human Approved!",
                "color": "green",
            }
        elif humanity_score >= 30:
            return {
                "emoji": "⚠️",
                "message": "Needs Work",
                "color": "yellow",
            }
        else:
            return {
                "emoji": "🤖",
                "message": "Robot Detected!",
                "color": "red",
            }

    def get_flesch_interpretation(self, score: float) -> str:
        """
        Get human-readable interpretation of Flesch score.

        Args:
            score: Flesch Reading Ease score

        Returns:
            Interpretation string
        """
        if score >= 90:
            return "Very Easy"
        elif score >= 80:
            return "Easy"
        elif score >= 70:
            return "Fairly Easy"
        elif score >= 60:
            return "Standard"
        elif score >= 50:
            return "Fairly Difficult"
        elif score >= 30:
            return "Difficult"
        else:
            return "Very Difficult"
