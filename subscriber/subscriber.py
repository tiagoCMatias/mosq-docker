import time
import os
import psycopg2 as psycopg2
import paho.mqtt.client as mqtt

db_connection = None


def connect_db():
    try:
        conn = psycopg2.connect(host='postgres',
                                database=os.environ["POSTGRES_DB"],
                                user=os.environ["POSTGRES_USER"],
                                password=os.environ["POSTGRES_PASSWORD"])
        conn.autocommit = True

    except:
        print("I am unable to connect to the database")
        return None

    cursor = conn.cursor()

    try:

        # Create Log Table if not exist
        query = """
            CREATE TABLE IF NOT EXISTS public.mosquitto_log (
                id SERIAL PRIMARY KEY,
                topic VARCHAR(256),
                message TEXT,
                timestamp TIMESTAMP,
            );
        """

        cursor.execute(query)

        print("Table created")
    
    except:
        print("Unable to create table")

    finally:
        return cursor


def save_to_db(topic, message):
    query = """
        INSERT INTO mosquitto_log (id, topic, message, timestamp) VALUES (DEFAULT, '{}', '{}', 'now()');
    """.format(topic, str(message.decode()))
    db_connection.execute(query)


def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))
    save_to_db(msg.topic, msg.payload)  # msg.qos


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(os.environ['MOSQUITTO_TOPIC'])


if __name__ == '__main__':

    db_connection = connect_db()

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect('localhost',#os.environ['MOSQUITTO_HOST'],
                   1883,#int(os.environ['MOSQUITTO_PORT']), 
                   60)

    print("connecting to broker -")#os.environ['MOSQUITTO_HOST'])

    client.loop_forever()
