def simulationThingworx(connection, frequency, timeInterval, minRange, maxRange):
    import sys
    import paho.mqtt.client as mqtt
    import time
    import json
    import random
    import logging

    logging.basicConfig(filename='test.log', level=logging.DEBUG, 
    format='%(asctime)s:%(levelname)s:%(message)s')

    
    # Callback from MQTT call
    def on_message(client, userdata, message):
        logging.debug("message received ", str(message.payload.decode("utf-8")))
        logging.debug("message topic=", message.topic)
        logging.debug("message qos=", message.qos)
        logging.debug("message retain flag=", message.retain)


##############################################################################################################################
# Configurations
    broker = connection['broker']
    topic = connection['topic']
    client = mqtt.Client("simulator")


##############################################################################################################################
# Publishing Data to Cloud


    def tempHumidityChange(test):
        client.on_message = on_message
        logging.debug("Connecting to Broker : ", broker)
        client.connect(broker)
        client.loop_start()
        client.publish(topic, test)
        logging.debug("published")
        logging.debug(test)
        time.sleep(4)
        client.loop_stop()

##############################################################################################################################


# Getting Temperature and Humidity from DHT11 sensor.

    def tempGen():
        a = random.randint(minRange, maxRange)
        return a

    def humidityGen():
        a = random.randint(minRange, maxRange)
        return a
# Sending data to Thingworx Cloud Continously using MQTT
    i = 0
    while i < frequency:
        humidity = humidityGen()
        temperature = tempGen()
        test = {"temperature": str(temperature), "humidity": str(humidity)}
        testJson = json.dumps(test)
        tempHumidityChange(testJson)
        i = i + 1
        time.sleep(timeInterval)
