import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    print("publishing")
    while True:
        client.publish('mosquitto', 'Welcome to Mosq')
        client.loop(.1)


client = mqtt.Client()
client.on_connect = on_connect

client.connect("localhost", 1883, 60)


client.loop_forever()