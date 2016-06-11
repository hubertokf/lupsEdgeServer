
class Proceeding(object):

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

    def set_val_atuador(self, vatuador):
        self.vatuador = vatuador

    def get_val_atuador(self):
        return vatuador

    def set_acao(self, acao): # 1 = sensor |   2 = atuador
        self.acao = acao

    def get_acao(self):
        return self.acao

    # Realiza toda a operação do proceeding utilizando o métodos criados
    def processamento(self,id,acao):  #device_folder <--- id do sensor, referente a pasta
        self.set_id(id)
        self.acao(acao)

        if get_acao == 1:   # Enviar dado referente a acao do sensor
            device_file = base_dir + self.get_id + "/temperature12"

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

        else if get_acao == 2:  # Enviar dado referente a acao do atuador
