__author__ = "Ribo Mo"

'''
	For this program you need to create a user file which contains all of the 
user name, every line should include only one user name. 
'''

import tweepy

#auth
auth = tweepy.OAuthHandler(
	"#################",
	"#################")
auth.set_access_token(
	"#################",
	"#################")

#init
api = tweepy.API(auth)
f = open("tweets.txt","w")

#import user name
userFile = open("user","r")
userList = userFile.readlines()

#main function
f.write("user\ttime\tretweet\tfavorite\ttext\tcount\n")
for user in userList:
	timeline = api.user_timeline(user,count = 500)
	for tweet in timeline:
		count = 0;
		for c in tweet.text:
			if(c == "#"):
				count += 1
		user = user.strip("\n")
		text = ("%s,%s,%s,%s,%s,%s\n"
			%(user,tweet.created_at,tweet.retweet_count,tweet.favorite_count,count,tweet.text))
		f.write(text)
	print(user)

f.close()