from bottle import route, run, template, static_file, os, request, redirect, response, get, delete, post
from bson import ObjectId
import datetime

from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client.BlogDB

blogColl = db.Blog
authColl = db.Auth

#static file routing
@route('/static/<filename:path>')
def get_static(filename):
    path = os.path.join(os.getcwd(), "static")
    return static_file(filename, root=path)

# Index routing to login page
@route('/')
def index():
    return template('login', {"check": False})

# Post request attempts simple credentials check for login, return login page with
# error flag if failed, returns blog view if successful
@post('/')
def login():
    user = request.forms.get('username')
    passw = request.forms.get('password')
    results = authColl.find({"username":user, "password":passw})
    if results.count() > 0:
        return redirect("/blog")
    else:
        return template('login', {"check": True})

# Direct route to blog view
@route('/blog')
def blog():
    post_list = blogColl.find({})
    return template('blog', {"posts": list(post_list)})

# Will find object matching the objectID of the post given in MongoDB and delete it
@route('/blog/delete/<objID>')
def delete_post(objID):
    doc = blogColl.find_one_and_delete({'_id':ObjectId(objID)})
    return redirect("/blog")

# Will return edit view where new post content can be changed for
# post object given
@route('/blog/edit/<objID>')
def to_edit(objID):
    docToEdit = blogColl.find({'_id':ObjectId(objID)}, {"_id": True, "post": True})
    return template('edit', {"post": list(docToEdit)})

# From edit view, finds and updates the text content for the post matching the given
# objectID
@post('/blog/edit/<objID>')
def edit_post(objID):
    text = request.forms.get('text')
    edited = blogColl.update_one({"_id":ObjectId(objID)}, {"$set": {"post":text}})
    return redirect("/blog")

# From post form at bottom of blog view, adds new post object to the MongoDB database
# using the details submitted in the form as well as the current date
@post('/blog')
def add_post():
    author = request.forms.get('author')
    text = request.forms.get('text')
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    post = {"post":text, "user":author, "comments":{},"posted":date}
    blogColl.insert_one(post)
    return redirect('/blog')
    
if __name__ == "__main__":	
	run(host='localhost', port=8082, debug=True, reloader=True)