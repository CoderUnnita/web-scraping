import pandas as pd

import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download NLP resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load scraped data
df = pd.read_csv("data/bbc_news.csv")

# Initialize NLP tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# Function to clean headlines
def clean_text(text):
    tokens = word_tokenize(text.lower())  # Convert to lowercase & tokenize
    tokens = [word for word in tokens if word.isalpha()]  # Remove punctuation/numbers
    tokens = [word for word in tokens if word not in stop_words]  # Remove stopwords
    tokens = [lemmatizer.lemmatize(word) for word in tokens]  # Lemmatization
    return " ".join(tokens)

# Apply cleaning function to each headline
df["Cleaned_Headline"] = df["Headline"].apply(clean_text)

# Save cleaned data
df.to_csv("data/cleaned_bbc_news.csv", index=False)
print("✅ Cleaned text data and saved!")
