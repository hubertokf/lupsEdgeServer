import requests
import json as prettyJson
import datetime
from core.manager_conect_DB import *

class Communication(object):

    core = None

    def __init__(self, parent):
        self.core = parent

    def get_values_on_gatway(self, jsonObject):

        # Utilizado no gateway, porém está desativado até a implementação do mesmo no gateway
        #headers = {'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"}

        if jsonObject['collect_to_rule']:

            jsonGateway = self.core.API_access("get", "gateways", model_id=jsonObject['gateway']).json()

            #url = str(jsonGateway['url'])+'sensor/?uuId=' + str(jsonObject['uuID'])
            url = str(jsonGateway['url'])+'sensor=' + str(jsonObject['uuID'])

        else:
            json_gateway2 = self.core.API_access("get", "sensors", model_id=jsonObject['sensor']).json()

            json_gateway = self.core.API_access("get", "gateways", model_id=json_gateway2['gateway']).json()

            json_gateway['uuID'] = json_gateway2['uuID']
            #url = str(json_gateway['url'])+'sensor/?uuId=' + str(json_gateway['uuID'])
            url = str(json_gateway['url'])+'sensor=' + str(json_gateway['uuID'])

        try:
            request = requests.get(url)#, headers=headers)
            #print(url)
            #print(request)
            information_of_sensor = request.json()

            date_now = datetime.datetime.now()
            date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
            information_of_sensor['collectDate']  = date_str

            if(type(information_of_sensor['value'])=="string"):

                information_of_sensor['value'] = 1000

            return information_of_sensor

        except requests.exceptions.ConnectionError:
            print("GATWAY OFFLINE")
            return None

        except:
            print("ERRO NO COMMUNICATION - VERIFICAR TIPO DE ERRO")
            return None
            

        

    def set_values_on_gatwat(self, jsonObject):

        #print("Verificar o JSON", jsonObject)

        if jsonObject['collect_to_rule']:

            jsonGateway = self.core.API_access("get", "gateways", model_id=jsonObject['gateway']).json()

            url = str(jsonGateway['url'])+'actuator/' + str(jsonObject['uuID'])

        else:
            json_gateway2 = self.core.API_access("get", "sensors", model_id=jsonObject['sensor']).json()

            json_gateway = self.core.API_access("get", "gateways", model_id=json_gateway2['gateway']).json()

            json_gateway['uuID'] = json_gateway2['uuID']
            url = str(json_gateway['url'])+'actuator/' + str(json_gateway['uuID'])


        request = requests.get(url)#, headers=headers)

        information_of_sensor = request.json()

        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
        information_of_sensor['collectDate']  = date_str

        if(type(information_of_sensor['value'])=="string"):

             information_of_sensor['value'] = 1000

        return information_of_sensor
