<?php session_start(); ?>
<?php 
        $db['db_host']= "localhost";
        $db['db_user']= "root";
        $db['db_pass']= "";
        $db['db_name']= "Image_upload";

        foreach($db as $key=>$value){
        	define(strtoupper($key),$value);
        }
        $connection = mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME); ?>
    <?php    
      if(isset($_POST['login'])){
      	$username = $_POST['username'];
      	$password=$_POST['password'];

        $_SESSION['uname']=$username;
        $_SESSION['pname']=$password;

      	$query = "SELECT * FROM login_table WHERE username= '$username' AND password= '$password' ";
      	$result=mysqli_query($connection,$query);
      	  if(mysqli_num_rows($result)){
            
           header("LOCATION:home_page.php");
          }
          else {
            echo "please check your inputs";
          }
         } 

 ?>

  
<!DOCTYPE html>
<html>
<head>
	<title>Login Page</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" crossorigin="anonymous">
</head>
<body> 
       <form action="" method="post">
     <div class="container" style="margin-top: 100px">
         <div class="row justify-content-center">
         	<div class="col-md-6">
         		<div class="form-group">
         		<label for="username">Username</label>
         		
         		   <input type="text" name="username" class="form-control">	
         		</div>
         	</div>
         </div>
         <div class="row justify-content-center">
         	<div class="col-md-6">
         	<div class="form-group">
         		<label for="password">Password</label>
         		
         		   <input type="password" name="password" class="form-control">	
         		</div>
         	</div>
         </div>

         <div class="row justify-content-center">
         	<div class="col-md-6">
         		<div class="form-group">
         		   <input type="submit" name="login" class="btn btn-success">	
         		</div>
         	</div>
         </div> 
       </div>
</form>



<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"  crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"  crossorigin="anonymous"></script>
</body>


</html>
