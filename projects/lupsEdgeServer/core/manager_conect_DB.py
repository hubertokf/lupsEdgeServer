
import json
import requests


class Manager_conect_DB(object):

    def check_sensor(self):
    #-------------------Usado para pegar dados em formato JSON----------------------
        headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}
        url = 'http://localhost:8000/sensors/?format=json'
        request = requests.get(url, headers=headers)
        jsonObject = request.json()
        #-------------------------------------------------------------------------------
        return jsonObject

    def check_schedules(self):
    #-------------------Usado para pegar dados em formato JSON----------------------
        headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}
        url = 'http://localhost:8000/schedules/?format=json'
        request = requests.get(url, headers=headers)
        jsonObject = request.json()
        #-------------------------------------------------------------------------------
        return jsonObject

    def get_sensor(self, id):

        headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}
        url = 'http://localhost:8000/sensors/' + str(id)
        request = requests.get(url, headers=headers)
        jsonObject = request.json()      # Possui dados do sensor

        return jsonObject

    def get_all_sensor(self):
        headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}

        url = 'http://localhost:8000/sensors/'
        request = requests.get(url, headers=headers)
        jsonObject = request.json()      # Possui dados do sensor

        return jsonObject

    def get_scheduler(self, id):
        headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}

        url = 'http://localhost:8000/schedules/' + str(id)
        request = requests.get(url, headers=headers)
        jsonObject = request.json()

        return jsonObject

    def get_all_scheduler(self):
        headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}

        url = 'http://localhost:8000/schedules/'
        request = requests.get(url, headers=headers)
        jsonObject = request.json()

        return jsonObject

    def get_gateway(self, id):
        headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}
        url = 'http://localhost:8000/gateways/' + str(id)

        request = requests.get(url, headers=headers)
        jsonObject = request.json()

        return jsonObject
