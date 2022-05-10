# snscrape - social network scraping

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:elonmusk) until:2022-05-10 since:2012-01-01" #it is search copied from twitter search
tweets = []
limit = 100 # number of tweets #can be altered

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))   
    # break 
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])

print(df)