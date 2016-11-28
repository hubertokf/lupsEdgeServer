import requests
import json as prettyJson
import datetime
from core.manager_conect_DB import *

class GetValuesSensor(object):

    def get_values_on_gatway(self, json):
        headers = {'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"}
        conect_db = Manager_conect_DB()

        #------Acessa o sensor para descbrir o GATEWAY que está vinculado-------
        # if json['collect_to_rule'] == False:
        #
        #     json_gateway2 = conect_db.get_sensor(json['sensor'])

        #-----------------------------------------------------------------------


        #-------Acessa o gateways cadastrados, pegando a URL do GATEWAY

        print(json)

        if json['collect_to_rule']:
            json_gateway = conect_db.get_gateway(json['gateway'])

            url = str(json_gateway['url'])+'temp?sensor=' + str(json['uuID'])

            # print("--------------------------------------")
            # print(json_gateway)
            # print("++++++++++++++++++++++++++++++++++++++")
        else:
            json_gateway2 = conect_db.get_sensor(json['sensor'])
            json_gateway = conect_db.get_gateway(json_gateway2['gateway'])

            json_gateway['uuID'] = json_gateway2['uuID']
            url = str(json_gateway['url'])+'temp?sensor=' + str(json_gateway['uuID'])



        # print("--------------------------------------")
        # print(json_gateway)
        # print("++++++++++++++++++++++++++++++++++++++")
        #-----------------------------------------------------------------------

        #url = str(json_gateway['url'])+'temp?sensor=' + str(json_gateway['uuID'])



        request = requests.get(url, headers=headers)

        information_of_sensor = request.json()

        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
        information_of_sensor['collectDate']  = date_str

        if(type(information_of_sensor['value'])=="string"):

             information_of_sensor['value'] = 1000

        return information_of_sensor
