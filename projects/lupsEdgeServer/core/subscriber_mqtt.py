#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A small example subscriber
"""
from threading import Thread
import paho.mqtt.client as paho

class Subscriber(object):
    """docstring for subscriber."""
    def __init__(self, parent):
        #threading.Thread.__init__(self)
        self.core = parent

        self.client = paho.Client()
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.on_publish = on_publish

        self.client.connect("127.0.0.1", 1883)

        # CLIENT_LOOP é colocado em uma thread para que o programa não entre em
        # loop e não add novos TOPICOS
        client_loop(self.client).start()

        # Verifica os TOPICOS existentes nas regras
        #param = {"uuid":parameters['id']}
        #id_sensor       = self.core.API_access("get", "rules", model_id=None, data=None, param=param).json()
        #param = {"sensor":id_sensor[0]['id']}

        rules           = self.core.API_access("get", "rules", model_id=None, data=None, param=None).json()
        #topic = rule[0]['topico']
        # for key, value in param.items():
        for topico in rules:
            print("++++++++++++++++++++++++++++")
            #print(topico['topico'])
            self.add_subscribe(topico['topico'])
            print("++++++++++++++++++++++++++++")


    def add_subscribe(self, topico):
        print("++++++++++++++++++++++++++++")
        #print(topico)
        #print("++++++++++++++++++++++++++++")
        #juca = topico
        self.client.subscribe(topico, 0)

def on_connect(client, userdata, flags, rc):
    print(rc)

def on_message(mosq, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(mosq, obj, mid):
        #print("mid: "+str(mid))
    pass

class client_loop (Thread):
    def __init__(self,client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.loop_forever()
