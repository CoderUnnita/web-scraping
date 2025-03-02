import os

# Run all scripts sequentially
os.system("python scripts/scrape_bbc.py")
os.system("python scripts/analyze_data.py")
os.system("python scripts/sentiment_analysis.py")

print("✅ Project completed successfully!")