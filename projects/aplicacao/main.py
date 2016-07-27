import requests
import json
import time
from io import BytesIO

sensor_ant = []

def verificar_DB():

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

    compara_DB(sensors_atual)

def compara_DB(dados):

    not_existe = 1
    #for row in dados:
    #    for sens in sensor_ant:
    #        if row['id'] == sens:
    #            existe = 1
    #    if existe == 0:
    #        sensor_ant.append(row)
    #        print(row)


    if len(sensor_ant) == 0:
        print('TABELA VAZIA')
        for row in dados:
            sensor_ant.append(row)
            print(row)

    else:
        print('TABELA COM DADOS')
        for sens in sensor_ant:
            #print(sens['id'])
            for row in dados:
                if sens['id'] == row['id']:
                    print('Sensores iguais')
                    not_existe = 0

            if not_existe == 1:
                print("Sensor removido")
            #    sensor_ant.remove(sens)
            #    not_existe = 0
            #else:
            #    print("Sensor novo cadastrado")
            #    sensor_ant.append(row)
                #print(row)

    #for sens in sensor_ant:
    #    print(sens['id'])

    print("\n---------------------")

# Gravar esses dados em algum lugar, pois quando tiver alteração no DB deve
# ocorrer uma comparação para alterar os eventos agendados(Scheduler)

while True:
    verificar_DB()
    time.sleep(5)
