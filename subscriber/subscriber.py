import time
import paho.mqtt.client as mqtt

broker="localhost"

def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe('mosquitto')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message=on_message

client.connect(broker, 1883, 60)

print("connecting to broker ",broker)

client.loop_forever()

