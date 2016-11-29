import requests
import json as prettyJson
import datetime
from core.manager_conect_DB import *

class Communication(object):

    request_API_to_DB = None

    def __init__(self, request_API):
        self.request_API_to_DB = request_API

    def get_values_on_gatway(self, jsonObject):

        # Utilizado no gateway, porém está desativado até a implementação do mesmo no gateway
        #headers = {'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"}

        if jsonObject['collect_to_rule']:

            json_gateway = self.request_API_to_DB.get_gateway(jsonObject['gateway'])

            url = str(json_gateway['url'])+'temp?sensor=' + str(jsonObject['uuID'])

        else:
            json_gateway2 = self.request_API_to_DB.get_sensor(jsonObject['sensor'])

            json_gateway = self.request_API_to_DB.get_gateway(json_gateway2['gateway'])

            json_gateway['uuID'] = json_gateway2['uuID']
            url = str(json_gateway['url'])+'temp?sensor=' + str(json_gateway['uuID'])


        request = requests.get(url)#, headers=headers)

        information_of_sensor = request.json()

        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
        information_of_sensor['collectDate']  = date_str

        if(type(information_of_sensor['value'])=="string"):

             information_of_sensor['value'] = 1000

        return information_of_sensor

    def set_values_on_gatwat(self, jsonObject):

        print("Verificar o JSON", jsonObject)

        # if jsonObject['collect_to_rule']:
        #
        #     json_gateway = self.request_API_to_DB.get_gateway(jsonObject['gateway'])
        #
        #     url = str(json_gateway['url'])+'temp?sensor=' + str(jsonObject['uuID'])
        #
        # else:
        #     json_gateway2 = self.request_API_to_DB.get_sensor(jsonObject['sensor'])
        #
        #     json_gateway = self.request_API_to_DB.get_gateway(json_gateway2['gateway'])
        #
        #     json_gateway['uuID'] = json_gateway2['uuID']
        #     url = str(json_gateway['url'])+'temp?sensor=' + str(json_gateway['uuID'])
        #
        #
        # request = requests.get(url)#, headers=headers)
        #
        # information_of_sensor = request.json()

        # date_now = datetime.datetime.now()
        # date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
        # information_of_sensor['collectDate']  = date_str
        #
        # if(type(information_of_sensor['value'])=="string"):
        #
        #      information_of_sensor['value'] = 1000
        #
        # return information_of_sensor
