import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

# Load sentiment data
df = pd.read_csv("data/sentiment_bbc_news.csv")

# 📌 **1️⃣ Visualize Word Frequency**
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(df["Cleaned_Headline"]))
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("BBC News Word Cloud")
plt.show()

# 📌 **2️⃣ Visualize Sentiment Distribution**
plt.figure(figsize=(6,4))
sns.countplot(x=df["Sentiment"], palette={"Positive": "green", "Negative": "red", "Neutral": "gray"})
plt.title("Sentiment Analysis of BBC News")
plt.show()
