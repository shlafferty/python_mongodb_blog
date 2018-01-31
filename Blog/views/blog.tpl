<!DOCTYPE html>
<html>
	<head>
		<title>Blog: Home</title>
		<link rel="stylesheet" type="text/css" href="/static/css/style.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	</head>
		<body>
				<div>
                    %for p in posts:
                        <div class="post">
                            <div class="post-topper">
                                <p class="date">{{p['posted']}}</p>
                                <a class="delete" href="/blog/delete/{{p['_id']}}">X</a>
                            </div>
                            <a class="edit" href="/blog/edit/{{p['_id']}}">Edit</a>
                            <p class="user">{{p['user']}}</p>
                            <p class="text">{{p['post']}}</p>
                        %for c in p["comments"]:
                            <div class="comment">
                                <div class="comment-topper">
                                        <p class="date">{{c['posted']}}</p>
                                </div>
                                <p class="user">{{c['user']}}</p>
                                <p class="text">{{c['comment']}}</p>
                            </div>
                        %end
                        </div>		
                    %end
                </div>				


            <form id="addForm" action="/blog" method="POST">
                <p>Add a new blog post here:</p>
                <p>Username</p><div id="user"><input id="inputAuth" type="text" name="author"></div>
                <p>Post</p><div><textarea id="inputText"  rows="4" cols="50" name="text" form="addForm"></textarea></div>
                <div><input type="submit" value="Add Post"></div>
            </form>
		</body>
</html>