from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler


def tick(a,b):
	print(a,b)
	#print(b)
    #print('Tick! The time is: %s' % datetime.now())
def te():
    print("foi")

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
  	
    a = "bosta"
    b = "jaja"
    c = "nenhuma"

    scheduler.add_job(tick, 'interval', seconds = 10,id = "ab", args=[a,b])
    scheduler.add_job(tick, 'interval', seconds = 5,id = "bc", args=[c,b])
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    a = 5

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        a = 0
        while True:
            time.sleep(2)
            if(a == 10):
                scheduler.remove_job("bc")
                scheduler.add_job(te, 'interval',seconds = a, id ="pica")
            a = a + 1
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.remove_job("bc")
        #scheduler.shutdown()
