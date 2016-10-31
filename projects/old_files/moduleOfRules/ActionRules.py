from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC,FIELD_SELECT, FIELD_TEXT
from business_rules import run_all
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC, FIELD_TEXT
from moduleOfRules.ConditionsRules import ConditionsRules
from moduleOfRules.Parameters import Parameters
import os
import json
import email
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
import smtplib


class ActionRules(BaseActions):

    def __init__ (self, parameters):
        self.parameters = parameters

    @rule_action(params={"info_adicional": FIELD_TEXT })
    def publisher(self,info_adicional): # ação que ativa o evento de publicação
        #json = '{{"id_sensor": {0}, "event": "{1}", "valor",{2}}}'.format(self.parameters.id,info_adicional,self.parameters.value)
        #resp = 'entrou no publicador {0}\n\n '.format(self.parameters.id)
        #----------------------------------------------------------------------------------------------------
        #headers = {'Authorization':'token %s' % "878559b6d7baf6fcede17397fc390c5b9d7cbb77"}
        #print("---------------"+id_sensor+"------------------------")

        #date_now = datetime.datetime.now()
        #date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")

        #payload = {'collectDate': date_str, 'value': value, 'sensor': '1', 'contextServer':'1'}

        #r = requests.post("http://localhost:8000/persistances/", data=payload, headers=headers)
        #----------------------------------------------------------------------------------------------------
        #chamar tratador de evento

    @rule_action(params={"info_adicional":FIELD_NUMERIC })
    def gathering(self,info_adicional): # ação que ativa o evento de coleta
        json = '{{"id_sensor": {0}, "event": "{1}", "valor",{2}}}'.format(self.parameters.id,self.parameters.event,self.parameters.value)
        #chamar tratador de evento

    @rule_action(params={"info_adicional":FIELD_NUMERIC })
    def proceding(self,info_adicional): # ação que ativa o evento de atuação
        json = '{{"id_sensor": {0}, "event": "{1}", "valor":{2}}}'.format(self.parameters.id,self.parameters.event,self.parameters.value)
        #chamar tratador de evento

    @rule_action(params = {"info_adicional": FIELD_TEXT})
    def test_post_Event(self, info_adicional):
        #sender = 'tainaribeiro.rs@gmail.com'
        #receivers = ['tainaribeiro.rs@hotmail.com']

        #message = "Houve um erro de leitura no sensor{0}.\n Por favor, verifique a situação do sensor assim como a sua comunicação com o gateway".format(self.parameters.id)
        #subject = "Problema no sensor {0}".format(self.parameters.id)

        # build the message
        # msg = MIMEMultipart()
        # msg['From'] = sender
        # msg['To'] = ', '.join(receivers)
        # msg['Date'] = formatdate(localtime=True)
        # msg['Subject'] = subject
        # msg.attach(MIMEText(message))
        # print(msg.as_string())
        # try:
        #   smtpObj = smtplib.SMTP('smtp.gmail.com',587)
        #   smtpObj.ehlo()
        #   smtpObj.starttls()
        #   smtpObj.login(sender,"3123123123121")
        #   smtpObj.sendmail(sender, receivers, msg.as_string())
        #   print ("Successfully sent email")
        #   smtpObj.quit()
        # except :
        #   print ("Error: unable to send email")
        #   smtpObj.quit()
        print(" ")

    @rule_action(params = {"ruler": FIELD_TEXT})
    def gathering_error(self,ruler):

        contador = self.parameters.contador - 1
        json = '{{"id_sensor": {0}, "event": "e", "valor":{1}, "contador": {2}}}'.format(self.parameters.id,self.parameters.value,contador)
        object_events = Event_Treatment()
        object_events.event(1,json)

    '''Método de transição para proximo regra, desabilita o conjunto de regra acionadas,bem como regra atual.
       Habilita proxima regra de transição, id's das regras di cinjunto encontranm-se no array rules,
       id da regra atual=> id_current_rule, id da próxima regra=>id_next_rule'''

    @rule_action(params={"rules": FIELD_SELECT,"id_next_rule": FIELD_NUMERIC,"id_current_rule":FIELD_NUMERIC})
    def next_rule(self,rules,id_next_rule,id_current_rule):

        headers = {'Authorization':'token %s' % "9517048ac92b9f9b5c7857e988580a66ba5d5061"}
        payload = {'status':False}
        url     ="http://localhost:8000/rules/{0}".format(id_current_rule)
        r       = requests.put(url, data=payload, headers=id_current_rule)
        payload = {'status':True}
        url     ="http://localhost:8000/rules/{0}".format(id_next_rule)
        r       = requests.put(url, data=payload, headers=headers)

        for id_rule_set in rules:
            payload = {'status':False}
            url     ="http://localhost:8000/rules/{0}".format(id_rule_set)
            r       = requests.put(url, data=payload, headers=headers)



    '''Método que desabilita todas as regras, ele só vai setar novamente quando receber um ok'''
    @rule_action
    def failure_transition(self,rules,id_rule,id_current_rule):
                payload = {'status':False}
                url     ="http://localhost:8000/rules/{0}".format(id_current_rule)
                r       = requests.put(url, data=payload, headers=id_current_rule)
                payload = {'status':False}
                url     ="http://localhost:8000/rules/{0}".format(id_next_rule)
                r       = requests.put(url, data=payload, headers=headers)

                for id_rule_set in rules:
                    payload = {'status':False}
                    url     ="http://localhost:8000/rules/{0}".format(id_rule_set)
                    r       = requests.put(url, data=payload, headers=headers)

    @rule_action(params = {"uuid": FIELD_TEXT,"url": FIELD_TEXT})
    def get_extern_sensor(self,uuid,url):
        #problema do gathring/LJ
        url  = "http://10.0.50.184:8081/sensor={0}".format(uuid)
        r    = requests.get(url)
        print(r.json())

    @rule_action(params={"foo": FIELD_TEXT})
    def get_sensor(self,foo ):
        pass
