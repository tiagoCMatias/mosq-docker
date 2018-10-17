import paho.mqtt.client as mqtt
import time
import os

# The callback for when the client receives a CONNACK response from the server.


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    print("publishing")
    welcome_message = 0
    while True:
        welcome_message = welcome_message+1
        client.publish(os.environ['MOSQUITTO_TOPIC'],
                       'Welcome to Mosq ', welcome_message)
        client.loop(.1)
        if welcome_message > 1000
        welcome_message = 0


client = mqtt.Client()
client.on_connect = on_connect

client.connect(os.environ['MOSQUITTO_HOST'],
               int(os.environ['MOSQUITTO_PORT']), 60)


client.loop_forever()
