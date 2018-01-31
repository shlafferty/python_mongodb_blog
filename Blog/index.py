from bottle import route, run, template, static_file, os, request, redirect, response, get, delete, post
from bson import ObjectId
import datetime

from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client.BlogDB

blogColl = db.Blog
authColl = db.Auth

@route('/static/<filename:path>')
def get_static(filename):
    path = os.path.join(os.getcwd(), "static")
    return static_file(filename, root=path)

@route('/')
def index():
    return template('login', {"check": False})

@post('/')
def login():
    user = request.forms.get('username')
    passw = request.forms.get('password')
    results = authColl.find({"username":user, "password":passw})
    if results.count() > 0:
        return redirect("/blog")
    else:
        return template('login', {"check": True})

@route('/blog')
def blog():
    post_list = blogColl.find({})
    return template('blog', {"posts": list(post_list)})

@route('/blog/delete/<objID>')
def delete_post(objID):
    doc = blogColl.find_one_and_delete({'_id':ObjectId(objID)})
    return redirect("/blog")

@route('/blog/edit/<objID>')
def to_edit(objID):
    docToEdit = blogColl.find({'_id':ObjectId(objID)}, {"_id": True, "post": True})
    return template('edit', {"post": list(docToEdit)})

@post('/blog/edit/<objID>')
def edit_post(objID):
    text = request.forms.get('text')
    edited = blogColl.update_one({"_id":ObjectId(objID)}, {"$set": {"post":text}})
    return redirect("/blog")

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