import json
import tweepy
from auth import get_api

api = get_api()

def get_by_search(query, count):
    return tweepy.Cursor(api.search, q=query).items(count)

def get_my_timeline(count):
    return tweepy.Cursor(api.home_timeline).items(count)

tweets = get_by_search("Storm Brian", 10)


for tweet in tweets:
    print(tweet)
