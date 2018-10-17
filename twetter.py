#!/usr/bin/env python
# encoding: utf-8
#Author - Anqi Guo

import tweepy #https://github.com/tweepy/tweepy
import json
import urllib.request
import os


#this is the twitter api credentials that we get from the twitter developer website, we need this credential keys to access the twitter api
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

#this is the funcation that we get all the twitters from the specefic user
def get_all_tweets(screen_name):
    
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print("...%s tweets downloaded so far" % (len(alltweets)))
       

#to get all the urls that in the json file
    for status in alltweets:
    	a = status.extended_entities.get('media')
#extract the media_url from media
    	for i in range(0,len(a)):
    		# print (a[i])
    		url=a[i]['media_url']
    		fullfilename=os.path.join('/home/ece-student/EC 601/image/','img00'+str(i)+'.jpg')
    		urllib.request.urlretrieve(url, fullfilename)
#download all the images from each image urls

    		print(a[i]['media_url'])
#print all the media urls
    		
    	
 #realise all the twitter urls   	
if __name__ == '__main__':
  #download images from anqiguo3
    get_all_tweets("@anqiguo3")
