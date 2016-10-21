from business_rules.variables import BaseVariables, numeric_rule_variable, boolean_rule_variable
import requests
import json

class ConditionsRules(BaseVariables):
    def __init__ (self, parameters):
        self.parameters = parameters

    @numeric_rule_variable
    def getNumber(self,a):
        return self.parameters.value

    @numeric_rule_variable
    def get_extern_sensor(self):
        uuid = "tenho que inserir"
        url  = "http://10.0.50.184:8081/sensor={0}".uuid
        r    = requests.get(url)

    @numeric_rule_variable
    def get_verify_sensor(self,params):

        gateways       = Gathering();
        data_condition = json.loads(params)
        uuid['uuID']   = data_condition['sensor']
        value          = gateways.coleting_value_of_sensor(uuid['uuID'] )
        return value


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

from ./gathering import Gathering
