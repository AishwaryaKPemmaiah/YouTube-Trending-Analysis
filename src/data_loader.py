'''import json
import pandas as pd

# Load the JSON file
with open("data/CA_category_id.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract categories
categories = data["items"]

# Process data into a list of dictionaries
category_list = []
for category in categories:
    category_list.append({
        "category_id": category["id"],
        "title": category["snippet"]["title"]
    })

# Convert to DataFrame
df = pd.DataFrame(category_list)

# Save as CSV
df.to_csv("data/video_categories.csv", index=False)

print("✅ YouTube categories saved to 'data/video_categories.csv'")


'''



import pandas as pd
import os

def load_data(file_path):
    """Load YouTube trending videos CSV file into a Pandas DataFrame."""
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' not found!")
        return None

    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Display basic info
        print(f"✅ Successfully loaded {file_path}")
        print(f"📊 Dataset Shape: {df.shape}")
        print(f"📝 Columns: {list(df.columns)}\n")
        print(f"Info: {df.info}\n")
        print(f"Count missing values {df.isnull().sum()}")  # Count missing values per column
        print(f"Describe: {df.describe()}\n")

        print(f"📊 Dataset Shape: {df.shape[0], {df.shape[1]}}")
        print(f"📝 Columns: {list(df.columns)}\n")
        print(f"DataTypes: {df.dtypes}")
        print(f"Duplicates: {df.duplicated().sum()}")
        #d removes duplicates df = df.drop_duplicates()


        for col in df.columns:
            print(f"{col} : {df[col].nunique()} Unique values")      
            
            return df
        
    except Exception as e:
        print(f"⚠️ Error reading {file_path}: {e}")
        return None

# Usage example
if __name__ == "__main__":
    file_path = "data/archive/USvideos.csv"  # Change this path if needed
    df = load_data(file_path)

    if df is not None:
        print(df.tail())  # Print first few rows

