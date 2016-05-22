
from datetime import datetime
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

    def add_job (self, a):

        self.scheduler.add_job(self.tick, 'cron', second = str(a)+','+str(a*2) , id = str(a))

    def remove_job(self, a):
        self.scheduler.remove_jobe(a)

    def tick(self):
        print("okkkk")
