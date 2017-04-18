
class Parameters(object):

    def __init__(self):
        self.dict            = {}
        self.dict_for_events = {}

    def create_obj_and_set_value(self,uuid,id_sensor,value,collectDate):
        self.dict[uuid]                = {}
        self.dict[uuid]["id_sensor"]   = id_sensor
        self.dict[uuid]["value"]       = value
        self.dict[uuid]["collectDate"] = collectDate
        # print("Ocorreu tudo bem aqui\n. uuid = {0}\n valor = {1}".format(uuid,self.disct[uuid]))


    def get_element_dist(self,a):
        return  self.disct[a]

    def get_dist(self):
        return self.disct

    def get_dict_for_event(self):
        return None

    def set_dict_for_event(self,topic,pay_load,ip_edge_receive):
        pass
