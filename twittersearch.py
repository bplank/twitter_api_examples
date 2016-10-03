import twitter
import json
from twitter import Twitter, OAuth, TwitterStream

cred = json.load(open("private/credentials-barbara.json"))
# Initiate the connection to Twitter REST API

my_authentication = OAuth(cred["ACCESS_TOKEN"], cred["ACCESS_TOKEN_SECRET"], \
                          cred["CONSUMER_KEY"], cred["CONSUMER_SECRET"])

twitter = Twitter(auth=my_authentication)
            
# Search for latest tweets, e.g. about Groningen or "#digitalhumanities" etc.
query =  twitter.search.tweets(q='Groningen',count=10)
for tweet in query["statuses"]:
    print(tweet['user']['screen_name'],tweet['text'])

