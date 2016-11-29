import bottle
import core.mtwsgi
import _thread
from core.mtbottle import *
from core.scheduler import *

#----------------------------------MAIN-----------------------------------------

new_scheduler = SchedulerEdge()

http_server = MTServer(new_scheduler)

http.start()
