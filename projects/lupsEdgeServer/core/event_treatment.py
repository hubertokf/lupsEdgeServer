#from core.proceeding import *
#from core.publisher import *
from core.publisher_context import *
from core.gathering import *
import json

class Event_Treatment(object):

    def event(self, jsonObject):
        #print(response)
        #jsonObject = json.loads(response)
        # print(jsonObject)
        if jsonObject['event'] == "proceeding":
            print('Proceeding')
                #event = Proceeding()
                
        elif jsonObject['event'] == "publisher":
            print('Publisher')
            event = Publisher()
            # print(dir(Publisher))
            event.publish_to_rules(jsonObject)

        elif jsonObject['event'] == "gathering":

            event = Gathering()
            return_parameters = event.processamento(jsonObject) # 1 em referencia ao sensor 1

            return return_parameters
        else:
            print("Nenhum do casos no TRATAMENTO EVENTO 2")
