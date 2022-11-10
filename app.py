import csv
import random
import tweepy
import datetime
import time

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

with open ('twitter-bot/languages.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    languages = []
    
    for row in reader:
        languages.append(row['Text'])
        
while True:
    x = datetime.datetime.now()
    hour = x.strftime("%H")
    if hour == 9:
        api.update_status(languages[random.randrange(len(languages))])
        time.sleep(36003)
    

