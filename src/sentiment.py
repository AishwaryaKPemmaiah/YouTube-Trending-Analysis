from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text using TextBlob.

    Returns:
        polarity (float): -1 (negative) to +1 (positive)
        subjectivity (float): 0 (objective) to 1 (subjective)
    """
    if not text or not isinstance(text, str):
        return 0.0, 0.0

    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity


def add_sentiment_columns(df):
    """
    Add sentiment analysis columns (polarity and subjectivity) 
    for title and description in the DataFrame.
    """
    print("🔍 Performing sentiment analysis...")

    # Analyze sentiment for titles
    df['title_polarity'], df['title_subjectivity'] = zip(*df['title'].apply(analyze_sentiment))

    # Analyze sentiment for descriptions
    if 'description' in df.columns:
        df['desc_polarity'], df['desc_subjectivity'] = zip(*df['description'].apply(analyze_sentiment))

    print("✅ Sentiment analysis complete.")
    return df


# Example usage
if __name__ == "__main__":
    from data_loader import load_data
    from preprocess import preprocess_data

    file_path = "data/archive/USvideos.csv"
    df = load_data(file_path)

    if df is not None:
        df = preprocess_data(df)
        df = add_sentiment_columns(df)
        print(df[['title', 'title_polarity', 'title_subjectivity']].head())
