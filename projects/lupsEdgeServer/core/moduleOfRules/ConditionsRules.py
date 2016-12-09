# -*- coding: utf-8 -*-
from business_rules.variables import BaseVariables, numeric_rule_variable, boolean_rule_variable
import requests
import json
import datetime
import math
import core.event_treatment
class ConditionsRules(BaseVariables):

    core_father = None
    def __init__ (self, parameters,parent):
        self.core_father = parent
        self.parameters = parameters
        # self.headers ={'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"} # este token sera coletado na base de parametros do bd de borda

    @numeric_rule_variable
    def getNumber(self,a):

        self.parameters.set_i(a)
        return 9

    @numeric_rule_variable
    def get_extern_sensor(self):
        #problema do gathering/LJ
        uuid = "tenho que inserir"
        url  = "http://10.0.50.184:8081/sensor={0}".uuid
        r    = requests.get(url)

    @numeric_rule_variable
    def get_verify_sensor(self,params):
        uuid                    = {}
        object_events           = core.event_treatment.Event_Treatment(self.core_father)
        data_condition          = json.loads(params)
        #print("visionnnnnnnn",data_condition['sensor'])
        uuid['uuID']            = data_condition['sensor']
        uuid['event']           = "gathering"
        uuid['collect_to_rule'] = True

        # url_gateway             = "http://localhost:8000/sensors/?format=json&uuID={0}".format(uuid['uuID'])
        # info_gateway            = requests.get(url_gateway,self.headers).json()

        param = {"uuID":uuid['uuID']}
        info_gateway = self.core_father.API_access("get", "sensors", model_id=None, data=None, param=param).json()

        id_gateway              = info_gateway[0]['gateway']
        uuid['gateway']         = id_gateway
        json_dumps_uuid         = uuid


        #json_dumps_uuid         = json.dumps(uuid)

        #print(json_dumps_uuid)

        info_gateway_and_sensor = object_events.event(json_dumps_uuid)
        format_colletcDate      = info_gateway_and_sensor['collectDate']
        value                   = float(info_gateway_and_sensor['value'])
        self.parameters.create_obj_and_set_value(uuid['uuID'],value,format_colletcDate)
        #print(value)
        return value

    @numeric_rule_variable
    def diff_values_sensor(self,params):

        gateways        = Gathering(self.core_father);
        data_condition  = json.loads(params)
        uuid['uuID']    = data_condition['sensor']
        current_value   = gateways.coleting_value_of_sensor(uuid['uuID'])
        #problema do gathering/LJ?

        # url             = "http://localhost:8000/sensors/?format=json&uuID={0}".format(uuid['uuID'])
        # r               = requests.get(url)
        # sensor          = r.json()
        param = {"uuID":uuid['uuID']}
        sensor            = self.core_father.API_access("get", "sensors", model_id=None, data=None, param=param).json()

        # url             = "http://localhost:8000/persistence/?format=json&sensor={0}".format(sensor['id'])
        # r               = requests.get(url)
        # preceding_value = r.json()

        param = {"sensor":sensor['id']}
        preceding_value = self.core_father.API_access("get", "persistence", model_id=None, data=None, param=param).json()

        return math.fabs(current_value - preceding_value['value'])

    '''Método de verificação do tempo e habilita um conunto de regras, apenas um esboço. devo arrumar'''
    @numeric_rule_variable
    def verify_time_and_trigger_rules(self,params):
        obj_json = json.loads(params)
        #devo verificar o status de uma das regras ,se falso, seto todas como true e seto o tempo inicial, devo salvar em algum lugar
        if(obj_json['type_time'] == "hour"): #inserir um save da hora de inicialização
            time = datetime.hour - obj_json['time_set'] # calcua a distância do tempo
        else:
            time = datetime.minute - obj_json['time_set']

    @boolean_rule_variable
    def fault_check_x(self):

        total_verificacao = 10
        contador = total_verificacao
        trigger = False

        while (contador > 0 and trigger == False):
                # Colocar o objeto gathering
                value_sensor = self.parameters.value
                if(value_sensor < 99.9):
                    trigger = True
                    break
                contador = contador - 1

        return trigger

    @numeric_rule_variable
    def calcule_average(self,parameter):
        object_events = core.event_treatment.Event_Treatment(self.core_father)
        average       = 0
        array_sensors = self.core_father.API_access("get", "sensors", model_id=None, data=None, param=None).json()
        
        for sensor in array_sensors:
            sensor['event']           = "gathering"
            sensor['collect_to_rule'] = True
            info_gateway_and_sensor   = object_events.event(sensor)
            format_colletcDate        = info_gateway_and_sensor['collectDate']
            value                     = float(info_gateway_and_sensor['value'])
            average = average + value

        average = average/len(array_sensors)
        return average




from core.gathering import Gathering
