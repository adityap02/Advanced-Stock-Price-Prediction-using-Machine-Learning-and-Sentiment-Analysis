import tweepy
import csv
import pandas as pd
import re

from textblob_analysis import cl,cl1
consumer_key = 'fM9sSIoN9oTuC65TQTA42AcGh'
consumer_secret = 'LeSnaQFeoHeCE8LqCHqDqeSyL6ZVSHz946NzwFpgB4qypTuodr'
access_token = '625427849-XFSWT7dRokATsiiuHGHMwigYurnm2hDMTi6FFXye'
access_token_secret = 'V5Nt3hnmIuVTZWMEKKS1jHZFDIe2LV0SZDyeJuWVPKpBC'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

def pre_process(tweets):
    tweets = tweets.lower()  # convert text to lower-case
    tweets = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','', tweets)  # remove URLs
    tweets = re.sub('@[^\s]+','', tweets)  # remove usernames
    tweets = re.sub(r'#([^\s]+)', r'\1', tweets)# remove the # in #hashtag
    return tweets

# Open/Create a file to append data

#Use csv Writer
ticker=input("enter stock ticker")
file_name='sentiments/'+ticker+"_sentiment.csv"
csvFile = open(file_name, 'a')
csvWriter = csv.writer(csvFile)


def sent_analysis(file_name):
    data = pd.read_csv(file_name)
    data = data.iloc[:, -1]
    # print(data)
    pos_count = 0
    neg_count = 0
    data = data.values.tolist()
    length = len(data)
    for i in range(length):
        if (data[i] == 'pos'):
            pos_count = pos_count + 1
        elif (data[i] == 'neg'):
            neg_count = neg_count + 1
    print("=============================")
    print("sentiment analysis of tweets ")
    print("No of tweets classified as positive: ", pos_count)
    print("No of tweets classified as negative: ", neg_count)
    pos_percentage=pos_count*100/(neg_count+pos_count)
    neg_percentage=neg_count*100/(neg_count+pos_count)
    print("positive percentage: " ,pos_percentage)
    print("negative percentage: ", neg_percentage)
    print("==============================")






def fetch_new_tweets():
    q = input("enter stock keyword:")
    count = 1
    print("=================================================")
    print(" Fetching new tweets ")
    print("=================================================")
    for tweet in tweepy.Cursor(api.search,q,count=100,lang="en",since="2020-04-10",tweet_mode='extended').items(10000):
        temp=tweet.full_text
        temp=pre_process(temp)
        if(cl1.classify(temp) == True):
            classification=cl.classify(temp)
            #if(blob.sentiment.subjectivity>0 and blob.sentiment.polarity!=0):
            print(count, ": " + temp +"sentiment: ",cl.classify(temp))
            count=count+1
            #csvWriter.writerow([count,tweet.id,tweet.full_text.encode('utf-8'),sentiment,subjectivity,classification])
            csvWriter.writerow([count,tweet.id, tweet.full_text.encode('utf-8'),classification])
        else:
             print(count, "Irrelevant: " + temp +"sentiment: ",cl.classify(temp))
             count=count+1


fetch_new_tweets()
#sent_analysis(file_name)






