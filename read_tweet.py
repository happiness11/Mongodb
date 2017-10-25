from tweepy import Stream
from tweepy.streaming import StreamListener
from auth import get_auth
from pymongo import MongoClient
import json

keyword_list=['halloween'] #you can change the keyword and collection name and it will create in the mlab ie mongo
limit = 20

MONGODB_URI = "mongodb://root:Pa55w0rd1@ds047514.mlab.com:47514/tweets"
DBS_NAME = "tweets"
COLLECTION_NAME = "halloween"

class MyStreamListener(StreamListener):

    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):
        if self.num_tweets < limit:
            self.num_tweets += 1
            try:
                with MongoClient(MONGODB_URI) as conn:
                    collection = conn[DBS_NAME][COLLECTION_NAME]
                    tweet = json.loads(data)
                    collection.insert_one(tweet)
                #now I want to write to mongo not to json#
                # with open('tweet_mining.json', 'a') as tweet_file:
                #     tweet_file.write(data)
                    return True
            except BaseException as e:
                print ("Failed on_data: %s" % str(e))
            return True
        else:
            return False

    def on_error(self, status):
        print(status)
        return True

auth = get_auth()

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)