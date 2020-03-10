import tweepy
import time

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #these all keys can be obtained from your twitter developer account
# auth.set_access_token(access_token, access_token_secret)  #insert keys before running the script

api = tweepy.API(auth)
user = api.me()
print(user.name) #Returns Twitter username
print(user.screen_name) #Returns Twitter Handle
print(user.followers_count) #Returns follower count
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

#Generous Bot - This bot will always follow back

# for follower in tweepy.Cursor(api.followers).items(): #cursor allows to go through the entire twitter
#     #print(follower.name)
#     if follower.name == 'TodayCat': #specify the account to follow
#         follower.follow()


#A bot that loves your own tweets or loves tweets based on certain
search_string = 'Cristiano'  #search word
number_tweets = 4 #no of tweets
for tweet in tweepy.Cursor(api.search,search_string).items(number_tweets):
    try:
        tweet.favorite()
        print('I liked the tweet')
    except tweepy.TweepError as e :
        print(e.reason)
    except StopIteration:
        break