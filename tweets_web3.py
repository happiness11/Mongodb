from flask import Flask, request
from flask import render_template
import os
from pymongo import MongoClient
from auth import get_api, MONGODB_URI
import tweepy
import json

MONGO_DB_NAME = "tweets"


def get_by_search(query, count):
    api = get_api()
    tweets = tweepy.Cursor(api.search, q=query).items(count)
    
    tweets_list = []
    for tweet in tweets:
        tweets_list.append(tweet._json)
    return tweets_list
    
    




app = Flask(__name__)

previous_searches = set()

@app.route("/")
def show_search_page():
    return render_template("search.html")


@app.route("/search")
def do_search():
    q = request.args.get('query')
    n = int(request.args.get('num'))
    previous_searches.add(q)

    with MongoClient(MONGODB_URI) as conn:
        db = conn[MONGO_DB_NAME]
        collection = db[q]
        collections_we_have = db.collection_names()
        
        # Search Twitter    
        if q in collections_we_have:
            #Get it from Mongo
            tweets = collection.find()
        else:
            #Get it from Twitter and save to Mongo
            tweets = get_by_search(q, n)
            collection.insert_many(tweets)

    return render_template("results.html", searched_for=q, the_tweets=tweets)

@app.route("/previous")
def show_previous():
    return render_template("previous.html", search_terms = previous_searches)









@app.route("/searchinurl/<query>")
def do_url_search(query):
    return "You searched for {0}".format(query)


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
