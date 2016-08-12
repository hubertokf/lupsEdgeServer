import requests
import datetime

class Publisher(object):

    def set_publisher(self, id_sensor, value, contextServer):

        #Cabeçalho do token, utilizado na publicação. É uma chave de verificação
        headers = {'Authorization':'token %s' % "efd7b8057d8eb6951a3138cbfd9b72cf68b17295"}

        date_now = datetime.datetime.now()  # Realiza um get da DATE/TIME
        payload = {'collectDate': date_now, 'value': valeu, 'sensor': id_sensor, 'contextServer': contextServer}

        # Realiza a publicação nesse comando logo abaixo
        r = requests.post("http://localhost:8000/persistances/", data=payload, headers=headers)


#-------------------------Converte em um formato a hora, retirando fuso horário---------------------
#import requests
#import datetime
#import time

#headers = {'Authorization':'token %s' % "efd7b8057d8eb6951a3138cbfd9b72cf68b17295"}

#date_now = datetime.datetime.now()
#date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")

#payload = {'collectDate': date_str, 'value': '10', 'sensor': '1', 'contextServer':'1'}

#r = requests.post("http://localhost:8000/persistances/", data=payload, headers=headers)
