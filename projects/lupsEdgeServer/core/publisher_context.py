import requests
import datetime
import json
import sqlite3

#----------------------Link para baixar os dados do SB--------------------------
#http://localhost:8000/persistances/?format=json&publisher=False

class Publisher(object):

    #deixar variavel com url da API borda e Token

    #a publicação deve receber o servidor de contexto a ser publicado
    def publish_context(self, jsonObject):

        #com o servidor de contexto, obter URL e Token através da API
        url = 'http://exehda-dev.ufpel.edu.br/contextServer/api/publicacoes'

        url_2 = 'http://localhost:8000/sensors/'+str(jsonObject['sensor'])+'/'
        headers = {'Content-type': 'application/json', 'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}

        #utilizar aqui o Token anteriormente adquirido
        r = requests.get(url_2, headers=headers)

        uuID = r.json()['uuID']

        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")

        date_str_coleta =   jsonObject['collectDate']
        value =             jsonObject['value']


        if jsonObject['persistance'] == True:
            date_str_coleta = datetime.datetime.strptime(date_str_coleta,'%Y-%m-%dT%H:%M:%S').strftime("%Y-%m-%d %H:%M:%S")


        #o servidor de contexto necessita do uuid para publicação, deve ser recebido atraves do paramentro "sensor_uuid"
        #fazer uma nova consulta na API para requisitar o UUID do sensor em questão

        data = {"content": {"sensor_uuid":str(uuID), "datacoleta":date_str_coleta, "valorcoletado":str(value), "dispararegra":"true"}}
        headers = {'Content-type': 'application/json', 'X-API-KEY': 'cfb281929c3574091ad2a7cf80274421e6a87c59'}
        #utilizar aqui o Token anteriormente adquirido
        r = requests.post(url, data=json.dumps(data), headers=headers)

        #r = requests.post(url, data=json.dumps(data), headers=headers)
        #print(data)
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
            #self.publish_local(sensor)
            sensor['persistance'] = True

            try:
                juca = self.publish_context(sensor)
                self.publish_local(sensor)
            except:
                print("Servidor Desligado")

    def publish_to_rules(self, jsonObject):
        #print("birinha 2018")
        try:    #Se não publica no CONTEXTO, então publica na PERSISTENCIA com a flag FALSE
            juca = self.publish_context(jsonObject)
            self.set_publisher_local(jsonObject, "True")
        except Exception as inst:
            print(inst.args)
            print(type(inst))
            raise
            self.set_publisher_local(jsonObject, "False")
