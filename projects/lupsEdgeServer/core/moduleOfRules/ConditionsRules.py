# -*- coding: utf-8 -*-
from business_rules.variables import BaseVariables, numeric_rule_variable, boolean_rule_variable
import requests
import json
import datetime
import math

class ConditionsRules(BaseVariables):
    def __init__ (self, parameters):
        self.parameters = parameters

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
        gateways                = Gathering();
        data_condition          = json.loads(params)
        uuid['uuID']            = data_condition['sensor']
        info_gateway_and_sensor = gateways.coleting_value_of_sensor(uuid)
        collectDate             = datetime.datetime.now()
        format_colletcDate        = collectDate.strftime("%Y-%m-%d %H:%M:%S")
        value                   = info_gateway_and_sensor
        self.parameters.create_obj_and_set_value(uuid['uuID'],value,format_colletcDate)
        return value
        
    @numeric_rule_variable
    def diff_values_sensor(self,params):

        gateways        = Gathering();
        data_condition  = json.loads(params)
        uuid['uuID']    = data_condition['sensor']
        current_value   = gateways.coleting_value_of_sensor(uuid['uuID'])
        #problema do gathering/LJ?
        url             = "http://localhost:8000/sensors/?format=json&uuID={0}".format(uuid['uuID'])
        r               = requests.get(url)
        sensor          = r.json()
        url             = "http://localhost:8000/persistence/?format=json&sensor={0}".format(sensor['id'])
        r               = requests.get(url)
        preceding_value = r.json()
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

from core.gathering import Gathering
