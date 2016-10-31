''' função encarregada de gerar e inserir condições na classe
    de condições de regra
'''

def create_condition(id_of_sensor):
    # abre o arquivo com contem as condições
    filer = open('ConditionsRules.py','a')
    #estrututra uma sitrng pno formato das condições
    condition = """
    # solicita a coleta do valor de um sensor e retorna para a regra, onde o valor será avaliado
    @numeric_rule_variable
    def getNumber_{0}(self):
        #inserir aqui a instacia do objeto gathering
        return self.number
    """.format(id_of_sensor)

    filer.write(condition)
    filer.close()

    #print(condition)
