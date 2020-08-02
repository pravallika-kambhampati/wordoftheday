import os
from os import environ
import tweepy
from tweepy import OAuthHandler
import time
import requests
import json


ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET  = os.environ['ACCESS_SECRET']
CONSUMER_KEY      = os.environ['C_KEY']
CONSUMER_SECRET   = os.environ['C_SECRET']


INTERVAL = 60 

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def getWordandMeaning():
    url = "https://wordsapiv1.p.rapidapi.com/words/"
    querystring = {"random":"true"}

    headers = {
       'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "a5a88e0350msh6b929f7ff2a0fa1p1583c7jsn84f6dbb3ca43"
       }
    

    while True:
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            response_obj = json.loads(response.text)
            randomword = response_obj['word']
            meaning = response_obj['results'][0]['definition']
            print(randomword,meaning)
            break
        except KeyError:
            pass

    return randomword, meaning 

while True:
    word, meaning = getWordandMeaning()
    tweet_content = f"Word of the day: {word}, Meaning: {meaning}"
    api.update_status(tweet_content)    
    time.sleep(INTERVAL)
