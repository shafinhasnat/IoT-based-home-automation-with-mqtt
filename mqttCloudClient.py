import paho.mqtt.client as mqtt
class IoT():
     def __init__(self):
          pass
     def on_connect(self,client,userdata,flags,rc):
          print('Connected with result code:'+str(rc))
          client.subscribe('Publish/#')

     def on_message(self,client,userdata,msg):
          print(str(msg.payload.decode('utf-8')))
     ##     print(client.publish("/Subscribe",'from pc'))
          if str(msg.payload.decode('utf-8'))=='on':
               print(client.publish("/Subscribe",'Lights on'))
          elif str(msg.payload.decode('utf-8'))=='off':
               print(client.publish("/Subscribe",'Lights off'))
if __name__=='__main__':
     IoT=IoT()
     client=mqtt.Client()
     client.on_connect=IoT.on_connect
     client.on_message=IoT.on_message
     client.connect('m16.cloudmqtt.com',12939,60)
     client.username_pw_set("xilebdfu","MknOzEMGsFs0")
     client.loop_forever()
