import requests
import datetime
import json
import sqlite3

#----------------------Link para baixar os dados do SB--------------------------
#http://localhost:8000/persistances/?format=json&publisher=False

class Publisher(object):

    def publish_context(self, jsonObject):

        url = 'http://exehda-dev.ufpel.edu.br/contextServer/api/publicacoes'

        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")

        id_sensor =         jsonObject['sensor']
        date_str_coleta =   jsonObject['collectDate']
        value =             jsonObject['value']

        date_aux = datetime.datetime.strptime(date_str_coleta,'%Y-%m-%dT%H:%M:%S').strftime("%Y-%m-%d %H:%M:%S")

        data = {"content": {"sensor_id":str(id_sensor), "datacoleta":date_aux, "valorcoletado":str(value), "dispararegra":"true"}}
        headers = {'Content-type': 'application/json', 'X-API-KEY': 'cfb281929c3574091ad2a7cf80274421e6a87c59'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

        #r = requests.post(url, data=json.dumps(data), headers=headers)
        #print(r.text)
        return r.text



    def publish_local(self, jsonObject):  # Altera a flag para TRUE ao publicar no CONTEXTO
        headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}

        payload = {'publisher': True}

        r = requests.patch("http://localhost:8000/persistances/"+str(jsonObject['id'])+"/", data=payload, headers=headers)
    #------------------------------------------------------------------------------------------------------------------------



    def set_publisher_local(self, jsonObject, flag): # Publica na PERSISTENCIA

        headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}
        #print("---------------"+id_sensor+"------------------------")

        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")

        id_sensor =         jsonObject['sensor']
        date_str_coleta =   date_str
        value =             jsonObject['value']

        payload = {'collectDate': date_str, 'value': str(value), 'sensor': str(id_sensor), 'contextServer':'1', 'publisher': str(flag)}

        r = requests.post("http://localhost:8000/persistances/", data=payload, headers=headers)

        #print(r.text)

    def get_dados_SB(self):
        headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}
        url = 'http://localhost:8000/persistances/?format=json&publisher=False'
        request = requests.get(url, headers=headers)
        jsonObject = request.json()

        return jsonObject

    def start(self):
        dados_sensores = self.get_dados_SB()

        for sensor in dados_sensores:
            self.publish_local(sensor)
            try:
                juca = self.publish_context(sensor)
                self.publish_local(sensor)
                #flag TRUE
            except:
                #flag FALSE
                print("Servidor Desligado")

    def publish_to_rules(self, jsonObject):
        print("birinha 2018")
        try:    #Se não publica no CONTEXTO, então publica na PERSISTENCIA com a flag FALSE
            juca = self.publish_context(jsonObject)
            self.set_publisher_local(jsonObject, "True")
        except Exception as inst:
            print(inst.args)
            print(type(inst))
            raise
            self.set_publisher_local(jsonObject, "False")
