import requests
import json
import time
from io import BytesIO
from scheduler import  *

sensor_ant = []


def verificar_DB():     # Pega todos os sensores cadastrados na API

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

    compara_DB(sensors_atual)         # Repassa um JSON com todos os dados de sensores cadastrados "NOVOS"

    dados_sched = verifica_schedules()# JSON com dados, utilizado no CRONTAB

    activa_scheduler(dados_sched)     # Repassa os dados e cria objeto scheduler para adicionar no CRON as tarefas

def verifica_schedules():   # Pega dados cadastrados em relação aos sensores, usado no CRONTAB

    #-------------------Usado para pegar dados em formato JSON----------------------
    headers = {'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"}
    url = 'http://localhost:8000/schedules/?format=json'
    request = requests.get(url, headers=headers)
    jsonObject = request.json()
    #-------------------------------------------------------------------------------
    return jsonObject

def activa_scheduler(dados_scheduler):
    global asd
    for sens in sensor_ant:
        json_new = cria_JSON(sens,dados_scheduler) # Mescla os sensores no DB com dados do scheduler da API
        if asd < 2:
            sched.add_job(json_new)
            asd = asd + 1

    print("-----------PASSOUUU----------")


def compara_DB(dados):

    not_existe = 1
    existe = 0

    if len(sensor_ant) == 0:
        print('TABELA VAZIA')
        for row in dados:
            sensor_ant.append(row)
            #print(row)

    else:
        print('TABELA COM DADOS')
        # sensor_ant -> Cadastrado do sensores que estão rodando no CRON
        # dados -> Sensores que estão no DB
        #-------------------Deleta os sensores na tabela antiga-----------------
        for sens in sensor_ant:
            for row in dados:
                if sens['id'] == row['id']:
                    print('Sensores iguais')
                    #print('Sensores iguais: ')
                    #print(row['id'])
                    not_existe = 0

            if not_existe == 1:     # Chamar o método do scheduler para remover o sensor do cron
                print("Sensor removido")    # remover em relação ao ID, pois é único
                #sched.remove_job(sens['id'])
                sensor_ant.remove(sens)
            not_existe = 0
        #-----------------------------------------------------------------------

        #-------------Adiciona sensores não cadastrados no CRON-----------------
        for row in dados:
            for sens in sensor_ant:
                if row['id'] == sens['id']:
                    existe = 1

            if existe == 0:
                print('Sensor adicionado: ')
                #print(row['id'])
                sensor_ant.append(row)
            existe = 0
        #-----------------------------------------------------------------------


    print("\n---------------------")

def cria_JSON(sensor,dados_sched):  # Cria um JSON no formato exato que SCHEDULER
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

sched = SchedulerEdge()
asd = 0
while True:
    verificar_DB()
    time.sleep(5)
