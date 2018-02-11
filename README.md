# PyMongo Blog and API example works

Created as a final project in a database course, the purpose of this project is to show
familiarity with the Python language and MongoDB through the use of PyMongo.

This project has two parts. The first is an API with no front-end design. It is meant to
test API calls to view and make alterations to the existing database; this is stored in
the API folder. The second shows a simple blog that shows all posts stored in a MongoDB
database and has options for editing the database through a front-end interface. The
design remains simplistic as functionality was the focus of the project. The second part
is stored in the Blog folder.

## Getting Started

### Prequisites

* **MongoDB** will be needed to create and run the database.
The Community Server Edition can be downloaded [here](https://www.mongodb.com/download-center?jmp=tutorials#community).

* **Python 2.7 or above** is naturally needed to run the Python code.
The Python language libraries can be downloaded [here](https://www.python.org/downloads/).

* **Bottle** is the Web Server Gateway Interface framework used to run the HTTP server hand routing.
Bottle can be installed using the pip package managmenet system. Further documentation for installing Bottle can be found [here](https://bottlepy.org/docs/dev/).
```
pip install bottle
```

* **PyMongo** is the last piece to provide you with the tools needed for Python to work with MongoDB. Instructions for the installation can be found [here](https://api.mongodb.com/python/current/installation.html).

* **Postman (Optional)** is a RESTful client can be used for making API calls and display the data that is returned.
It can be run as an extension to Chrome or as a native app on your system.
Installation instructions and documentation can be found [here](https://www.getpostman.com/docs/postman/launching_postman/installation_and_updates).

### Installing

* You can simply download a ZIP of the files or clone the repository to the directory you would like to work in
```
git clone https://github.com/shlafferty/python_mongodb_blog.git
```

## Prep for running the blog and API
* First run the mongod.exe to start the database process from the command prompt
'''
"C:\Program Files\MongoDB\Server\3.6\bin\mongod.exe"
'''
* Navigate to the directory where you copied the collection of files
* Run the CreateBlog.py file to create the database of blog posts and users in MongoDB

### Running the Blog website
* Navigate to the Blog directory and run the *index.py* file. This will start the Bottle HTTP server on localhost using port 8082
```
http://localhost:8082
```
* Directing your browser to local host will pull up the login page. Login that are already part of the authentication database are four users ranging from "user1" to "user4". The password for all accounts is simply "pass2018". A proper sign-in will bring you to the main blog page.
* The features of the page that have been implemented are creating, editing, and deleting posts. There is no option for creating or altering comments at this time.

## Running the API
* Navigate to the API directory and run the *index.py* file. This will start the Bottle HTTP server on localhost using port 8083
```
http://localhost:8083
```
* There is no front-facing webpage for using the API, you can use Postman or another RESTful client for your API calls.
* The features of the page that have been implemented are creating, editing, and deleting posts. There is no option for creating or altering comments at this time.

## Author
* Shaun Lafferty