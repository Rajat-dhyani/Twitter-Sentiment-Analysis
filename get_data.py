import api_keys as keys
import tweepy
from datetime import datetime

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

class myListener(tweepy.StreamListener):

    def on_data(self, data):
        try:
            with open('adhar_data.json','a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True;

twitter_stream = tweepy.Stream(auth = api.auth, listener= myListener())
twitter_stream.filter(track=["Aadhaar", "Aadhaar Card", "Aadhar"])
