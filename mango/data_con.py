import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure
from datetime import datetime
def main():

	try:
		c = Connection(host="localhost", port=27017)
	except ConnectionFailure, e:
		sys.stderr.write("Could not connect to MongoDB: %s" % e)
		sys.exit(1)
	# Get a Database handle to a database named "mydb"
	dbh = c["mydb"]

	assert dbh.connection == c
	user_doc = {
	"username" : "janedoe",
	"firstname" : "drek",
	"surname" : "Doe",
	"dateofbirth" : datetime(1974, 4, 12),
	"email" : "janedoe74@example.com",
	"score" : 0,
	"views":53,
	"categories" : "explore",
	}
	dbh.side.insert(user_doc, safe=True)
	print "u ser   s : %s  \n" % dbh.side
	print "Successfully inserted document: %s \n" % user_doc
	users = dbh.side.find({"firstname":"Jane"})
	print users.count()
	for user in users:
		
		print user.get("email")
	print "donme"
	print dbh.connection


if __name__ == "__main__":
	main()