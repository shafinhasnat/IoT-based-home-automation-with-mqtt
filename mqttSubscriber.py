import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
     print('Connected with result code:'+str(rc))
     client.subscribe('topic/test')

def on_message(client,userdata,msg):
     print(str(msg.payload.decode('utf-8')))
     if msg.payload==b'Hello from the other side!!!':
          print('yes')

     else:
          print('oks')

client=mqtt.Client()
client.connect("test.mosquitto.org",1883,60)

client.on_connect=on_connect
client.on_message=on_message

client.loop_forever()
