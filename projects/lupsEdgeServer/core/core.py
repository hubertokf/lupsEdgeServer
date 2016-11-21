import datetime

import bottle
import core.mtwsgi
import _thread
from core.mtbottle import *
from core.scheduler import *

#----------------------------------MAIN-----------------------------------------

class Core:
    API_url = "http://localhost:8000/"
    API_token = "878559b6d7baf6fcede17397fc390c5b9d7cbb77"

    def __init__(self):
        #asd = Asd();
        new_scheduler = SchedulerEdge()
        new_scheduler.start_process();
        #juca = Analisador_Complexo(asd)
        #juca.start()
        http_server = MTServer(new_scheduler)
        http.start()

    def API_access(self, method, model, model_id=None, data=None, param=None):
        ### Metodo para acesso a API local ###
        #retorna json de resposta
        #method é o metodo do request (get, post, put, patch)
        #model é a tabela que está acessando. (sensors, persistances)
        #model_id caso definido, refere-se ao acesso direto a um determinado elemento do banco
        #data(DICT) armazena os dados a serem enviados para o metodo
        #param(DICT) parametros para ser colocados na url. (&publisher=False)

        url  = self.API_url+model
        if (model_id != None):
            url  += str(model_id)+"/"

        headers = {'Content-type': 'application/json', 'Authorization':'token %s' % self.API_token}

        url += "?format=json"

        if (param != None):
            for key, value in param:
                url = url+"&"+key+"="+value

        if (method == "post"):
            if(data != None):
                r = requests.post(url, data=json.dumps(data), headers=headers)
            else:
                r = requests.post(url, headers=headers)
                
        elif (method == "get"):
                r = requests.get(url, headers=headers)
        elif (method == "put"):
            if(data != None):
                r = requests.put(url, data=json.dumps(data), headers=headers)
            else:
                r = requests.put(url, headers=headers)
        elif (method == "patch"):
            if(data != None):
                r = requests.patch(url, data=json.dumps(data), headers=headers)
            else:
                r = requests.patch(url, headers=headers)

        return r.json()

    
