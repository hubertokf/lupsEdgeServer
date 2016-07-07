import pycurl
import json
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://localhost:8000/sensors/?format=json')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
jsonObject = json.loads(body.decode('iso-8859-1'))
#print(body.decode('iso-8859-1'))
#print(jsonObject)
for row in jsonObject:
    print(row['url'])

# Gravar esses dados em algum lugar, pois quando tiver alteração no DB deve ocorrer uma comparação para alterar os eventos agendados(Scheduler)
