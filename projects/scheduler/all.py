import schedule
import time
import sqlite3

def job(message='stuff'):
    print("I'm working...", message)

conn = sqlite3.connect('dados_sensores.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM dados_sensores;
""")

for linha in cursor.fetchall():
	#print(linha[2])
	rslt = int(linha[2])
	sensor = linha[1]
	schedule.every(rslt).seconds.do(job, message=sensor)

conn.close()

while True:
    schedule.run_pending()
    time.sleep(1)