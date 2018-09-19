#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta

import wget
import tweepy #https://github.com/tweepy/tweepy
import json
import urllib.request
import os


#Twitter API credentials
consumer_key = "jTC38AzwtgHKzLvusvOHm1ni4"
consumer_secret = "H1WnO5q4oIq0VRs9coqJ5BjSmkIcx2DEhoXBOz77JaI7k0wboJ"
access_key = "1039258380504846341-VzdOeFASNH5Kr2DSqLTtg7yIfIVEVy"
access_secret = "Fcwy6ArMGLJoIrEZUOT4Rp4J8E36FOt6nNPUF5NABEBWh"


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
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
       
    #write tweet objects to JSON
    # file = open('tweet.json', 'w') 
    # print("Writing tweet objects to JSON please wait...")
    # for status in alltweets:
    #     json.dump(status._json,file,sort_keys = True,indent = 4)
    
    
    # file.close()

    for status in alltweets:
    	#print(status.extended_entities)
    	# print(status.extended_entities.get('media'))
    	a = status.extended_entities.get('media')
    	# print(range(4))
    	# print(range(len(a)))
    	for i in range(0,len(a)):
    		# print (a[i])
    		url=a[i]['media_url']
    		fullfilename=os.path.join('/home/ece-student/EC 601/image/','img00'+str(i)+'.jpg')
    		urllib.request.urlretrieve(url, fullfilename)
    		print(url, fullfilename)

    		print(a[i]['media_url'])
    		
    	
    	
if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@anqiguo3")
