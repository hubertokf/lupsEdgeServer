#from proceeding import *
#from publisher import *
#from gathering import *
import json

class Event_Treatment(object):

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_tipo_evento(self, tipo_evento): # 1 = Proceeding |   2 = Publisher  | 3 = Gathering
        self.tipo_evento = tipo_evento

    def get_tipo_evento(self):
        return self.tipo_evento

    def event(self, response):
        #print(response)

        jsonObject = json.loads(response)

        self.set_id(jsonObject['id_sensor_virtual'])
        self.set_tipo_evento(jsonObject['event'])

        if self.get_tipo_evento() == "proceeding":        # Cria objeto Proceeding
            print('Proceeding')
            #event = Proceeding()
            #event.processamento()

        elif self.get_tipo_evento() == "publish":   # Cria objeto Publisher
            print('Publisher')
            #event = Publisher()
            #event.
        elif self.get_tipo_evento() == "gathering":   # Cria objeto Gathering
            print('Gathering')
            #event = Gathering()
            #event.
        else:
            print("Nenhum do casos no TRATAMENTO EVENTO")
            #print(self.get_tipo_evento())
            #print(type("publish"))
            #print(type(self.get_tipo_evento()))
