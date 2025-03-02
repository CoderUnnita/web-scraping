import requests
from bs4 import BeautifulSoup
import pandas as pd

# BBC News URL
URL = "https://www.bbc.com/news"

# Function to scrape BBC news headlines
def scrape_bbc_news():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Failed to fetch BBC News")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h3')  # BBC headlines are inside <h3> tags

    news_list = []
    for headline in headlines:
        title = headline.get_text(strip=True)
        if title:  # Ignore empty headlines
            news_list.append(title)

    # Save data to CSV
    df = pd.DataFrame(news_list, columns=["Headline"])
    df.to_csv("data/bbc_news.csv", index=False)
    print("✅ Scraped and saved BBC News headlines!")

# Run scraper
scrape_bbc_news()
