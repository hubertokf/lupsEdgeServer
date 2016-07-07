import json

class Proceeding(object):

    base_dir = "/mnt/1wire/uncached/"
    device_folder = ""
    device_file = ""

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_val_atuador(self, vatuador):
        self.vatuador = vatuador

    def get_val_atuador(self):
        return vatuador

    # Realiza toda a operação do proceeding utilizando o métodos criados
    def processamento(self,a):  #device_folder <--- id do sensor, referente a pasta
        jsonObject = json.loads(a)

        self.set_id(jsonObject['id_real'])
        self.set_val_atuador(jsonObject['acao_atuador'])

        if get_acao() == 1:   # Ativa o atuador

        else if get_acao() == 2:  # Desativa o atuador
