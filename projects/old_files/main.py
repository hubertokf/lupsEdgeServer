import datetime

import bottle
import core.mtwsgi
import _thread
from core.mtbottle import *
from core.scheduler import *


#---------------------Objeto compartilhado entre as THREADS---------------------
#class Asd(object):
#    def __init__(self):
#        self.asd = 1
#
#    def set_asd(self, val):
#        self.asd = val
#
#    def get_asd(self):
#        return self.asd
#-------------------------------------------------------------------------------

#----------------------------------MAIN-----------------------------------------


#asd = Asd();
new_scheduler = SchedulerEdge()
new_scheduler.start_process();
#juca = Analisador_Complexo(asd)
#juca.start()
http_server = MTServer(new_scheduler)
http.start()
