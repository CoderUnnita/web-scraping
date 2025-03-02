import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download sentiment model
nltk.download('vader_lexicon')

# Load cleaned data
df = pd.read_csv("data/cleaned_bbc_news.csv")

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def get_sentiment(text):
    score = sia.polarity_scores(text)["compound"]
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Cleaned_Headline"].apply(get_sentiment)

# Save sentiment results
df.to_csv("data/sentiment_bbc_news.csv", index=False)
print("✅ Sentiment analysis completed!")
