import datetime

import bottle
import core.mtwsgi
import _thread
from core.mtbottle import *
from core.scheduler import *

#----------------------------------MAIN-----------------------------------------


        #asd = Asd();
new_scheduler = SchedulerEdge()
#new_scheduler.start_process();
#juca = Analisador_Complexo(asd)
#juca.start()
http_server = MTServer(new_scheduler)
http.start()
