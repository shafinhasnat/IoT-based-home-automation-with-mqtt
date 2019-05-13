<?php
require('E:/Software/xampp/htdocs/notrix/phpmqtt/phpMQTT.php');
$server = "m16.cloudmqtt.com";     // change if necessary
$port = 12939;                     // change if necessary
$username = "xilebdfu";                   // set your username
$password = "MknOzEMGsFs0";                   // set your password
$client_id = "phpMQTT-publisher"; // make sure this is unique for connecting to sever - you could use uniqid()
$mqtt = new phpMQTT($server, $port, $client_id);

$mqtt->connect(true, NULL, $username, $password);



$light=$_GET['light'];




$mqtt->publish("Publish", $light, 0);
//$mqtt->close();

header("Location: index.php");