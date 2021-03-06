import requests
import json
import time
from io import BytesIO
from scheduler import  *
import threading

class Analisador_Complexo(threading.Thread):

    sensor_ant = []
    sensor_add = []
    asd = None

    def __init__(self,asd):
        threading.Thread.__init__(self)
        self.asd = asd
        self.sched = SchedulerEdge()
#----------------------Variável do OBJETO ------------------------
    def run(self):
        while True:
            if(self.asd.get_asd() == 1):
                self.verificar_DB()
                self.asd.set_asd(0);
            time.sleep(5)
# Essa variável é setada pela outra THREAD(processo "anterior"),
    #avisando que teve alteração no DB. Então fica sempre nesse laço
    #verificando essa variável.
#-----------------------------------------------------------------


    def verificar_DB(self):     # Pega todos os sensores cadastrados na API

        #-------------------Usado para pegar dados em formato JSON----------------------
        headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}
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

        teste2 = self.sensor_add
        if len(teste2) != 0:
            #print("SENSOR activa_scheduler")
            dados_sched = self.verifica_schedules()# JSON com dados, utilizado no CRONTAB

            self.activa_scheduler(dados_sched)     # Repassa os dados e cria objeto scheduler para adicionar no CRON as tarefas

    def verifica_schedules(self):   # Pega dados cadastrados em relação aos sensores, usado no CRONTAB

            #-------------------Usado para pegar dados em formato JSON----------------------
        headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}
        url = 'http://localhost:8000/schedules/?format=json'
        request = requests.get(url, headers=headers)
        jsonObject = request.json()
            #-------------------------------------------------------------------------------
        return jsonObject

    def activa_scheduler(self, dados_scheduler):
        global asd
        for sens in self.sensor_add:
            json_new = self.cria_JSON(sens,dados_scheduler) # Mescla os sensores no DB com dados do scheduler da API
            self.sched.add_job(json_new)
        self.sensor_add.clear()

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
                    print("Removeu JOB: ", sens['id'])
                    self.sched.remove_job(sens['id'])   #   <------------------------------------------------------
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

    def cria_JSON(self, sensor,dados_sched):  # Cria um JSON no formato exato que SCHEDULER
                                    # irá utilizar. QQ tratamento deve ocorrer aqui.
        job = {}
        info = {}
        for row in dados_sched:
            if row['sensor'] == sensor['id']:

                job['modo'] = "cron"
                job['id_sensor'] = str(sensor['id'])
                job['event'] = "gathering"
                job['gateway'] = sensor['gateway']

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
#-------------------------------------------------------------------------------
