"""
This file plots time series graphs of the average sentiment score and
the number of posts every year using datasets from 2012-2022. Includes
tests of each function
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


def merge_files(files: list[str]) -> None:
    '''
    Merges multiple datasets together with the given files
    '''
    df = pd.DataFrame()
    for file in files:
        data = pd.read_csv(file)
        df = pd.concat([df, data], axis=0)
    df.to_csv('merged_files.csv', index=False)


def processing() -> pd.Series:
    '''
    Reads the merged data from the CSV file, converts date column to
    datetime format, and calculates mean sentiment score and mean number
    of posts for each date. Returns yearly score data and yearly posts data
    '''
    merged_data = pd.read_csv('merged_files.csv')
    # Convert 'DATE' column to datetime
    merged_data["DATE"] = pd.to_datetime(merged_data["DATE"])
    # Group the data by year and calculate the mean sentiment score
    yearly_score_data = merged_data.groupby('DATE')['SCORE'].mean()
    # Group the data by year and calculate the mean posts
    yearly_posts_data = merged_data.groupby('DATE')['N'].mean()
    return yearly_score_data, yearly_posts_data


def plot_sentiment_scores(yearly_score_data: pd.Series) -> None:
    '''
    Generates a line plot to visualize the time series of sentiment scores,
    returns None
    '''
    # Plot the time series
    plt.plot(yearly_score_data.index, yearly_score_data.values)
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Score')

    plt.savefig('sentiment_scores.png', bbox_inches='tight')


def plot_posts(yearly_posts_data: pd.Series) -> None:
    '''
    Generates a line plot to visualize the time series of number of posts,
    returns None
    '''
    # Plot the time series
    plt.plot(yearly_posts_data.index, yearly_posts_data.values)
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Posts')
    plt.title('Daily Number of Post')

    plt.savefig('posts.png', bbox_inches='tight')


def test_merge_files() -> None:
    '''
    Tests the function merge_files, returns None
    '''
    files = ['num_posts_and_sentiment_summary_2012.csv',
             'num_posts_and_sentiment_summary_2013.csv',
             'num_posts_and_sentiment_summary_2014.csv']
    merge_files(files)
    assert os.path.exists('merged_files.csv')


def test_processing() -> None:
    '''
    Tests the function processing, returns None
    '''
    merge_files(['num_posts_and_sentiment_summary_2012.csv'])
    yearly_score_data, yearly_posts_data = processing()
    assert isinstance(yearly_score_data, pd.Series)
    assert isinstance(yearly_posts_data, pd.Series)


def test_plot_sentiment_scores() -> None:
    '''
    Tests the function sentiment_scores, returns None
    '''
    merge_files(['num_posts_and_sentiment_summary_2012.csv'])
    yearly_score_data = processing()
    plot_sentiment_scores(yearly_score_data)
    assert os.path.exists('sentiment_scores.png')


def test_plot_posts() -> None:
    '''
    Tests the function plot_posts, returns None
    '''
    merge_files(['num_posts_and_sentiment_summary_2012.csv'])
    yearly_posts_data = processing()
    plot_posts(yearly_posts_data)
    assert os.path.exists('posts.png')


def run_tests() -> None:
    '''
    Runs tests on all test functions
    '''
    test_merge_files()
    test_processing()
    test_plot_sentiment_scores()
    test_plot_posts()
    print("All tests passed!")


def main():
    files = ['num_posts_and_sentiment_summary_2012.csv',
             'num_posts_and_sentiment_summary_2013.csv',
             'num_posts_and_sentiment_summary_2014.csv',
             'num_posts_and_sentiment_summary_2015.csv',
             'num_posts_and_sentiment_summary_2016.csv',
             'num_posts_and_sentiment_summary_2017.csv',
             'num_posts_and_sentiment_summary_2018.csv',
             'num_posts_and_sentiment_summary_2019.csv',
             'num_posts_and_sentiment_summary_2020.csv',
             'num_posts_and_sentiment_summary_2021.csv',
             'num_posts_and_sentiment_summary_2022.csv']
    merge_files(files)
    yearly_score_data, yearly_posts_data = processing()
    plot_sentiment_scores(yearly_score_data)
    plot_posts(yearly_posts_data)
    run_tests()


if __name__ == "__main__":
    main()
