**THIS PROJECT CANNOT BE RAN DIRECTLY ON ED WORKSPACE**

Sentiment Analysis on Twitter and Reddit Data Towards Climate Change.

Instructions on how to run this project:

STEP 1: Clone our git repo!
https://github.com/SirBlank/Spring-2023-CSE-163-Project.git


-------------------------------------------------------------


STEP 2: Install packages

1. Ensure that you have the following packages installed on your system:
- pandas
- geopandas
- numpy
- math
- string
- matplotlib
- nltk
- sklearn
- scipy
- typing

2. If not, run the following pip commands on command line
pip install pandas
pip install geopandas
pip install numpy
pip install math (maybe)
pip install string (maybe)
pip install matplotlib
pip install nltk
pip install scikit-learn
pip install scipy
pip install typing


-------------------------------------------------------------


STEP 3: Download datasets

1. Twitter sentiment dataset

(Recommended)
Clone our github repo, the Twitter sentiment dataset is already there:
https://github.com/SirBlank/Spring-2023-CSE-163-Project.git

-OR-

Obtain Twitter sentiment dataset by downloading it from this website:
https://www.kaggle.com/datasets/edqian/twitter-climate-change-sentiment-dataset?resource=download

2. Harvard sentiment datasets

(Recommended)
Clone our github repo, the Harvard sentiment datasets from 2012-2022 is already there:
https://github.com/SirBlank/Spring-2023-CSE-163-Project.git

-OR-

(Not Recommended)
Go to this website and download all the 'Sentiment Data - State/' csv files from 2012-2022:
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2F3IL00Q&version=&q=&fileTypeGroupFacet=%22Data%22&fileAccess=&fileTag=&fileSortField=&fileSortOrder=


-------------------------------------------------------------


STEP 4: Run our codes!

PART 1: Geographic maps of sentiment values (RQ1)

1. Unzip all 'num_posts_and_sentiment_summary_XXXX.csv.zip' files into the same folder as the git repo.
Your repo folder should look something like this:

num_posts_and_sentiment_summary_2012.csv
num_posts_and_sentiment_summary_2012.csv.zip
num_posts_and_sentiment_summary_2013.csv
num_posts_and_sentiment_summary_2013.csv.zip
...

2. Run 'harvard_map.py' in your terminal!
NOTE: this might take more than 10 minutes to run. Please be patient!

PART 2: Time series graphs of sentiment values (RQ2)

1. This one is simple! Run 'graphs.py' in your terminal!

PART 3: Predictive Sentiment models (RQ3)

1. Open the repo folder in an IDE and run 'sentiment_analysis.ipynb'.
This notebook will be using 'filtered_twitter_data(10,000).csv' (this is already created for you in the repo)
since it would take a really long time to compile the original dataset.

You can also find the code that created 'filtered_twitter_data(10,000).csv'
in the repo as well. The script is called filter_twitter_data.py.
The notebook should run successfully if all listed packages are downloaded!
(NOTE: might take a few minutes to compile the entire notebok)
