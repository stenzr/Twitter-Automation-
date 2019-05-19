import tweepy
import userCredentials

#twitter authentication

auth = tweepy.OAuthHandler(userCredentials.consumer_key, userCredentials.consumer_secret)
auth.set_access_token(userCredentials.access_token, userCredentials.access_token_secret)
api = tweepy.API(auth)

#printing tweets on home timeline

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


# Get the User object for <userName>...
user = api.get_user('username')


print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)


# Iterate through all of the authenticated user's friends
for friend in tweepy.Cursor(api.friends).items():
    # Process the friend here
    print(friend)

# Iterate through the first 200 statuses in the home timeline
for status in tweepy.Cursor(api.home_timeline).items(200):
    # Process the status here
    print(status)


#to check for potential spambots
#lists all followers who themselves folow less than 500 people

for follower in tweepy.Cursor(api.followers).items():
    if follower.friends_count < 500:
        print(follower.screen_name)


#lists the spambots
for follower in tweepy.Cursor(api.followers).items():
    if follower.friends_count > 500:
        print(follower.screen_name)



#to follow every follower
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

#streaming
from tweepy import Stream
from tweepy.streaming import StreamListener


class MyListener(StreamListener):

	def on_data(self, data):
		try:
			with open('python.json', 'a') as f:
				f.write(data)
				return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True

	def on_error(self, status):
		print(status)
		return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['keyword'])


