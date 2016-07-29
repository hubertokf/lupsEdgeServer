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

    def __init__(self):             #instância do objeto e inicia o escalonador

        def run_thread():
            while(True):
                time.sleep(1)

        self.scheduler = BackgroundScheduler()          # atribui um agendador background
        self.scheduler.start()                          # inicia o agendador
        self.th = threading.Thread(target= run_thread)  # thread executa outtro fluxo para o agendador rodar
        self.th.start()

    def add_job(self, a): # cria uma nova tarefa no escalonador
    #  analisar o modo (interval,date,cron) para executar de forma correta
        jsonObject = json.loads(a)

        if(jsonObject['modo']=='cron'):
            self.scheduler.add_job(self.tick, jsonObject['modo'], second = jsonObject['info']['second'], minute = jsonObject['info']['minute'],
            hour = jsonObject['info']['hour'], day = jsonObject['info']['day'], month = jsonObject['info']['month'], year = jsonObject['info']['year'],id = a, args = [a])
        #    self.scheduler.add_job(self.tick, jsonObject['modo'], second = 0, minute = jsonObject['info']['minute'],
        #    hour = jsonObject['info']['hour'], day = jsonObject['info']['day'], month = jsonObject['info']['month'], year = jsonObject['info']['year'],id = a, args = [a])


        elif(jsonObject['modo']=='interval'):
            self.scheduler.add_job(self.tick, jsonObject['modo'], second = jsonObject['info']['second'], minute = jsonObject['info']['minute'],
            hour = jsonObject['info']['hour'], day = jsonObject['info']['day'], month = jsonObject['info']['month'], year = jsonObject['info']['year'],id = a, args = [a])

        elif(jsonObject['modo']=='date'):
            variabledate = datetime.date(int(jsonObject['info']['year']),int(jsonObject['info']['month'])
            ,int(jsonObject['info']['day']))

            self.scheduler.add_job(self.tick, jsonObject['modo'],run_time = datetime.date(variabledate),id = a, args = [a])

    def remove_job(self, a):    # a - É ID do sensor a ser removido
        self.scheduler.remove_job(a)

    def tick(self,response):    # response - É JSON passado como argumento
        object_events = Event_Treatment()
        object_events.event(1,response)
