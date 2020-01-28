<?php
/**
 * Check if the visitor is already logged in
 */
function is_logged_in() {
    if (isset($_SESSION['user'])) {
        return true;
    } else {
        return false;
    }
}

function connect_db() {
    $pdo = new PDO("sqlite:/var/www/sqlite.db");
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
    return $pdo;
}

/**
 * Try to login
 */
function login($username, $password) {
    $pdo = connect_db();
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username=? AND password=?");
    $stmt->execute([md5($username), md5($password)]);
    $r = $stmt->fetchAll();

    if (count($r) > 0) {
        $_SESSION['user'] = $username;
    }
}

/**
 * Register new account
 */
function register($username, $password) {
    $pdo = connect_db();

    if (user_exists($pdo, $username)) {
        return false;
    }
    
    $stmt = $pdo->prepare("INSERT INTO users(username, password) values(?, ?)");
    $stmt->execute([md5($username), md5($password)]);
    
    return true;
}

/**
 * Check if user exists
 */
function user_exists($pdo, $username) {
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username=?");
    $stmt->execute([md5($username)]);
    $r = $stmt->fetchAll();

    if (count($r) > 0) {
        return true;
    } else {
        return false;
    }
}
?>
