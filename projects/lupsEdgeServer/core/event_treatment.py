from core.publisher_context import *
from core.gathering import *
import threading
import json

class Event_Treatment(object):
    core = None

    def __init__(self, parent):             #instância do objeto e inicia o escalonador
        #threading.Thread.__init__(self)
        self.core = parent

    def event(self, jsonObject):

        if jsonObject['event'] == "proceeding":
            print('Proceeding')
                #event = Proceeding(self.request_API_to_DB)

        elif jsonObject['event'] == "publisher":
            #print('Publisher')
            event = Publisher(self.core)
            # print(dir(Publisher))
            event.publish_to_rules(jsonObject)

        elif jsonObject['event'] == "gathering":
            event = Gathering(self.core)
            return_parameters = event.processamento(jsonObject) # 1 em referencia ao sensor 1
            return return_parameters
        else:
            print("Nenhum do casos no TRATAMENTO EVENTO 2")
