from Blog import blog_posts, authentication
from pymongo import MongoClient

# Create an instance of the MongoClient connecting to the local host
mongo_client = MongoClient("localhost", 27017)

# Access 'BlogDB' instance
db = mongo_client.BlogDB

# Declare variables for Blog and Auth collections retrieved from the database
blogColl = db.Blog
authColl = db.Auth

# Insert the collections taken from the Blog.py file into the database
# Store array of the object IDs in 'results'
# Each command is followed by stating how many records were sucessfully inserted
results = blogColl.insert_many(blog_posts).inserted_ids
"{} blog records were inserted ".format(len(results))
results = authColl.insert_many(authentication).inserted_ids
"{} authentication records were inserted ".format(len(results))