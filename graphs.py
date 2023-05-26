import pandas as pd
import plotly.express as px
import plotly.io as pio

files = ['num_posts_and_sentiment_summary_2012.csv', 'num_posts_and_sentiment_summary_2013.csv', 'num_posts_and_sentiment_summary_2014.csv', 
         'num_posts_and_sentiment_summary_2015.csv', 'num_posts_and_sentiment_summary_2016.csv', 'num_posts_and_sentiment_summary_2017.csv', 
         'num_posts_and_sentiment_summary_2018.csv', 'num_posts_and_sentiment_summary_2019.csv', 'num_posts_and_sentiment_summary_2020.csv', 
         'num_posts_and_sentiment_summary_2021.csv', 'num_posts_and_sentiment_summary_2022.csv']
df = pd.DataFrame()
for file in files:
    data = pd.read_csv(file)
    df = pd.concat([df, data], axis=0)
df.to_csv('merged_files.csv', index=False)
merged_data = pd.read_csv('merged_files.csv')

# interactive line plot
fig = px.line(merged_data, x='DATE', y='SCORE', title='Sentiment Score')

fig.update_layout(xaxis_title='Year', yaxis_title='Sentiment Score')

pio.write_image(fig, 'sentiment_score.png')
