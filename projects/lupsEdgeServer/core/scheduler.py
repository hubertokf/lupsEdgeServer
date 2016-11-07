from datetime import datetime
import json
import time
import re
import os
import threading
import pycurl
from array import array
from io import BytesIO
from core.event_treatment import *
from apscheduler.schedulers.background import BackgroundScheduler
from core.publish_context import *


class SchedulerEdge(object):

    sensor_ant = []
    sensor_add = []
    scheduler_data_ant = []

    def __init__(self):             #instância do objeto e inicia o escalonador

        def run_thread():
            while(True):
                time.sleep(1)

        self.scheduler = BackgroundScheduler()          # atribui um agendador background
        self.scheduler.start()                          # inicia o agendador
        self.th = threading.Thread(target= run_thread)  # thread executa outtro fluxo para o agendador rodar
        self.th.start()

    def add_job(self, a): # cria uma nova tarefa no escalonador
        jsonObject = json.loads(a)

        #print(jsonObject['id_sensor'])

        if(jsonObject['modo']=='cron'):
            self.scheduler.add_job(self.function, jsonObject['modo'], second = jsonObject['info']['second'], minute = jsonObject['info']['minute'],
            hour = jsonObject['info']['hour'], day = jsonObject['info']['day'], month = jsonObject['info']['month'], year = jsonObject['info']['year'],id = jsonObject['id_sensor'], args = [a],max_instances=3)

        elif(jsonObject['modo']=='publish'):    #Modificar function a chamar!
            self.scheduler.add_job(self.function_publisher, jsonObject['modo'], second = jsonObject['info']['second'], minute = jsonObject['info']['minute'],
            hour = jsonObject['info']['hour'], day = jsonObject['info']['day'], month = jsonObject['info']['month'], year = jsonObject['info']['year'],id = jsonObject['id_sensor'], args = [a],max_instances=1)


    def remove_job(self, id_tarefa):    # id_tarefa - É ID do sensor/atuador a ser removido do CRON
        teste = str(id_tarefa)
        self.scheduler.remove_job(teste)

    def function(self,response):        # response - É JSON passado como argumento
        jsonObject = json.loads(response)
        object_events = Event_Treatment()
        object_events.event(response)

    def function_publisher(self,response):# Modificar
        publicador = Publisher()
        publicador.start()

        #jsonObject = json.loads(response)
        #object_events = Event_Treatment()
        #object_events.event(response)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

    def start_process(self):
        global scheduler_data_ant

        sensors_data = self.check_sensor()
        scheduler_data = self.check_schedules()

        sensors_actual = []

        for sensor in sensors_data:
            id_sensor = sensor['id']
            sensors_actual.append(sensor)

        self.compara_DB(sensors_actual)         # Repassa um JSON com todos os dados de sensores cadastrados "NOVOS"

        aux_sensor_add = self.sensor_add

        if len(aux_sensor_add) != 0:            # Por algum motivo não funciona colocando direto o "self.sensor_add"
                                                            #                oO
            self.activa_scheduler(scheduler_data)     # Repassa os dados e cria objeto scheduler para adicionar no CRON as tarefas
        else:                                   # Teve modificação apenas no scheduler, sem add ou remove sensor/atuador
            self.measure_schedulers(scheduler_data_ant, scheduler_data, sensors_data)

        scheduler_data_ant = scheduler_data
        #print("------------------------------------------------------")
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


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

    def compara_DB(self, dados):
        global sensor_ant
        global sensor_add
        sensor_remove = []
        add = 0
        not_existe = 1
        existe = 0
        teste = self.sensor_ant

        if len(teste) == 0:         # Quando nenhuma JOB está no CRON
            for row in dados:
                add = add +1
                self.sensor_ant.append(row)
                self.sensor_add.append(row)

        else:                       # Quando já possui JOBs no CRON
            # sensor_add -> Sensores que serão add no CRON, após add a tab fica vazia
            # sensor_ant -> Sensores que estão rodando no CRON
            # dados -> Sensores que estão no DB
            #-------------------Deleta os sensores na tabela antiga-----------------
            for sens in self.sensor_ant:
                for row in dados:
                    if sens['id'] == row['id']:
                        not_existe = 0
                if not_existe == 1:    # remover em relação ao ID, pois é único
                    #print("Removeu JOB: ", sens['id'])
                    self.remove_job(sens['id'])   #   <------------------------------------------------------
                    sensor_remove.append(sens)

                not_existe = 1
        #-----------------------------------------------------------------------
            ##---------REMOVE SENSORES DA TABELA ANTIGA-------------------------
            for sens_r in sensor_remove:
                self.sensor_ant.remove(sens_r)
            sensor_remove.clear()
            #-------------------------------------------------------------------


        #-------------Adiciona sensores não cadastrados no CRON-----------------
            for row in dados:
                for sens in self.sensor_ant:
                    if row['id'] == sens['id']:
                        existe = 1

                if existe == 0:
                    self.sensor_ant.append(row)
                    self.sensor_add.append(row)
                existe = 0
        #-----------------------------------------------------------------------

    def activa_scheduler(self, dados_scheduler):
        global sensor_add

        for sens in self.sensor_add:
            json_new = self.create_JSON(sens,dados_scheduler) # Mescla os sensores no DB com dados do scheduler da API
            if json_new !=0:
                self.add_job(json_new)  #   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.sensor_add.clear()


    def create_JSON(self, sensor,dados_sched):  # Cria um JSON no formato exato que SCHEDULER
                                    # irá utilizar. QQ tratamento deve ocorrer aqui.
        job = {}
        info = {}
        for row in dados_sched:
            if row['sensor'] == sensor['id']:
                #print("-------------"+str(sensor['id'])+"-------------")

                job['modo'] = "cron"
                job['id_sensor'] = str(sensor['id'])
                job['uuID'] = str(sensor['uuID'])
                job['event'] = "gathering"
                job['id_gateway'] = sensor['gateway']

                info['second'] = "*/{}".format(row['minute'])
                info['minute']  = "*"
                info['hour'] = "*"
                info['day'] = "*"
                info['week'] = "*"
                info['month'] = "*"
                info['year'] = "*"

                job['info'] = info
                #print(job)
                return json.dumps(job)
        return 0;
#-------------------------------------------------------------------------------
    def measure_schedulers(self, sched_data_old, sched_data_new, sensors_data):
        aux_variable = 0

        for data_new in sched_data_new:
            for data_old in sched_data_old:
                if data_old['minute'] == data_new['minute']:
                    aux_variable = 1

            for data_sens in sensors_data:
                if str(data_new['sensor']) == str(data_sens['id']):
                    sensor = data_sens

            if aux_variable == 0:   # Chamar o NEW_JSON para ADD no CRON
                self.remove_job(sensor['id'])
                json_new = self.create_JSON(sensor, sched_data_new)

                self.add_job(json_new)          #   <<<<<<<<<<<<<<<<<<<<<<<<<<<<

            aux_variable = 0

#-------------------------------------------------------------------------------

# Adiciona uma TAREFA no CRON, tornando resposavél pela publicação no contexto
# quando não ocorreu com sucesso este ato no módulo de gathering.

    def add_publish(self):

        job = {}
        info = {}

        job['modo'] = "publish"
        job['id_sensor'] = "0"
        job['uuID'] = "juca"
        job['event'] = ""
        job['id_gateway'] = "0"

        info['second'] = "*"
        info['minute']  = "*/10"
        info['hour'] = "*"
        info['day'] = "*"
        info['week'] = "*"
        info['month'] = "*"
        info['year'] = "*"

        job['info'] = info

        self.add_job(json.dumps(job))
                #print(job)
                #return json.dumps(job)
