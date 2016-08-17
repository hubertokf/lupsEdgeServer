import requests

class GetValuesSensor(object):

    def get_values_on_gatway(self):
        headers = {'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"}
        url = 'http://10.0.50.186/temp?sensor=1'
        request = requests.get(url, headers=headers)
        information_of_sensor = request.json()
        if(type(information_of_sensor['value'])=="string"):

            information_of_sensor['value'] = 1000

        return information_of_sensor
