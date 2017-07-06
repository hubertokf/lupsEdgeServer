#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A small example subscriber
"""
from threading import Thread
import paho.mqtt.client as paho
import json

class Subscriber(object):
    """docstring for subscriber."""


    def __init__(self, parent):
        def on_connect(client, userdata, flags, rc):
            print(rc)

        def on_message(mosq, obj, msg):
        #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
            #print(msg.payload)
            self.new_json_result(msg.payload)
            self.core
            pass

        def on_publish(mosq, obj, mid):
            #print("mid: "+str(mid))
            pass

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

        rules           = self.core.API_access("get", "rules", model_id=None, data=None, param=None).json()

        for topico in rules:
            self.add_subscribe(topico['topico'])


    def add_subscribe(self, topico):
        self.core
        self.client.subscribe(topico, 0)

    def new_json_result(self, dados_publisher):

        # Converte de bytes para string e após para json
        my_new_string_value = dados_publisher.decode("utf-8")
        my_json = json.loads(my_new_string_value)

        # Criar o JSON no formato para enviar as regras
        # {'gateway': 1, 'uuID': '123e4567-e89b-12d3-a456-426655440001', 'event': 'gathering', 'collect_to_rule': True}

        param = {"uuid":my_json['uuID']}
        id_sensor       = self.core.API_access("get", "sensors", model_id=None, data=None, param=param).json()
        id_gateway           = {"id":id_sensor[0]['gateway']}

        json_rules={}

        json_rules['id_gateway'] = id_gateway['id']
        json_rules['id_sensor'] = my_json['uuID']
        json_rules['value'] = my_json['value_sensor']
        json_rules['collectDate'] = my_json['date']

        self.regra(json_rules)



    def regra(self,json_result_gathering):   # Verifica argumentos e criar objeto p chamar regras
        engine = EngineRule(self.core)

        string_rule = '{{ "evento": "e", "id": "{0}","valor": {1}, "id_gateway": {2} }}'.format(json_result_gathering['id_sensor'],json_result_gathering['value'],json_result_gathering['id_gateway'],json_result_gathering['collectDate'])
        #print(string_rule)
        #print("chegou no gathering, vai chamar regra")
        #engine.run_rules(string_rule)

from core.moduleOfRules.EngineRuleEdge import EngineRule





class client_loop (Thread):
    def __init__(self,client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.loop_forever()
