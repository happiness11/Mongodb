import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = '54LxUVaH0m60f6jksl8KRjL0x'
CONSUMER_SECRET = 'NMlzQwz0IUKNb2BMtMLAIVAlDlwCRr2KosZQ7sE9jXmoPR5WhE'
OAUTH_TOKEN = '756425691386748928-vnV7zu9bvbpxFf7jcNTNZK7WW3NGc9G'
OAUTH_TOKEN_SECRET = 'hl4EUIXlmtmklH6sBDhgcCnThK9MiOvlV5dxCOi14sezj'
MONGODB_URI = "mongodb://root:Pa55w0rd1@ds047514.mlab.com:47514/tweets"

def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth

def get_api():
    auth = get_auth()
    return tweepy.API(auth)