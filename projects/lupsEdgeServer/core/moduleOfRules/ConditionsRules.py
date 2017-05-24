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
    def get_verify_sensor(self,params):

        ''' Método responsável pela leitura de um dispostivo e retorna o valor coletado para analise na condição ao qual está vinculado.
         '''

        collect_data            = {}
        object_events           = core.event_treatment.Event_Treatment(self.core_father)
        data_condition          = json.loads(params)

        collect_data['uuID']            = data_condition['sensor']
        collect_data['event']           = "gathering"
        collect_data['collect_to_rule'] = True

        param        = {"uuID":collect_data['uuID']}
        info_gateway = self.core_father.API_access("get", "sensors", model_id=None, data=None, param=param).json()

        id_gateway              = info_gateway[0]['gateway']
        collect_data['gateway'] = id_gateway
        json_dumps_collect_data = collect_data

        info_gateway_and_sensor = object_events.event(json_dumps_collect_data)# tratar erro de comunicação, gateway e/ou sensor
        format_colletc_date     = info_gateway_and_sensor['collectDate']
        value                   = float(info_gateway_and_sensor['value'])
        self.parameters.create_obj_and_set_value(collect_data['uuID'],None,value,format_colletc_date)

        return value

    @numeric_rule_variable
    def diff_values_sensor(self,params):

        gateways        = Gathering(self.core_father);
        data_condition  = json.loads(params)
        uuid['uuID']    = data_condition['sensor']
        current_value   = gateways.coleting_value_of_sensor(uuid['uuID'])

        param = {"uuID":uuid['uuID']}
        sensor            = self.core_father.API_access("get", "sensors", model_id=None, data=None, param=param).json()

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
    def calcule_average(self,parameter=None):
        object_events = core.event_treatment.Event_Treatment(self.core_father)
        average       = 0
        array_sensors = self.core_father.API_access("get", "sensors", model_id=None, data=None, param=None).json()

        for sensor in array_sensors:
            sensor['event']           = "gathering"
            sensor['collect_to_rule'] = True
            info_gateway_and_sensor   = object_events.event(sensor)
            format_colletcDate        = info_gateway_and_sensor['collectDate']
            value                     = float(info_gateway_and_sensor['value'])
            average                   = average + value
            self.parameters.create_obj_and_set_value(sensor["uuID"],sensor["id"],value,format_colletcDate)
        average = average/len(array_sensors)
        return average


from core.gathering import Gathering
