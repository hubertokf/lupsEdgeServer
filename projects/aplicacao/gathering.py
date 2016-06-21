import json

class Gathering(object):

    base_dir = "/mnt/1wire/uncached/"
    device_folder = ""
    device_file = ""

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_val_sensor(self, vsensor):
        self.vsensor = vsensor

    def get_valor(self):
        return self.vsensor

    # Realiza toda a operação do proceeding utilizando o métodos criados
    def processamento(self,a):  #device_folder <--- id do sensor, referente a pasta
        jsonObject = json.loads(a)

        self.set_id(jsonObject['id_real'])

        device_file = base_dir + self.get_id() + "/temperature12"

        ler = 0
        valor_temp = float("99.3")

        while ((valor_temp == 99.3 or valor_temp == 85.0) and (ler < 10)):  #Utilizado na verificação de erros ao requisitar dados
            result = ""
            try:
                f = open(device_file)
                saida = f.readline()
                f.close()
            except IOError:
                saida = "        99.3"
            # Logando...
            saida_temp = saida[0:12]
            try:
                valor_temp = float(saida_temp)
            except ValueError:
                valor_temp = float("99.1")
                ler = ler + 1

            self.set_val_sensor(saida[0:12].strip())
