from bottle import route, run, request, response, get, delete, post, put, hook
from bson.json_util import dumps
from bson import ObjectId
from blog_conn import blogColl
from pymongo.errors import PyMongoError
import re, datetime

# API for blog CRUD operations
# MongoClient and database objects set in blog_conn.py
# Exceptions set for 400 bad request and 500 internal server error

# Get /blog request returns full collection of post and their comments sorted by date posted
@get("/blog")
def get_posts():
    try:
        try:
            allPosts = blogColl.find({}).sort("posted")
            if allPosts is None:
                raise ValueError
        except PyMongoError:
            raise EnvironmentError

    except EnvironmentError:
        response.status = 500
        return ({"error": "Blog postings are unavailable at this time"})
    except ValueError:
        response.status = 400
        return ({"error": "Blog posts could not be found"})

    response.headers['Cache-Control'] = 'cache'
    return dumps({"blog": allPosts})

# Get /blog/<author> searches for given username and returns collection of posts by that user
@get("/blog/<author>")
def get_blog(author):
    try:
        try:
            userPosts = blogColl.find({"user":author}).sort("posted")

            if userPosts is None:
                raise ValueError

        except PyMongoError:
            raise EnvironmentError
    
    except EnvironmentError:
        response.status = 500
        return ({"error": "Blog postings are unavailable at this time"})
    except ValueError:
        response.status = 400
        return ({"error": "Blog posts could not be found"})

    response.headers['Cache-Control'] = 'cache'
    return dumps({"UserPosts": userPosts})

# Put request will take username and text given, as well as current date and attempt to insert it
# into the existing database
@put("/blog")
def create_post():
    t = request.params.get('text')
    u = request.params.get('user')
    d = datetime.datetime.now().strftime('%Y-%m-%d')

    try:
        if (t is None) or (u is None):
            raise ValueError
        try:
            blogColl.insert_one({"post":t,"user":u,"posted":d,"comments":[]})

        except PyMongoError:
            raise EnvironmentError

    except EnvironmentError:
        response.status = 500
        return ({"error": "Blog postings are unavailable at this time"})
    except ValueError:
        response.status = 400
        return ({"error": "Blog posts could not be found"})

    response.headers['Cache-Control'] = 'no-cache'
    return ({"success":"Your post was successfully added"})

# Delete request will first make sure ID given is in correct format and then
# delete the record with that matching ID
@delete("/blog/<objID>")
def delete_post(objID):
    try:
        pattern = r'^[a-fA-F0-9]{24}$'

        if re.search(pattern, objID) is None:
            raise TypeError

        try:
            id = ObjectId(objID)
            results = blogColl.delete_one({"_id":id})

            if results.deleted_count == 0:
                raise ValueError

        except PyMongoError:
            raise EnvironmentError
	
    except EnvironmentError:
        response.status = 500
        return ({"error": "Blog postings are unavailable at this time"})
    except ValueError:
		response.status = 400
		return ({"error": "Blog posts could not be found"})
    except TypeError:
		response.status = 400
		return ({"error": "ID is not a proper ObjectID value"})

    response.headers['Cache-Control'] = 'no-cache'
    return ({"num_deleted": results.deleted_count})

# Post request will first make sure ID given is in correct format and then
# update the record with the provided username and text
@post("/blog")
def update_post():
    t = request.params.get('text')
    u = request.params.get('user')
    d = datetime.datetime.now().strftime('%Y-%m-%d')
    id = request.params.get('id')

    try:
        pattern = r'^[a-fA-F0-9]{24}$'

        if re.search(pattern, id) is None:
            raise TypeError

        if (t is None) or (u is None):
            raise ValueError

        try:
            id = ObjectId(id)
            results = blogColl.update_one({"_id":id}, {"$set": {"post":t, "user":u, "posted":d}})
        except PyMongoError:
            raise EnvironmentError
    
    except EnvironmentError:
        response.status = 500
        return ({"error": "Blog postings are unavailable at this time"})
    except ValueError:
        response.status = 400
        return ({"error": "Blog posts could not be found"})
    except TypeError:
        response.status = 400
        return ({"error": "ObjectId is not in the proper format"})

    response.headers['Cache-Control'] = 'no-cache'
    return ({"num_mod": results.modified_count, "_id":str(results.upserted_id)})

# Set headers to return response in JSON and allow cross origin requests
@hook('after_request')
def enable_cors():
    """Permit cross site requests and format response as json"""
    response.headers['Content-Type']='application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods']='PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers']='Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

run(host = 'localhost', port = 8083, debug=True, reloader=True)