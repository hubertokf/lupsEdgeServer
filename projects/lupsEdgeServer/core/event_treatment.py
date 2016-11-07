#from proceeding import *
#from publisher import *
#from publisher_context import *
from core.gathering import *
import json

class Event_Treatment(object):

    def event(self, response):
        #print(response)
        jsonObject = json.loads(response)

        if jsonObject['event'] == "proceeding":
            print('Proceeding')
                #event = Proceeding()
        elif jsonObject['event'] == "publisher":
            print('Publisher')
            event = Publisher()
            event.publish_to_rules(jsonObject)
        elif jsonObject['event'] == "gathering":
            #print('Sensor: ', jsonObject['id_sensor'])
            #print('uuID: ', jsonObject['uuID'])
            event = Gathering()
            #print(jsonObject['id_sensor'])
            event.processamento(jsonObject) # 1 em referencia ao sensor 1

            #event.processamento(jsonObject['id_sensor'], select_features) # 1 em referencia ao sensor 1
        else:
            print("Nenhum do casos no TRATAMENTO EVENTO 2")
