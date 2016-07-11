
# coding: utf-8
import twython
import pandas as pd
import random


api_key = api_key
api_secret = api_secret
access_token = acess_token
token_secret = token_secret

#get_ipython().system('pip3 install twython')
#get_ipython().system('pip3 install Textblob')
#get_ipython().system('python3 -m textblob.download_corpora')
from textblob import TextBlob


twitter = twython.Twython(api_key, api_secret, access_token, token_secret)

df = pd.read_excel("poetrybot.xlsx", sheetname='Sheet1')

def random_poetry_sentence(lines):
    line = random.choice(lines)
    #output = sentence.format(line)
    return line
random_poetry_sentence(df['lines'])

poem = random_poetry_sentence(df['lines'])
translation = TextBlob(poem).translate(to="en")
translation_str = str(translation)

if len(translation_str) > 140:
    translation_str_tweet = translation_str[0:135]
else:
    translation_str_tweet = translation_str

if len(poem) > 140:
    poem_tweet = poem[0:135]
else:
    poem_tweet = poem

translation_tweet = translation_str_tweet + " " + "#詩經"
tweet = poem + " " + "#詩經"

twitter.update_status(status=tweet)
twitter.update_status(status=translation_tweet)
