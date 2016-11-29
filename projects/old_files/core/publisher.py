import requests
import datetime
import json

class Publisher(object):

    core = None

    def __init__(self, parent):             #instância do objeto e inicia o escalonador

        self.core = parent

    def set_publisher_local(self, id_sensor, value, contextServer):

        headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}
        #print("---------------"+id_sensor+"------------------------")

        date_now = datetime.datetime.now()
        date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")

        payload = {'collectDate': date_str, 'value': value, 'sensor': '1', 'contextServer':'1'}

        r = requests.post("http://localhost:8000/persistances/", data=payload, headers=headers)




        #Cabeçalho do token, utilizado na publicação. É uma chave de verificação
    #     headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}
    #
    #     date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Realiza um get da DATE/TIME
    #     #date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
    #     payload = {"collectDate": date_now, "value": value, "sensor": id_sensor, "contextServer": 1}
    #     payload = json.dumps(payload)
    #     # Realiza a publicação nesse comando logo abaixo
    #     #collectDate: "2016-07-21T15:44:21.766584", value: 14, sensor: 2, contextServer: 1
    #     r = requests.post("http://localhost:8000/persistances/", json=payload, headers=headers)
    #
    #     print("--------------------------------PUBLICOU--------------------------------------")
    #
    # def set_publisher_contexto(self, id_sensor, value, date_coleta):
    #
    #     #Cabeçalho do token, utilizado na publicação. É uma chave de verificação
    #     headers = {'Authorization':'token %s' % "cfb281929c3574091ad2a7cf80274421e6a87c59"}
    #
    #     date_now = datetime.datetime.now()  # Realiza um get da DATE/TIME
    #     payload = {'sensor_id': id_sensor, 'valorcoletado': valeu, 'datacoleta': date_coleta}
    #
    #     # Realiza a publicação nesse comando logo abaixo
    #     r = requests.post("http://localhost:8000/persistances/", data=payload, headers=headers)


#-------------------------Converte em um formato a hora, retirando fuso horário---------------------
#import requests
#import datetime
#import time

#headers = {'Authorization':'token %s' % "efd7b8057d8eb6951a3138cbfd9b72cf68b17295"}

#date_now = datetime.datetime.now()
#date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")

#payload = {'collectDate': date_str, 'value': '10', 'sensor': '1', 'contextServer':'1'}

#r = requests.post("http://localhost:8000/persistances/", data=payload, headers=headers)
