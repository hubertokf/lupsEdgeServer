import requests
import json as prettyJson
import datetime

class GetValuesSensor(object):

    def get_values_on_gatway(self, json):
        headers = {'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"}
        #url = 'http://10.0.50.186/temp?sensor=123e4567-e89b-12d3-a456-42665544001' #+ json['uuID']
        #url = 'http://10.0.50.186/temp?sensor=' + json['uuID']
        #headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}
        url = 'http://localhost:8000/gateways/'
        request = requests.get(url, headers=headers)
        json_gateway = request.json()
        print(json_gateway)
        print(json_gateway[0]['url'])
        print("OI")

        url = str(json_gateway[0]['url'])+'temp?sensor=' + str(json['uuID'])
        print(url)
        request = requests.get(url, headers=headers)

        information_of_sensor = request.json()
        print(information_of_sensor)
        # information_of_sensor = information_of_sensor[0,36]+"\\"+ information_of_sensor[37,41]+"\\"+information_of_sensor[42,45]+"\\"+information_of_sensor[46,49]+"\\"+information_of_sensor[50,55]
        # print(information_of_sensor)
        # information_of_sensor = fuckjson.loads(information_of_sensor)
        #print(type(information_of_sensor))
        #print(information_of_sensor

        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
        information_of_sensor['collectDate']  = date_str

        if(type(information_of_sensor['value'])=="string"):

             information_of_sensor['value'] = 1000

        return information_of_sensor
