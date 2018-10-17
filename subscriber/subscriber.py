import time
import os
import psycopg2 as psycopg2
import paho.mqtt.client as mqtt

db_connection = None


def connect_db():
    try:
        conn = psycopg2.connect(host="db",
                                database=os.environ["DB_NAME"],
                                user=os.environ["DB_USER"],
                                password=os.environ["DB_PASS"])
        conn.autocommit = True

    except:
        print("I am unable to connect to the database")
        return None

    cursor = conn.cursor()

    # Create Log Table if not exist
    query = """
        CREATE TABLE IF NOT EXISTS mosquitto_log (
            id SERIAL PRIMARY KEY,
            topic VARCHAR(256),
            message TEXT,
            timestamp TIMESTAMP,
        );
    """

    cursor.execute(query)

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

    client.connect(os.environ['MOSQUITTO_HOST'],
                   int(os.environ['MOSQUITTO_PORT']), 60)

    print("connecting to broker -", os.environ['MOSQUITTO_HOST'])

    client.loop_forever()
