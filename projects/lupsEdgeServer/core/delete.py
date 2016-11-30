import requests

headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}

for i in range(8,1006):
    r = requests.delete("http://localhost:8000/persistances/"+str(i), headers=headers)

print(r)
