
class Parameters(object):

    def __init__(self):
        self.disct = {}

    def create_obj_and_set_value(self,uuid,value,collectDate):
        self.disct[uuid] = {}
        self.disct[uuid]["value"] = value
        self.disct[uuid]["collectDate"] = collectDate
        # print("Ocorreu tudo bem aqui\n. uuid = {0}\n valor = {1}".format(uuid,self.disct[uuid]))


    def get_i(self,a):
        return  self.disct[a]
