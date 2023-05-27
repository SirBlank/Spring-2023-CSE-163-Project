import pandas as pd
import matplotlib.pyplot as plt

files = ['/Users/slin7/Downloads/sentiment/graphs/num_posts_and_sentiment_summary_2012.csv',
         '/Users/slin7/Downloads/sentiment/graphs/num_posts_and_sentiment_summary_2013.csv',
         '/Users/slin7/Downloads/sentiment/graphs/num_posts_and_sentiment_summary_2014.csv',
         '/Users/slin7/Downloads/sentiment/graphs/num_posts_and_sentiment_summary_2015.csv',
         '/Users/slin7/Downloads/sentiment/graphs/num_posts_and_sentiment_summary_2016.csv',
         '/Users/slin7/Downloads/sentiment/graphs/num_posts_and_sentiment_summary_2017.csv',
         '/Users/slin7/Downloads/sentiment/graphs/num_posts_and_sentiment_summary_2018.csv',
         '/Users/slin7/Downloads/sentiment/graphs/num_posts_and_sentiment_summary_2019.csv',
         '/Users/slin7/Downloads/sentiment/graphs/num_posts_and_sentiment_summary_2020.csv',
         '/Users/slin7/Downloads/sentiment/graphs/num_posts_and_sentiment_summary_2021.csv',
         '/Users/slin7/Downloads/sentiment/graphs/num_posts_and_sentiment_summary_2022.csv']

df = pd.DataFrame()

# merging all the files together
for file in files:
    data = pd.read_csv(file)
    df = pd.concat([df, data], axis=0)
df.to_csv('merged_files.csv', index=False)
merged_data = pd.read_csv('merged_files.csv')

# Convert 'DATE' column to datetime
merged_data["DATE"] = pd.to_datetime(merged_data["DATE"])
# merged_data["YEAR"] = merged_data["DATE"].dt.year

# Group the data by year and calculate the mean sentiment score
yearly_score_data = merged_data.groupby('DATE')['SCORE'].mean()

# Plot the time series
plt.plot(yearly_score_data.index, yearly_score_data.values)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Score')

plt.savefig('sentiment_scores.png', bbox_inches='tight')

# Group the data by year and calculate the mean posts
yearly_posts_data = merged_data.groupby('DATE')['N'].mean()

# Plot the time series
plt.plot(yearly_posts_data.index, yearly_posts_data.values)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Posts')
plt.title('Daily Number of Post')

plt.savefig('posts.png', bbox_inches='tight')
