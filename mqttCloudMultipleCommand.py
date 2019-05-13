import paho.mqtt.client as mqtt
class IoT():
    new_fan=0
    new_light=0
    def __init__(self,fan=0,light=0):
        self.fan=fan
        self.light=light
        ##########fan##########
##        if self.new_fan=='on':
##            print(client.publish("/Subscribe",'Fan on'))
##        elif self.new_fan=='off':
##            print(client.publish("/Subscribe",'Fan off'))
##        ##########Light##########
##        if self.new_light=='on':
##            print(client.publish("/Subscribe",'Light on'))
##        elif self.new_light=='off':
##            print(client.publish("/Subscribe",'Light off'))
##
##
##
##        print('fan state:',self.new_fan,'--- light state:',self.new_light)
##            
            

        if self.fan!=0:
            self.new_fan=fan
        if self.light!=0:
            self.new_light=light
        pass
    
    def on_connect(self,client,userdata,flags,rc):
        print('Connected with result code:'+str(rc))
        client.subscribe('Publish/#')
        client.subscribe('Publish1/#')

    def on_message_light(self,client,userdata,msg):
        print(msg.payload)
        command=str(msg.payload.decode('utf-8'))
        print(command)
        self.__init__(light=str(msg.payload.decode('utf-8')))
        pass
    
    def on_message_fan(self,client,userdata,msg):
        print(str(msg.payload.decode('utf-8')))
        self.__init__(fan=str(msg.payload.decode('utf-8')))
        pass
        
if __name__=='__main__':
    IoT=IoT()
    client=mqtt.Client()
    client.on_connect=IoT.on_connect
    client.message_callback_add('Publish/#',IoT.on_message_light)
    client.message_callback_add('Publish1/#',IoT.on_message_fan)
    client.connect('m16.cloudmqtt.com',12939,60)
    client.username_pw_set("xilebdfu","MknOzEMGsFs0")
    client.loop_forever()
