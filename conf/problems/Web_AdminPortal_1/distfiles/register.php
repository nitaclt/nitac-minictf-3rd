<?php
require_once 'util.php';

session_start();

function redirect($msg="", $error="") {
    header(sprintf("Location: /login.php?msg=%s&error=%s",
                   urlencode($msg), urlencode($error)));
    exit(0);
}

if (is_logged_in()) {
    header("Location: /");
    exit(0);
}

if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = (string)$_POST['username'];
    $password = (string)$_POST['password'];
    
    if (register($username, $password)) {
        redirect("Registered new user", "");
    } else {
        redirect("", "Username already taken");
    }
}

redirect("", "Invalid request");
?>
