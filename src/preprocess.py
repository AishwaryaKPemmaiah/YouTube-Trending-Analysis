import pandas as pd
import re

def clean_text(text):
    """Remove unwanted characters, emojis, links, and punctuation."""
    if pd.isnull(text):
        return ""
    
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = re.sub(r"[^A-Za-z0-9\s]+", "", text)  # remove special characters and emojis
    text = text.lower().strip()  # lowercase and trim
    return text

def preprocess_data(df):
    """Clean and preprocess the loaded YouTube trending video data."""

    print("🔧 Starting preprocessing...")

    # 1. Drop duplicates
    before = df.shape[0]
    df = df.drop_duplicates()
    print(f"🗑️ Dropped {before - df.shape[0]} duplicate rows")


    # 2. Drop completely empty rows
    df = df.dropna(how='all')

    # 3. Backup original text fields before cleaning
    for col in ['title', 'description', 'tags']:
        if col in df.columns:
            df[f'raw_{col}'] = df[col]

    # 4. Clean text fields
    text_fields = ['title', 'description', 'tags']
    for col in text_fields:
        if col in df.columns:
            df[col] = df[col].fillna("").apply(clean_text)

    # 5. Convert 'publish_time' to datetime
    if 'publish_time' in df.columns:
        df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

    # 6. Standardize column names to snake_case
    df.columns = [col.strip().lower(    ).replace(" ", "_") for col in df.columns]

    print("✅ Preprocessing complete.")
    return df




# For standalone testing
if __name__ == "__main__":
    from data_loader import load_data

    file_path = "data/archive/USvideos.csv"
    df = load_data(file_path)

    if df is not None:
        clean_df = preprocess_data(df)
        print(clean_df.head())










