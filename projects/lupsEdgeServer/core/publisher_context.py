import requests
import datetime
import json
import sqlite3

#----------------------Link para baixar os dados do SB--------------------------
#http://localhost:8000/persistances/?format=json&publisher=False

class Publisher(object):

    #deixar variavel com url da API borda e Token
    core = None

    def __init__(self, parent):             #instância do objeto e inicia o escalonador

        self.core = parent

    #a publicação deve receber o servidor de contexto a ser publicado
    def publish_context(self, jsonObject):

        #com o servidor de contexto, obter URL e Token através da API
        #url = 'http://exehda-dev.ufpel.edu.br/contextServer/api/publicacoes'

        #trocar isso aqui quando receber o servidor de contexto a ser publicado
        context = self.core.API_access("get", "contextServers").json()[0]

        #utilizar aqui o Token anteriormente adquirido
        sensor = self.core.API_access("get", "sensors", model_id=str(jsonObject['sensor'])).json()


        uuID = sensor['uuID']

        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")

        date_str_coleta =   jsonObject['collectDate']
        value =             jsonObject['value']


        if jsonObject['persistance'] == True:
            date_str_coleta = datetime.datetime.strptime(date_str_coleta,'%Y-%m-%dT%H:%M:%S').strftime("%Y-%m-%d %H:%M:%S")


        #o servidor de contexto necessita do uuid para publicação, deve ser recebido atraves do paramentro "sensor_uuid"
        #fazer uma nova consulta na API para requisitar o UUID do sensor em questão

        data = {"content": {"sensor_uuid":str(uuID), "datacoleta":date_str_coleta, "valorcoletado":str(value), "dispararegra":"true"}}
        headers = {'Content-type': 'application/json', 'X-API-KEY': context['accessToken']}
        #utilizar aqui o Token anteriormente adquirido
        #print(context['addressUrl']+"publicacoes/")

        try:
            context_publication = requests.post(context['addressUrl']+"publicacoes/", data=json.dumps(data), headers=headers)
            return context_publication.text
        except:
            print("OCORREU ERRO AO PUBLICAR NO SERVIDOR DE CONTEXTO")
            return None
        #r = requests.post(url, data=json.dumps(data), headers=headers)
        #print(data)
        #print(r.text)
        #return context_publication.text


    def publish_local(self, jsonObject):  # Altera a flag para TRUE ao publicar no CONTEXTO
        data = {'publisher': True}

        r = self.core.API_access("patch", "persistances", str(jsonObject['id']), data).json()

    #------------------------------------------------------------------------------------------------------------------------



    def set_publisher_local(self, jsonObject, flag): # Publica na PERSISTENCIA

        #print("---------------"+id_sensor+"------------------------")

        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")

        id_sensor =         jsonObject['sensor']
        date_str_coleta =   date_str
        value =             jsonObject['value']

        data = {'collectDate': date_str, 'value': str(value), 'sensor': str(id_sensor), 'contextServer':'1', 'publisher': str(flag)}

        r = self.core.API_access("post", "persistances", model_id=None, data=data, param=None).json()

        #print(r.text)

    def get_dados_SB(self):
        param = {"publisher":"False"}
        jsonObject = self.core.API_access("get", "persistances", model_id=None, data=None, param=param).json()

        return jsonObject

    def start(self):
        dados_sensores = self.get_dados_SB()
        #print("START")

        for sensor in dados_sensores:
            #self.publish_local(sensor)
            #sensor["persistance"] = True

            try:
                #print("TRY")
                juca = self.publish_context(sensor)
                #sensor['persistance'] = True
                #print(juca)
                self.publish_local(sensor)
                #print("TRY")
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
