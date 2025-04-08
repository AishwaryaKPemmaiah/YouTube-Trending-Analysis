def test_sentiment_score_range():
    score = analyze_sentiment("I love it!")
    assert 0 <= score <= 1
