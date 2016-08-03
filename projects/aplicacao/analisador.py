import requests
import json
import time
from io import BytesIO
from scheduler import  *

class Analisador_Complexo(object):

    sensor_ant = []
    sensor_add = []

    def __init__(self):
        self.sched = SchedulerEdge()
        asd = 0
        while True:
            if(asd == 1):
                self.verificar_DB()
                asd=0
            time.sleep(5)


    def verificar_DB(self):     # Pega todos os sensores cadastrados na API

        #-------------------Usado para pegar dados em formato JSON----------------------
        headers = {'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"}
        url = 'http://localhost:8000/sensors/?format=json'
        request = requests.get(url, headers=headers)
        jsonObject = request.json()
        #-------------------------------------------------------------------------------

        # JSONOBJECT é um vetor de todos os sensors cadastrados, então o FOR percorre
        # cada posição do mesmo, transmitindo essas informações ao SCHEDULER
        sensors_atual = []

        for row in jsonObject:
            b = row['id']
            sensors_atual.append(row)

        self.compara_DB(sensors_atual)         # Repassa um JSON com todos os dados de sensores cadastrados "NOVOS"

        dados_sched = self.verifica_schedules()# JSON com dados, utilizado no CRONTAB

        self.activa_scheduler(dados_sched)     # Repassa os dados e cria objeto scheduler para adicionar no CRON as tarefas

    def verifica_schedules(self):   # Pega dados cadastrados em relação aos sensores, usado no CRONTAB

            #-------------------Usado para pegar dados em formato JSON----------------------
        headers = {'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"}
        url = 'http://localhost:8000/schedules/?format=json'
        request = requests.get(url, headers=headers)
        jsonObject = request.json()
            #-------------------------------------------------------------------------------
        return jsonObject

    def activa_scheduler(self, dados_scheduler):
        global asd
        for sens in self.sensor_add:
            json_new = self.cria_JSON(sens,dados_scheduler) # Mescla os sensores no DB com dados do scheduler da API
            #if asd > 2:
            self.sched.add_job(json_new)        #           <----------------------
            self.sensor_add.remove(sens)
            #asd = asd + 1


        #print("-----------PASSOUUU----------")


    def compara_DB(self, dados):
        global sensor_ant
        global sensor_add
        not_existe = 1
        existe = 0
        teste = self.sensor_ant

        if len(teste) == 0:
            #print('TABELA VAZIA')
            for row in dados:
                self.sensor_ant.append(row)
                self.sensor_add.append(row)
                #print(row)

        else:
            #print('TABELA COM DADOS')
            # sensor_ant -> Cadastrado do sensores que estão rodando no CRON
            # dados -> Sensores que estão no DB
            #-------------------Deleta os sensores na tabela antiga-----------------
            for sens in self.sensor_ant:
                for row in dados:
                    if sens['id'] == row['id']:
                        #print('Sensores iguais')
                        #print('Sensores iguais: ')
                        #print(row['id'])
                        not_existe = 0
                if not_existe == 1:    # remover em relação ao ID, pois é único
                    self.sched.remove_job(sens['id'])
                    self.sensor_ant.remove(sens)
                not_existe = 0
        #-----------------------------------------------------------------------

        #-------------Adiciona sensores não cadastrados no CRON-----------------
            for row in dados:
                for sens in self.sensor_ant:
                    if row['id'] == sens['id']:
                        existe = 1

                if existe == 0:
                    #print('Sensor adicionado: ')
                    #print(row['id'])
                    self.sensor_ant.append(row)
                    self.sensor_add.append(row)
                existe = 0
        #-----------------------------------------------------------------------


        #print("\n---------------------")

    def cria_JSON(self, sensor,dados_sched):  # Cria um JSON no formato exato que SCHEDULER
                                    # irá utilizar. QQ tratamento deve ocorrer aqui.
        job = {}
        info = {}
        for row in dados_sched:
            if row['sensor'] == sensor['id']:

                job['modo'] = "cron"
                job['id_sensor'] = str(sensor['id'])
                job['event'] = "gathering"

                info['second'] = str("*/"+row['cron'])
                info['minute']  = "*"
                info['hour'] = "*"
                info['day'] = "*"
                info['week'] = "*"
                info['month'] = "*"
                info['year'] = "*"

                job['info'] = info
            #print(json.dumps(job))
        return json.dumps(job)
#-------------------------------------------------------------------------------
    def set_add(self, valor):
        global asd
        asd = valor
#-------------------------------------------------------------------------------
