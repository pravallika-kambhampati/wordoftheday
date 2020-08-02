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
RAPID_API_KEY = os.environ['RAPID_API_KEY']

INTERVAL = 60 * 60 * 24

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def getWordandMeaning():
    url = "https://wordsapiv1.p.rapidapi.com/words/"
    querystring = {"random":"true"}

    headers = {
       'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': RAPID_API_KEY
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
