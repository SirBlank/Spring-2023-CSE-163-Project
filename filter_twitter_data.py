"""
This script filters Twitter dataset to 10,000 rows.
"""


import pandas as pd

# Read the CSV file using pandas
df = pd.read_csv("twitter_sentiment_data.csv")
filtered_twitter = df.sample(n=10000, random_state=42)
filtered_twitter.to_csv("filtered_twitter_data(10,000).csv", index=False)