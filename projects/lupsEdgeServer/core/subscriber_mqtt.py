#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A small example subscriber
"""
import paho.mqtt.client as paho

class subscriber(object):
    """docstring for subscriber."""
    def __init__(self, topic):
        client = paho.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.on_publish = on_publish

        client.connect("127.0.0.1", 1883)#, 60)

        client.subscribe(topic, 0)
        #client.subscribe("kids/yolo", 0)
        #client.subscribe("adult/#", 0)

        client.loop_forever()

def on_connect(client, userdata, flags, rc):
    print(rc)

def on_message(mosq, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(mosq, obj, mid):
        #print("mid: "+str(mid))
    pass
# vi: set fileencoding=utf-8 :
