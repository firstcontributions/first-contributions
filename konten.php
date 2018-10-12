<?php include 'header.php'; ?>

<div class="content">
	<p>Ini Body Konten</p>

<?php 
if (isset($_POST['nim']) && isset($_POST['Alamat']) && isset($_POST['Jenis'])) {

	echo "Nama : " . $_POST['nim']. "<br>";
echo "Alamat : " . $_POST['Alamat']. "<br>";
echo "Gender : " . $_POST['Jenis']. "<br>";

} else {
	echo "ehok";
	# code...
}


 ?>

	
</div>


<?php require 'footer.php'; ?>
