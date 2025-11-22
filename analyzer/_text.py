from typing import Any, Dict, List
from textblob import TextBlob


def analyze_text(text: str) -> Dict[str, Any]:
    """Analyze text and return simple primitive results.

    Returns:
        Dict with keys: 'sentiment' ({'polarity','subjectivity'}), 'word_count', 'key_words'
    """

    blob = TextBlob(text or "")
    polarity = float(blob.sentiment.polarity)
    subjectivity = float(blob.sentiment.subjectivity)
    word_count = len(text.split()) if text else 0
    key_words: List[str] = list(blob.noun_phrases)

    return {
        "sentiment": {"polarity": polarity, "subjectivity": subjectivity},
        "word_count": word_count,
        "key_words": key_words,
    }
