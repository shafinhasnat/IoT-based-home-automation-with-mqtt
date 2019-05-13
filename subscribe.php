
            
            <?php
require("E:/Software/xampp/htdocs/notrix/phpmqtt/phpMQTT.php");
$server = "m16.cloudmqtt.com";     // change if necessary
$port = 12939;                     // change if necessary
$username = "xilebdfu";                   // set your username
$password = "MknOzEMGsFs0";                   // set your password
$client_id = "phpMQTT-subscriber"; // make sure this is unique for connecting to sever - you could use uniqid()
$mqtt = new phpMQTT($server, $port, $client_id);

echo "asdasdasd";
if(!$mqtt->connect()){
    exit(1);
}

$topics['Subscribe/#'] = array("qos"=>0, "function"=>"procmsg");
$mqtt->subscribe($topics,0);

while($mqtt->proc()){

}


$mqtt->close();

function procmsg($topic,$msg){
        echo "Msg Recieved: ".date("r")."\nTopic:{$topic}\n$msg\n";}?>
            ?>