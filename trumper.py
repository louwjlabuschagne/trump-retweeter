import tweepy
from time import gmtime, strftime
import pickle

def log_print(message):
    print('[%s]: %s'%(strftime("%Y-%m-%d %H:%M:%S", gmtime()), message))

(consumer_key, consumer_secret, access_token, access_token_secret) = pickle.load(open('keys.pkl', 'rb'))

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
trump = api.get_user('realDonaldTrump')
latest_tweet = trump.status
latest_tweet_id = latest_tweet.id

f = open('trumper.log','a+')
try:
    api.retweet(latest_tweet_id)
    result = 'Tweeted \n%s'%latest_tweet.text.encode('ascii', 'ignore')
except tweepy.error.TweepError:
    result = 'Already Tweeted \n%s'%latest_tweet.text.encode('ascii', 'ignore')
    exit()
log_print(result)
f.write(result)
f.close()
