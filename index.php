<html>
    <head><script>
setTimeout(function() {
  location.reload();
}, 2000);

</script></head>
    
    
<?php
include('setup.php');
    
$sql="SELECT * FROM esp WHERE id=1";
    
$result = mysqli_query($conn,$sql);
$resultCheck=mysqli_num_rows($result);
if ($resultCheck > 0){
    while($row=mysqli_fetch_assoc($result)){
        echo "Temperature:  ",(int)$row['temp'];
        echo "<br> Humidity:  ",(int)$row['humidity'];
}
}
?>
</html>