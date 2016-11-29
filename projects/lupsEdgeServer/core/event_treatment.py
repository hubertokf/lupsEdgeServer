from core.publisher_context import *
from core.gathering import *
import json

class Event_Treatment(object):

    request_API_to_DB = None

    def __init__(self, request_API):
        self.request_API_to_DB = request_API

    def event(self, jsonObject):

        if jsonObject['event'] == "proceeding":
            print('Proceeding')
                #event = Proceeding(self.request_API_to_DB)

        elif jsonObject['event'] == "publisher":
            print('Publisher')
            event = Publisher()
            # print(dir(Publisher))
            event.publish_to_rules(jsonObject)

        elif jsonObject['event'] == "gathering":

            event = Gathering(self.request_API_to_DB)
            return_parameters = event.processamento(jsonObject) # 1 em referencia ao sensor 1

            return return_parameters
        else:
            print("Nenhum do casos no TRATAMENTO EVENTO 2")
