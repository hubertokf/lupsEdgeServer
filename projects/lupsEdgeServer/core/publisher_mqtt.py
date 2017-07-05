#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Publish some messages to queue
"""
import paho.mqtt.publish as publish

class Publish(object):
    """docstring for publish."""
    def __init__(self):
        print("Criou objeto MQTT")
    #    client = paho.Client()

    def send_message(self, topic, payload, host):
        #publish.single(topic="kids/yolo", payload="just do it", hostname=host)
        publish.single(topic=topic, payload=payload, hostname=host)
        #print(topic)
        #print(payload)
        #print(host)
