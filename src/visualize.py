import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set Seaborn style
sns.set(style="ticks")

# Load USvideos.csv
DATA_PATH = os.path.join("data", "archive", "USvideos.csv")
df = pd.read_csv(DATA_PATH)

# Helper to show plots nicely
def show_plot(title):
    plt.title(title, fontsize=14)
    plt.xlabel("")
    plt.tight_layout()
    plt.show()

# 1. Top 10 video categories by count
def plot_top_categories(df):
    top_categories = df['category_id'].value_counts().head(10)
    sns.barplot(x=top_categories.values, y=top_categories.index, palette="viridis")
    show_plot("Top 10 Video Categories by Frequency")

# 2. Views vs. Likes
def plot_views_vs_likes(df):
    sns.scatterplot(x='likes', y='views', data=df, alpha=0.5, color = "orange")
    plt.xscale('log')
    plt.yscale('log')
    show_plot("Views vs Likes (Log Scale)")

# 3. Video uploads by hour
def plot_upload_hour(df):
    df['trending_date'] = pd.to_datetime(df['trending_date'], errors='coerce', format='%y.%d.%m')
    df['upload_hour'] = pd.to_datetime(df['publish_time']).dt.hour
    sns.histplot(df['upload_hour'], bins=24, kde=True, color="skyblue")
    show_plot("Video Uploads by Hour of Day")

# Run all plots
if __name__ == "__main__":
    print("Generating visualizations...")
    plot_top_categories(df)
    plot_views_vs_likes(df)
    plot_upload_hour(df)
    print("✅ Visualizations done!")
