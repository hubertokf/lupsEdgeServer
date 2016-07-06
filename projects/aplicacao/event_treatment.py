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

        self.set_id(jsonObject['id_sensor_virtual'])
        self.set_tipo_evento(jsonObject['event'])

        if select_features == 0:

            if self.get_tipo_evento() == "proceeding":        # Cria objeto Proceeding
                #print('Proceeding')
                event = Proceeding()

            elif self.get_tipo_evento() == "publisher":   # Cria objeto Publisher
                #print('Publisher')
                event = Publisher()

            elif self.get_tipo_evento() == "gathering":   # Cria objeto Gathering
                #print('Gathering')
                event = Gathering()
                print('FOI')

            else:
                print("Nenhum do casos no TRATAMENTO EVENTO 1")
                #print(self.get_tipo_evento())
        else:
            if self.get_tipo_evento() == "proceeding":
                event = Proceeding()
            elif self.get_tipo_evento() == "publisher":
                event = Publisher()
            elif self.get_tipo_evento() == "gathering":
                event = Gathering()
                event.processamento(self, 1, select_features)
            else:
                print("Nenhum do casos no TRATAMENTO EVENTO 2")
