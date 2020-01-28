<?php
require_once 'util.php';

session_start();

if (isset($_POST['username']) && isset($_POST['password'])) {
    login((string)$_POST['username'], (string)$_POST['password']);
    $error = 'Wrong username or password';
}

if (isset($_GET['msg'])) $msg = htmlspecialchars($_GET['msg']);
if (isset($_GET['error'])) $error = htmlspecialchars($_GET['error']);

if (is_logged_in()) {
    header("Location: /");
    exit(0);
}
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Login</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </head>
    <body>
        <main role="main" class="container">
            <?php if (!empty($error)) { ?>
                <div class="alert alert-warning alert-dismissible fade show" rule="alert">
                    <strong>Error!</strong> <?php echo $error; ?>
                    <button type="button" class="close" data-dismiss="alert" aria-label="close"><span aria-hidden="true">&times;</span></button>
                </div>
            <?php } ?>
            <?php if (!empty($msg)) { ?>
                <div class="alert alert-primary alert-dismissible fade show" rule="alert">
                    <strong>Error!</strong> <?php echo $msg; ?>
                    <button type="button" class="close" data-dismiss="alert" aria-label="close"><span aria-hidden="true">&times;</span></button>
                </div>
            <?php } ?>
            
            <h1 class="m-3">Login</h1>
            <form method="POST">
                <div class="form-group">
                    <label for="u">Username: </label>
                    <input type="text" name="username" id="u">
                </div>
                <div class="form-group">
                    <label for="p">Password: </label>
                    <input type="password" name="password" id="p">
                </div>
                <input type="submit" class="btn btn-primary" value="Login" formaction="/login.php">
                <!--
                <input type="submit" class="btn btn-success" value="Register" formaction="/register.php">
                -->
            </form>
        </main>
    </body>
</html>
