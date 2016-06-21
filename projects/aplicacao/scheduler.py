from datetime import datetime
import json
import time
import re
import os
import threading
import pycurl
from array import array
from io import BytesIO
from event_treatment import *
from apscheduler.schedulers.background import BackgroundScheduler


class SchedulerEdge(object):
    #instacia do objeto e inicia o escalonador

    def __init__(self):
        #self.verifica_sensores()

        def run_thread():
            while(True):
                time.sleep(1)

        self.scheduler = BackgroundScheduler() # atribui um agendador background
        self.scheduler.start() # inicia o agendador
        self.th = threading.Thread(target= run_thread) # thread executa outtro fluxo para o agendador rodar
        self.th.start()

        #def verifica_DB():
        #    print("Aqui")
        self.verifica_sensores()

    def add_job(self, a): # cria uma nova tarefa no escalonador
    #  analisar o modo (interval,date,cron) para executar de forma correta
        jsonObject = json.loads(a)

        if(jsonObject['modo']=='cron'):
            self.scheduler.add_job(self.tick, jsonObject['modo'], second = jsonObject['info']['second'], minute = jsonObject['info']['minute'],
            hour = jsonObject['info']['hour'], day = jsonObject['info']['day'], month = jsonObject['info']['month'], year = jsonObject['info']['year'],id = a, args = [a])

        elif(jsonObject['modo']=='interval'):
            self.scheduler.add_job(self.tick, jsonObject['modo'], second = jsonObject['info']['second'], minute = jsonObject['info']['minute'],
            hour = jsonObject['info']['hour'], day = jsonObject['info']['day'], month = jsonObject['info']['month'], year = jsonObject['info']['year'],id = a, args = [a])

        elif(jsonObject['modo']=='date'):
            variabledate = datetime.date(int(jsonObject['info']['year']),int(jsonObject['info']['month'])
            ,int(jsonObject['info']['day']))

            self.scheduler.add_job(self.tick, jsonObject['modo'],run_time = datetime.date(variabledate),id = a, args = [a])

    def remove_job(self, a):
        self.scheduler.remove_job(a)

    def tick(self,response):
        object_events = Event_Treatment()
        object_events.event(response)
        #print(response)

    def verifica_sensores(self):    # Verifica os sensores cadastrados no DB, colocando-os em uma tabela para
        print("Entrou")                            #       comparar quando ocorrer modificaçõe no DB. Dessa forma, é possivel
        buffer = BytesIO()          #       adicionar ou remover novos sensores em tempo de execução.
        c = pycurl.Curl()
        c.setopt(c.URL, 'http://localhost:8000/sensors/?format=json')   # Local onde se encontra todos os sensores
        c.setopt(c.WRITEDATA, buffer)                                   #       cadastrados no DB
        c.perform()
        c.close()

        body = buffer.getvalue()
        # Body is a byte string.
        # We have to know the encoding in order to print it to a text file
        # such as standard output.
        jsonObject = json.loads(body.decode('iso-8859-1'))

        i=0
        j=0
        lista_sensores = []
        for row in jsonObject:      # Pega todos os links referente a cada sensor cadastrado
            print(row['url'])
                                    # Coloca em uma tabela como a finalidade que foi descrita
            ##self.tab_temp[i] = row['url']
            lista_sensores.insert(i,row['url'])
            #lista_sensores.append(row['url'])
            i=i+1

        #print(lista_sensores)
        #teste = lista_sensores[0]
        #print(teste)
        tab_permanente = []

        if len(tab_permanente):             # Se tiver algo na tabela, ocorre atualização dos dispositivos
            for j in range(i):      #       no T_EVENTO
                print("tabela permanente existe")            # Criar uma função para comparar as tabelas || talvez uma fila

        else:
            for w in lista_sensores:
                tab_permanente.insert(j,lista_sensores[j])
                #Chamar um metodo para retornar um json.
                print("Json sensor", j)
#-------------------------------------------------------------------------------
                buffer = BytesIO()          #       adicionar ou remover novos sensores em tempo de execução.
                c = pycurl.Curl()
                c.setopt(c.URL, lista_sensores[j])   # Local onde se encontra todos os sensores
                c.setopt(c.WRITEDATA, buffer)                                   #       cadastrados no DB
                c.perform()
                c.close()

                body = buffer.getvalue()
                jsonObject = json.loads(body.decode('iso-8859-1'))
                print(jsonObject)
#-------------------------------------------------------------------------------

                self.add_job(body.decode('iso-8859-1'))
                j=j+1
            #self.add_job('{ "modo": "cron", "info": {"second": "*/5", "minute": "*", "hour": "*", "day": "*", "week": "*", "month": "*", "year": "*"	}, "id_sensor_virtual": "21231214", "id_sensor": "18", "event": "publish"}')

    #    for w in tab_permanente:
    #        print(w)
