#include <ESP8266WiFi.h>
#include <WiFiClient.h> 
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
#include <DHTesp.h>
 
DHTesp dht;
 
/* Set these to your desired credentials. */
const char *ssid = "Syed";  //ENTER YOUR WIFI SETTINGS
const char *password = "chintsuzai1119";
 

void setup() {
  delay(1000);
  Serial.begin(9600);
  WiFi.mode(WIFI_OFF);        //Prevents reconnection issue (taking too long to connect)
  delay(1000);
  WiFi.mode(WIFI_STA);        //This line hides the viewing of ESP as wifi hotspot
  
  WiFi.begin(ssid, password);     //Connect to your WiFi router
  Serial.println("");
 
  Serial.print("Connecting");
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  //If connection successful show IP address in serial monitor
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());  //IP address assigned to your ESP
 
  dht.setup(4, DHTesp::DHT11);


  
}
 
//=======================================================================
//                    Main Program Loop
//=======================================================================
void loop() {
  HTTPClient http;    //Declare object of class HTTPClient
  
  float temperature = dht.getTemperature();
  float humidity = dht.getHumidity();
  
  Serial.print("Temperature: ");
  Serial.println(temperature);
  Serial.print("Humidity: ");
  Serial.println(humidity);
  
  String ADCData, station, getData, Link,temp,hum;
//  int adcvalue=digitalRead(D2);  //Read Analog value of LDR
//  ADCData = String(adcvalue);   //String to interger conversion
//  station = "B";
   temp=String(50);
   hum=String(23);
  //GET Data 103.231.163.1
  getData = "?temp=" + temp + "&hum=" + hum ;  //Note "?" added at front
  Link = "http://192.168.0.100/espcmd.php"+getData ;
  Serial.println(Link);
  http.begin(Link);     //Specify request destination
  
  int httpCode = http.GET();            //Send the request
  String payload = http.getString();    //Get the response payload
 
  Serial.println(httpCode);   //Print HTTP return code
//  Serial.println(payload);    //Print request response payload
 
  http.end();  //Close connection
  
  delay(10000);  //GET Data at every 5 seconds
}
