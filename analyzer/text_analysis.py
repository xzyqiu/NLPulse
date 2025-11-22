from textblob import TextBlob

def analyze_text(text):
    sentiment = TextBlob(text).sentiment
    word_count = len(text.split())
    key_words = TextBlob(text).noun_phrases
    dictionary = {
        'sentiment': sentiment,
        'word_count': word_count,
        'key_words': key_words
    }
    return dictionary