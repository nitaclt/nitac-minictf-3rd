<?php
require_once 'util.php';

session_start();

if (!is_logged_in()) {
    header("Location: /login.php");
    exit(0);
}

if (empty($_GET['lang'])) {
    $_GET['lang'] = "en.html";
}
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Home</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </head>
    
    <body>
        <main role="main" class="container">
            <?php include("templates/" . $_GET['lang']); ?>
        </main>
        <hr>
        <footer role="footer" class="container">
            <a href="/?lang=en.html">English</a>
            <a href="/?lang=ja.html">日本語</a>
            <a href="/?lang=ch.html">中文</a>
            <a href="/?lang=ko.html">한글</a>
            <br>
            <p><?php print(file_get_contents("/flag1.txt")); ?></p>
        </footer>
    </body>
</html>
