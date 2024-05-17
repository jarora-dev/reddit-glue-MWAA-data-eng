from etls.reddit_etl import connect_reddit
from etls.reddit_etl import extract_posts
from utils.constants import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET
from etls.reddit_etl import transform_data
from etls.reddit_etl import load_data_to_csv
from utils.constants import OUTPUT_PATH

import pandas as pd

def extract_reddit_pipeline(file_name:str, subreddit:str, limit=None, time_filter='day'):

    #connectivity to reddit
    instance = connect_reddit(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, 'Airscholar Agent')

    #extract data from reddit
    posts = extract_posts(instance, subreddit, limit, time_filter)
    post_df = pd.DataFrame(posts)
    post_df = transform_data(post_df)

    #transform data
    file_path = f"{OUTPUT_PATH}/{file_name}.csv"
    load_data_to_csv(post_df, file_path)

    return file_path




