import tweepy
from localkeys import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

def profile_image(filename) :
    api.update_profile_image(filename)

# profile_image('purple bee creek-01.jpg')
def update_profile_info(name, url, location, description):
    api.update_profile(name, url, location, description)

def post_tweet(text):
    api.update_status(text)

post_tweet('New Kindle Vella Chapter for Last Burning Ember coming on the 8th! #kindle, #lastburningember, #fantasy')