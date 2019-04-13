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
latest_status = trump.status
id = latest_status.id
tweet = latest_status.text.encode('ascii', 'ignore').decode('ascii', 'ignore')

try:
    api.retweet(id)
    result = 'Tweeted \n'+tweet
except tweepy.error.TweepError:
    result = 'Already Tweeted \n'+tweet

log_print(result)
with open('trumper.log','a+') as f:
    f.write('[%s]: %s\n'%(strftime("%Y-%m-%d %H:%M:%S", gmtime()), result))
