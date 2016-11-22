#from core.proceeding import *
#from core.publisher import *
from core.publisher_context import *
from core.gathering import *
import json

class Event_Treatment(object):
    core = None

    def __init__(self, parent):             #instância do objeto e inicia o escalonador

        self.core = parent

    def event(self, response):
        #print(response)
        jsonObject = json.loads(response)
        # print(jsonObject)
        if jsonObject['event'] == "proceeding":
            print('Proceeding')
                #event = Proceeding()
        elif jsonObject['event'] == "publisher":
            print('Publisher')
            event = Publisher(self.core)
            # print(dir(Publisher))
            event.publish_to_rules(jsonObject)
        elif jsonObject['event'] == "gathering":
            #print('Sensor: ', jsonObject['id_sensor'])
            #print('uuID: ', jsonObject['uuID'])
            event = Gathering(self.core)
            #print(jsonObject['id_sensor'])
            if jsonObject['collect_to_rule']:
                return_parameters = event.processamento1(jsonObject) # 1 em referencia ao sensor 1
            else:
                event.processamento(jsonObject)
                return_parameters = None
            return return_parameters
            #event.processamento(jsonObject['id_sensor'], select_features) # 1 em referencia ao sensor 1
        else:
            print("Nenhum do casos no TRATAMENTO EVENTO 2")
