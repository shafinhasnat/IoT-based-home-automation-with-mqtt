import paho.mqtt.publish as publish
publish.single("topic/test","Hello from the other side!!!",hostname="test.mosquitto.org")
publish.single("topic/test","i must have called you thousand times!!!",hostname="test.mosquitto.org")
print('sod')
