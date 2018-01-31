<!DOCTYPE html>
<html>
<head>
    <title>Blog: Login</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
</head>
<body>
    <div id="login">
        <h1><code>Blog</code></h1>
        <form action="/" method="post">
            <p>Username</p><div><input type="text" name="username"></div>
            <p>Password</p><div><input type="password" name="password"></div>
            <div><input type="submit" value="Sign In"></div>
            %if check:
                <p id="error">Either the username or password is incorrect</p>
            %end
        </form>
    </div>
</body>
</html>