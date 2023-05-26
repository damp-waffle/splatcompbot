import tweepy
import os
from dotenv import load_dotenv
import sys
import re

load_dotenv()
client = tweepy.Client(
    bearer_token=os.getenv('BEARER_TOKEN'),
    consumer_key=os.getenv('CONSUMER_KEY'),
    consumer_secret=os.getenv('CONSUMER_SECRET'),
    access_token=os.getenv('ACCESS_TOKEN'),
    access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')
)
def requestTweet(url):
    url = url.split('/')
    id = url[len(url) - 1]
    if('?' in id):
        id = id[:id.find('?')]
    x = client.get_tweet(id, expansions='author_id',media_fields='url',tweet_fields='created_at',user_fields='username')
    print(x)
    if(x.data == None):
        return ""
    y = str(x)
    y = y[(y.find("text=")+6):]
    text = y[:y.find(">,")-1]
    if(re.match("https\S+",text)):
        text = re.sub(r"http\S+", "", text)[:-1] #remove any media links
    y = y[(y.find("id=")+3):]
    author = y[:y.find(" ")]
    y = y[(y.find("username=")+9):]
    username = y[:y.find(">")]
    return {'id':id, 'text':text, 'author':author, 'username':username}
try:
    url = sys.argv[1]
except:
    print("Need tweet url or id")
else:
    response = requestTweet(url)
    if(response == ""):
        print("Could not find tweet at " + url)
    else:
        print("Success:" + str(response.values()))
        print("Tweet ID: " + response['id'])
        print("Tweet Text: " + response['text'])
        print("Tweeter ID: " + response['author'])
        print("Tweeter Name: " + response['username'])