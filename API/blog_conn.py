from pymongo import MongoClient

# Create an instance of the MongoClient connecting to the local host
mongo_client = MongoClient("localhost", 27017)

# Access 'BlogDB' instance
db = mongo_client.BlogDB

# Declare variable for Blog collection retrieved from the database
blogColl = db.Blog