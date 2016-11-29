import json
import threading
from core.event_treatment import *
from apscheduler.schedulers.background import BackgroundScheduler


class SchedulerEdge(object):

    request_API_to_DB = None

    def __init__(self):             #instância do objeto e inicia o escalonador
        self.request_API_to_DB = Manager_conect_DB()

        self.scheduler = BackgroundScheduler()          # atribui um agendador background
        self.scheduler.start()                          # inicia o agendador

        self.create_job_check_persistence()
        self.check_scheduler_reactivave()

    def add_job(self, jsonObject): # cria uma nova tarefa no escalonador
        #print(type(jsonObject['status']))
        jsonObject['collect_to_rule'] = False
        if (jsonObject['status'] == 'True'or jsonObject['status'] == True):
            if jsonObject['id'] != '0':
                try:
                    #print('klhashjkah')
                    self.scheduler.add_job(self.function, jsonObject['modo'], second = jsonObject['second'], minute = jsonObject['minute'],
                    hour = jsonObject['hour'], day = jsonObject['day'], month = jsonObject['month'], year = jsonObject['year'], id = str(jsonObject['id']), args = [jsonObject],max_instances=20)
                except:     # Utilizado quando tem uma tarefa com ID para reescalonar
                    self.scheduler.reschedule_job(jsonObject['id'], trigger='cron', second = jsonObject['second'],  minute = jsonObject['minute'],hour = jsonObject['hour'], day = jsonObject['day'], month = jsonObject['month'], year = jsonObject['year'])

            else:
                self.scheduler.add_job(self.check_persistence, jsonObject['modo'], second = jsonObject['second'], minute = jsonObject['minute'],
                hour = jsonObject['hour'], day = jsonObject['day'], month = jsonObject['month'], year = jsonObject['year'], id = jsonObject['id'], max_instances=1)

    def remove_job(self, jsonObject):    # id_tarefa - É ID do sensor/atuador a ser removido do CRON
        self.scheduler.remove_job(jsonObject['id'])

    def function(self, jsonObject):        # response - É JSON passado como argumento

        #print(jsonObject['id'])
        #print("SENSOR ADD"+jsonObject['id_sensor'])
        object_events = Event_Treatment(self.request_API_to_DB)
        object_events.event(jsonObject)

    def check_persistence(self):# Modificar
        persistence_publisher = Publisher()
        persistence_publisher.start()

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# Adiciona uma TAREFA no CRON, tornando resposavél pela publicação no contexto
# quando não ocorreu com sucesso este ato no módulo de gathering.

    def create_job_check_persistence(self):

        job = {}

        job['modo'] = 'cron'
        job['id'] = '0'
        job['status'] = 'True'

        job['second'] = "*"
        job['minute']  = "*/10"
        job['hour'] = "*"
        job['day'] = "*"
        job['week'] = "*"
        job['month'] = "*"
        job['year'] = "*"

        self.add_job(job)

    def check_scheduler_reactivave(self):

        jsonObject = self.request_API_to_DB.get_all_scheduler()

        for dados in jsonObject:
            dados['modo'] = 'cron'
            self.add_job(dados)
