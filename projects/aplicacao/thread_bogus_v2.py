import datetime

import bottle
import mtwsgi
import _thread

from analisador import  *
from mtbottle_v2 import *


#---------------------Objeto compartilhado entre as THREADS---------------------
class Asd(object):
    def __init__(self):
        self.asd = 1

    def set_asd(self, val):
        self.asd = val

    def get_asd(self):
        return self.asd
#-------------------------------------------------------------------------------

#--------------------MAIN-------------------

asd = Asd();

juca = Analisador_Complexo(asd)
juca.start()
tes = MTServer(asd)
tes.start()
