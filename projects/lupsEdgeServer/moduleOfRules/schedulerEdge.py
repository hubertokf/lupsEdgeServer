
from datetime import datetime
import json
import time
import re
import os
import threading
from apscheduler.schedulers.background import BackgroundScheduler


class SchedulerEdge(object):
    #instacia do objeto e inicia o escalonador
    def __init__(self):

        def run_thread():
            while(True):
                time.sleep(1)

        self.scheduler = BackgroundScheduler() # atribui um agendador background
        self.scheduler.start() # inicia o agendador
        self.th = threading.Thread(target= run_thread) # thread executa outtro fluxo para o agendador rodar
        self.th.start()

    def add_job (self, a): # cria uma nova tarefa no escalonador
    #  analisar o modo (interval,date,cron) para executar de forma correta
        jsonObject = json.loads(a)

        if(jsonObject['modo']=='cron'):
            self.scheduler.add_job(self.tick, jsonObject['modo'], second = jsonObject['info']['second'], minute = jsonObject['info']['minute'],
            hour = jsonObject['info']['hour'], day = jsonObject['info']['day'], month = jsonObject['info']['month'], year = jsonObject['info']['year'],id = a, args = [a])
        elif(jsonObject['modo']=='interval'):
            print("ok1")
        elif(jsonObject['modo']=='date'):
            print("ok2")

    def remove_job(self, a):
        self.scheduler.remove_job(a)

    def tick(self,response):
        print(response)
