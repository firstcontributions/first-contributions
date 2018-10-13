<?php session_start(); ?>
  <?php if(!isset($_SESSION['uname'])){
  	header("Location:login.php");
  } ?>

<!DOCTYPE html>
<html>
<head>
	<title>Home Page</title>
</head>
<body>
     <h1><center>Hello!!<?php echo $_SESSION['uname'];  ?></center></h1>
     <center><a href="logout.php">Logout</a></center>
</body>
</html>
