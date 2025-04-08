def test_remove_special_chars():
    from src.preprocess import clean_text
    assert clean_text("Hello!!") == "Hello"
