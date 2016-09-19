from business_rules.variables import BaseVariables, numeric_rule_variable, boolean_rule_variable
import json as intermed

class ConditionsRules(BaseVariables):
    def __init__ (self, parameters):
        self.parameters = parameters
        self.ativator   = True # controla a primeira leitura do valor do sensor x, oriunda de uma chamada de regra

    @numeric_rule_variable
    def getNumber(self):
        return self.parameters.value

    @numeric_rule_variable
    def get_verify_sensor(self,sensor):
        if(self.ativator): # se verdadeiro, pega valor do parametro do metodo get_rules, caso contrário, solicita o valor para o gathering
            value = self.parameters.value
            self  = False
        else:
            print("ko")
            # intermed.dumps(sensor)
            # passar paramatros para o gathering ou processar na regra
            #value = Gathering.get_values_sensor(sensor)

        return value

    @boolean_rule_variable
    def fault_check_x(self,sensor):

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
