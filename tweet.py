import tweepy
import complete
import os
from dotenv import load_dotenv

load_dotenv()
def makeTweet(override = ""):
    client = tweepy.Client(
        bearer_token=os.getenv('BEARER_TOKEN'),
        consumer_key=os.getenv('CONSUMER_KEY'),
        consumer_secret=os.getenv('CONSUMER_SECRET'),
        access_token=os.getenv('ACC_ACCESS_TOKEN'),
        access_token_secret=os.getenv('ACC_ACCESS_TOKEN_SECRET')
    )
    if(override == ""):
        tweet = complete.generate()
        if(len(tweet) > 280):
            tweet = tweet[:280]
        client.create_tweet(text=tweet)
    else:
        client.create_tweet(text=override)
makeTweet()