import requests
import json as prettyJson

class GetValuesSensor(object):

    def get_values_on_gatway(self, json):
        headers = {'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"}
        #url = 'http://10.0.50.186/temp?sensor=123e4567-e89b-12d3-a456-42665544001' #+ json['uuID']
        url = 'http://10.0.50.186/temp?sensor=' + json['uuID']
        request = requests.get(url, headers=headers)

        information_of_sensor = request.json()
        # information_of_sensor = information_of_sensor[0,36]+"\\"+ information_of_sensor[37,41]+"\\"+information_of_sensor[42,45]+"\\"+information_of_sensor[46,49]+"\\"+information_of_sensor[50,55]
        # print(information_of_sensor)
        # information_of_sensor = fuckjson.loads(information_of_sensor)
        #print(type(information_of_sensor))

        if(type(information_of_sensor['value'])=="string"):

             information_of_sensor['value'] = 1000

        return information_of_sensor
