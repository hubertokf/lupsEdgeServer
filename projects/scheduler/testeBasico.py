from datetime import datetime
import time
import os
import sqlite3
import threading

from apscheduler.schedulers.background import BackgroundScheduler


def tick(a):
	print(a)
	#print(b)
    #print('Tick! The time is: %s' % datetime.now())
def te():
	print("foi")

def loop():
	while True:
	 	time.sleep(2)


if __name__ == '__main__':
	scheduler = BackgroundScheduler()

	conn = sqlite3.connect('dados_sensores.db')
	cursor = conn.cursor()

	cursor.execute("""
	SELECT * FROM dados_sensores;
	""")

	for linha in cursor.fetchall():
	#print(linha[2])
		rslt = int(linha[2])
		sensor = linha[1]
		scheduler.add_job(tick, 'interval', seconds = rslt, id = sensor, args=[sensor])

	conn.close()

    #scheduler.add_job(tick, 'interval', seconds = 10,id = "ab", args=[a,b])
	scheduler.start()
	#https://docs.python.org/3.4/library/threading.html
	#http://www.tutorialspoint.com/python/python_multithreading.htm
	#thread = loop()
	thread = threading.Thread(target=loop)

	thread.start();
	thread.join();

#	a = 5

#	try:
        # This is here to simulate application activity (which keeps the main thread alive).
#		a = 0
#		while True:
#			time.sleep(2)
#			if(a == 10):
#				scheduler.remove_job("bc")
#				scheduler.add_job(te, 'interval',seconds = a, id ="pica")
#				a = a + 1
#	except (KeyboardInterrupt, SystemExit):
		# Not strictly necessary if daemonic mode is enabled but should be done if possible
#		scheduler.remove_job("bc")
        #scheduler.shutdown()
