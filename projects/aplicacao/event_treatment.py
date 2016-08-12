#from proceeding import *
#from publisher import *
from gathering import *
import json

class Event_Treatment(object):

    def set_id(self, id_devices):
        self.id_devices = id_devices

    def get_id(self):
        return self.id_devices

    def set_tipo_evento(self, tipo_evento): # 1 = Proceeding |   2 = Publisher  | 3 = Gathering
        self.tipo_evento = tipo_evento

    def get_tipo_evento(self):
        return self.tipo_evento

    def event(self, select_features, response):
        #print(response)

        jsonObject = json.loads(response)

        self.set_id(jsonObject['id_sensor'])
        self.set_tipo_evento(jsonObject['event'])

        if select_features == 0:

            if self.get_tipo_evento() == "proceeding":        # Cria objeto Proceeding
                print('Proceeding')
                #event = Proceeding()

            elif self.get_tipo_evento() == "publisher":   # Cria objeto Publisher
                print('Publisher')
                #event = Publisher()

            elif self.get_tipo_evento() == "gathering":   # Cria objeto Gathering
                print('Gathering')
                #event = Gathering()
                #print('FOI')

            else:
                print("Nenhum do casos no TRATAMENTO EVENTO 1")
                #print(self.get_tipo_evento())
        else:
            if self.get_tipo_evento() == "proceeding":
                print('Proceeding')
                #event = Proceeding()
            elif self.get_tipo_evento() == "publisher":
                print('Publisher')
                #event = Publisher()
            elif self.get_tipo_evento() == "gathering":
                print('Sensor: ', jsonObject['id_sensor'])
                #event = Gathering()
                #event.processamento(1, select_features) # 1 em referencia ao sensor 1
            else:
                print("Nenhum do casos no TRATAMENTO EVENTO 2")
