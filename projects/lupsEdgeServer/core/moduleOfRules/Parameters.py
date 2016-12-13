
class Parameters(object):

    def __init__(self):
        self.disct = {}

    def create_obj_and_set_value(self,uuid,id_sensor,value,collectDate):
        self.disct[uuid]                = {}
        self.disct[uuid]["id_sensor"]   = id_sensor
        self.disct[uuid]["value"]       = value
        self.disct[uuid]["collectDate"] = collectDate
        # print("Ocorreu tudo bem aqui\n. uuid = {0}\n valor = {1}".format(uuid,self.disct[uuid]))


    def get_element_dist(self,a):
        return  self.disct[a]

    def get_dist(self):
        return self.disct
