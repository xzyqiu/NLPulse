from typing import Any, Dict, List
from textblob import TextBlob


def analyze_text(text: str) -> Dict[str, Any]:
    """Analyze text and return sentiment, word count, and keywords.

    Returns a dictionary with the following keys:
    - 'sentiment': {'polarity': float, 'subjectivity': float}
    - 'word_count': int
    - 'key_words': List[str]
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
from typing import Any, Dict, List
from textblob import TextBlob

def analyze_text(text: str) -> Dict[str, Any]:
    """Analyze text and return sentiment, word count, and keywords.

    Returns a dictionary with the following keys:
    - 'sentiment': {'polarity': float, 'subjectivity': float}
    - 'word_count': int
    - 'key_words': List[str]

    The function keeps the implementation small and deterministic so it is easy
    to test and review for a portfolio project.
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