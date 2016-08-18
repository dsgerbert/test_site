<!DOCTYPE html>
<html>
<head>
<link href="static/style.css" rel="stylesheet" type="text/css">
</head>
<body>
<div>
<img alt="Logo images" height="768" width="1024" src="images/logo.jpg" alt="Logo images">
</div>
<h1>Добро пожаловать в {{msg}}!</h1>
%if cur_hour in range(6,10):
    <h2>Good morning!</h2>
%elif cur_hour in range(11,18):
    <h2>Good day!</h2>
%elif cur_hour in range(19,23):
    <h2>Good evening!</h2>
%else:
    <h2>Good night!</h2>
%end
</body>
</html>