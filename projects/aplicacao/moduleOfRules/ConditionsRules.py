from business_rules.variables import BaseVariables, numeric_rule_variable, boolean_rule_variable

class ConditionsRules(BaseVariables):
    def __init__ (self, parameters):
        self.parameters = parameters

    @numeric_rule_variable
    def getNumber(self):
        return self.parameters.value

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
