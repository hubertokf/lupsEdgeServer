import requests

def get_values_on_gatway():

    headers = {'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"}
    url = 'http://10.0.50.155/virtualSensor'
    request = requests.get(url, headers=headers)
    information_of_sensor = request.json()
    print(information_of_sensor)


if __name__ == '__main__':
    get_values_on_gatway()
