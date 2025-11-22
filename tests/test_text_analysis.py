from analyzer._text import analyze_text


def test_analyze_text_basic():
    res = analyze_text("This is excellent and clear.")
    assert "sentiment" in res
    assert isinstance(res["sentiment"]["polarity"], float)
    assert isinstance(res["sentiment"]["subjectivity"], float)
    assert isinstance(res["word_count"], int)
    assert isinstance(res["key_words"], list)
