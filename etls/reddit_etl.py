from praw import Reddit
import pandas as pd
import sys

def connect_reddit(client_id,client_secret,user_agent) ->  Reddit:
    import praw
    try:
        reddit = praw.Reddit(client_id=client_id,
                            client_secret=client_secret,
                            user_agent=user_agent)
        print("Connected to Reddit API successfully!")
        return reddit
    except Exception as e:
        print(f"Error connecting to Reddit API: {str(e)}")
        sys.exit(1)


def extract_posts(reddit_instance: Reddit, subreddit:str, limit=None, time_filter=str):
    try:
        posts = reddit_instance.subreddit(subreddit)
        if time_filter == 'day':
            posts = posts.top(time_filter, limit=limit)
        else:
            posts = posts.top(time_filter)
        post_list = []
        for post in posts:
            post_list.append({
                'id': post.id,
                'title': post.title,
                'score': post.score,
                'num_comments': post.num_comments,
                'author': post.author,
                'url': post.url,
                'upvote_ratio': post.upvote_ratio,
                'over_18': post.over_18,
                'spoiler': post.spoiler,
                'created': post.created,
                'body': post.selftext
            })
        return post_list
    except Exception as e:
        print(f"Error extracting posts from Reddit: {str(e)}")
        sys.exit(1)

def transform_data(df):
    df['created'] = pd.to_datetime(df['created'],unit='s')
    df['author'] = [str(author) for author in df['author']]
    df['over_18'] = [True if over_18 else False for over_18 in df['over_18']]
    df['num_comments'] = df['num_comments'].astype(int)
    df['score'] = df['score'].astype(int)
    df['upvote_ratio'] = df['upvote_ratio'].astype(float)
    df['title'] = df['title'].astype(str)

    return df

def load_data_to_csv(df, path:str):
    df.to_csv(path, index=False)
    print(f"Data saved to {path}")