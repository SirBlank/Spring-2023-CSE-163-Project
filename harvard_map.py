"""
This file plots and saves color maps that track the sentiment score
and number of Twitter posts relating to climate change by country
using the datasets from Harvard Dataverse for years
2016, 2018, 2020, and 2022
"""

import os.path
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def test_sentiment_range_all(file_name: str) -> None:
    """
    Testing function to see if sentiment scores of all used harvard csv files
    are within the valid range
    :param file_name: the name of the harvard csv file, with 'XXXX'
    acting as a variable for the year
    :return:
    """
    test_sentiment_range(file_name.replace('XXXX', '2022'))
    test_sentiment_range(file_name.replace('XXXX', '2020'))
    test_sentiment_range(file_name.replace('XXXX', '2018'))
    test_sentiment_range(file_name.replace('XXXX', '2016'))


def test_sentiment_range(file_name: str) -> None:
    """
    Testing function to see if sentiment scores of a single harvard csv file
    are within the valid range
    :param file_name: the name of a single harvard csv file of a specific year
    """
    harvard_df = pd.read_csv(file_name)
    assert harvard_df['SCORE'].min() >= 0
    assert harvard_df['SCORE'].max() <= 1


def test_files_exist(harvard_file_name: str, countries_file_name: str) -> None:
    """
    Testing function to see if csv, shapely, and output png files exist
    :param harvard_file_name: the name of the harvard csv file, with 'XXXX'
    acting as a variable for the year
    :param countries_file_name: the name of the shapely geojson file
    """
    for i in range(2016, 2023, 2):
        assert os.path.exists(harvard_file_name.replace('XXXX', str(i)))
        assert os.path.exists(str(i) + '_number_map.png')
        assert os.path.exists(str(i) + '_sentiment_map.png')
        print(i)
    assert os.path.exists(countries_file_name)


def test_single_country(file_name: str, countries: gpd.GeoDataFrame,
                        year_str: str):
    """
    Testing function to see if color maps could be made using just a single
    country
    :param file_name: the name of the harvard csv file to which will be
    used to plot color maps
    :param countries: the GeoDataFrame that contains shapes
    to draw the world map
    :param year_str: the string containing the year of the harvard csv file
    :return:
    """
    harvard_df = pd.read_csv(file_name)
    harvard_df = harvard_df.replace('United States',
                                    'United States of America')
    harvard_df = harvard_df[harvard_df['NAME_0'] == 'United States of America']
    df = countries.merge(harvard_df, how="inner",
                         left_on='NAME_EN', right_on='NAME_0')
    df2 = df[['NAME_EN', 'geometry', 'N', 'SCORE']]
    df2 = df2.dissolve('NAME_EN', aggfunc='mean')

    df2.plot(column='N', legend=True)
    plt.title('Average Number of Climate Change\nTwitter Posts' +
              ' Per State/Province\nby Country in ' + year_str)
    plt.savefig(year_str + '_number_map_test.png')
    df2.plot(column='SCORE', legend=True)
    plt.title('Average Sentiment Score of Climate Change\nTwitter Posts'
              ' Per State/Province\nby Country in ' + year_str)
    plt.savefig(year_str + '_sentiment_map_test.png')
    assert os.path.exists(year_str + '_number_map_test.png')
    assert os.path.exists(year_str + '_sentiment_map_test.png')


def process_harvard(file_name: str, countries: gpd.GeoDataFrame,
                    year_str: str) -> None:
    """
    Plots and saves two types of color maps for the given dataset's year,
    one working with the number of Twitter posts and one working with the
    sentiment scores
    :param file_name: the name of the harvard csv file to which will be
    used to plot color maps
    :param countries: the GeoDataFrame that contains shapes
    to draw the world map
    :param year_str: the string containing the year of the harvard csv file
    """
    harvard_df = pd.read_csv(file_name)
    harvard_df = harvard_df.replace('United States',
                                    'United States of America')
    df = countries.merge(harvard_df, how="inner",
                         left_on='NAME_EN', right_on='NAME_0')
    df2 = df[['NAME_EN', 'geometry', 'N', 'SCORE']]
    df2 = df2.dissolve('NAME_EN', aggfunc='mean')

    df2.plot(column='N', legend=True)
    plt.title('Average Number of Climate Change\nTwitter Posts' +
              ' Per State/Province\nby Country in ' + year_str)
    plt.savefig(year_str + '_number_map.png')
    df2.plot(column='SCORE', legend=True)
    plt.title('Average Sentiment Score of Climate Change\nTwitter Posts'
              ' Per State/Province\nby Country in ' + year_str)
    plt.savefig(year_str + '_sentiment_map.png')


if __name__ == "__main__":
    harvard_file_name = "num_posts_and_sentiment_summary_XXXX.csv"
    countries_file_name = "countries.geojson"

    # plot and save the maps as png files for years
    # 2016, 2018, 2020, and 2022
    countries = gpd.read_file(countries_file_name)
    test_single_country(harvard_file_name.replace('XXXX', '2022'),
                        countries, '2022')
    process_harvard(harvard_file_name.replace('XXXX', '2022'),
                    countries, '2022')
    process_harvard(harvard_file_name.replace('XXXX', '2020'),
                    countries, '2020')
    process_harvard(harvard_file_name.replace('XXXX', '2018'),
                    countries, '2018')
    process_harvard(harvard_file_name.replace('XXXX', '2016'),
                    countries, '2016')

    # testing suite
    test_sentiment_range_all(harvard_file_name)
    test_files_exist(harvard_file_name, countries_file_name)
    test_single_country(harvard_file_name.replace('XXXX', '2022'),
                        countries, '2022')