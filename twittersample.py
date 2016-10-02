#!/usr/bin/env python3
# __author__: bplank
import argparse
import json
from twitter import OAuth, TwitterStream

parser = argparse.ArgumentParser("Example: Accessing the Twitter Streaming API")
parser.add_argument('--credentials','-c', help="user credentials (required)",required=True)
parser.add_argument('--count', help="number of tweets", default=10)

args = parser.parse_args()

## Load your credentials
credentials = json.load(open(args.credentials))

CONSUMER_KEY=credentials["CONSUMER_KEY"]
CONSUMER_SECRET=credentials["CONSUMER_SECRET"]
ACCESS_TOKEN=credentials["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET=credentials["ACCESS_TOKEN_SECRET"]

my_authentication = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Init the connection to the Twitter Streaming API
twitter_stream = TwitterStream(auth=my_authentication)

# Get a sample from the Twitter Streaming API (it's an endless loop)
iterator = twitter_stream.statuses.sample()

i=0
for tweet in iterator:
    if i < args.count:
        if "text" in tweet:
            text = tweet["text"]
            date = tweet["created_at"]
            print(text, date)
    i+=1



