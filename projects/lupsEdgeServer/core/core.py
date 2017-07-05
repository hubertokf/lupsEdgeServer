import datetime

import bottle
import core.mtwsgi
import _thread
from core.mtbottle import *
from core.scheduler import *
from core.subscriber_mqtt import *

#----------------------------------MAIN-----------------------------------------

class Core:
    API_url = "http://localhost:8000/"
    API_token = "03986a715b41657a909e8ab66ba800d6fdea7f71"

    def __init__(self):
        #asd = Asd();
        # Comentar a funcionalidade
        new_scheduler = SchedulerEdge(self)
        #juca = Analisador_Complexo(asd)

        # Verifica os TOPICOS existentes nas regras, criando o canal de comunicação
        # referente a esses TOPICOS.
        # Quando recebe mensagens, encaminha os dados ao motor de regras
        new_subscriber = Subscriber(self)
        #juca.start()
        http_server = MTServer(new_scheduler, new_subscriber)
        http.start()

    def API_access(self, method, model, model_id=None, data=None, param=None):
        ### Metodo para acesso a API local ###
        #retorna json de resposta
        #method é o metodo do request (get, post, put, patch)
        #model é a tabela que está acessando. (sensors, persistances)
        #model_id caso definido, refere-se ao acesso direto a um determinado elemento do banco
        #data(DICT) armazena os dados a serem enviados para o metodo
        #param(DICT) parametros para ser colocados na url. (&publisher=False)

        url  = self.API_url+model+"/"
        if (model_id != None):
            url  += str(model_id)+"/"

        url += "?format=json"

        if (param != None):
            for key, value in param.items():
                url = url+"&"+str(key)+"="+str(value)

        method = getattr(self, "_api_access_"+method)
        return method(url, data)

    def _api_access_post(self, url, data):
        headers = {'Content-type': 'application/json', 'Authorization':'token %s' % self.API_token}

        if(data != None):
            r = requests.post(url, data=json.dumps(data), headers=headers)
        else:
            r = requests.post(url, headers=headers)

        return r

    def _api_access_get(self, url, data):
        headers = {'Content-type': 'application/json', 'Authorization':'token %s' % self.API_token}

        r = requests.get(url, headers=headers)

        return r

    def _api_access_put(self, url, data):
        headers = {'Content-type': 'application/json', 'Authorization':'token %s' % self.API_token}

        if(data != None):
            r = requests.put(url, data=json.dumps(data), headers=headers)
        else:
            r = requests.put(url, headers=headers)

        return r

    def _api_access_patch(self, url, data):
        headers = {'Content-type': 'application/json', 'Authorization':'token %s' % self.API_token}

        if(data != None):
            r = requests.patch(url, data=json.dumps(data), headers=headers)
        else:
            r = requests.patch(url, headers=headers)

        return r
