import twitter

api = twitter.Api(consumer_key = "v0oGW2xIpG8X1n8tHcbuGg",
	consumer_secret = "uUyLOYLfILknDrWIqPn9WrwpKQFsgGR2IRnIS8Yiio",
	access_token_key = '1109121336-SKdqL9vZfAor4QE5k7R9FCIT43ilwTsccidL1rH',
	access_token_secret = 'V0j5nsXOr878qRaimUjws4Cwf4L4KtCgG8LbZEo')

users = api.GetFriends()

for s in users:
	print s.text
	print "\n"
	
print api.VerifyCredentials()
statuses = api.GetUserTimeline("srinath")
print "status updates"
for s in statuses:
	print s.text
	print "\n"

print "friends or following"




# print "updating status"

# status = api.PostUpdate('I love python-twitter!')

# print " staus text "+status.text