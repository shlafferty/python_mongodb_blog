<!DOCTYPE html>
<html>
	<head>
		<title>Blog: Edit</title>
		<link rel="stylesheet" type="text/css" href="/static/css/style.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	</head>
		<body>
        %for p in post:
            <form id="editForm" action="/blog/edit/{{p['_id']}}" method="POST">
                <p>Edit Your Post</p><div><textarea id="inputText"  rows="4" cols="50" name="text" form="editForm">{{p['post']}}</textarea></div>
                <div><input type="submit" value="Edit"></div>
            </form>
        %end
		</body>
</html>