<?php
include('setup.php');

// Create connection
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$temp=$_GET['temp'];
$hum=$_GET['hum'];

$sql = "UPDATE esp SET temp=$temp,humidity=$hum WHERE id=1";
mysqli_query($conn, $sql);

mysqli_close($conn);
?>