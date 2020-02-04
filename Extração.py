# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:50:55 2019

@author: gabri
"""
# -*- coding: UTF-8 -*-
import tweepy
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#informações para autenticar login
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''



#autenticacao
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#abre arquivo que salva os tweets
csvFile=open('quero me matar','a')
csvWriter =csv.writer(csvFile,delimiter=';')

for tweet in tweepy.Cursor(api.search,q = 'quero me matar -filter:retweets -filter:links -filter:images -filter:native_video',tweet_mode='extended', lang = "pt").items():
    if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
        csvWriter.writerow([tweet.user.screen_name,tweet.created_at,tweet.user.location.replace('\n', ' '),tweet.full_text.replace('\n', ' ')])
    
csvFile.close()


    