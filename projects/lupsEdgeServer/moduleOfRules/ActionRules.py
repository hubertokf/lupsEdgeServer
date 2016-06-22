from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC, FIELD_TEXT
from business_rules import run_all
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC, FIELD_TEXT
from ConditionsRules import ConditionsRules
from Parameters import Parameters
import os
import json
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
import smtplib


class ActionRules(BaseActions):

    def __init__ (self, parameters):
        self.parameters = parameters


    @rule_action(params={"info_adicional":FIELD_NUMERIC })
    def publish(self,info_adicional): # ação que ativa o evento de publicação
        json = '{{"id_sensor": {0}, "event": "{1}", "valor",{2}}}'.format(self.parameters.id,self.parameters.event,self.parameters.value)
        print(json)
        #chamar tratador de evento

    @rule_action(params={"info_adicional":FIELD_NUMERIC })
    def gathering(self,info_adicional): # ação que ativa o evento de coleta
        json = '{{"id_sensor": {0}, "event": "{1}", "valor",{2}}}'.format(self.parameters.id,self.parameters.event,self.parameters.value)
        #chamar tratador de evento

    @rule_action(params={"info_adicional":FIELD_NUMERIC })
    def proceding(self,info_adicional): # ação que ativa o evento de atuação
        json = '{{"id_sensor": {0}, "event": "{1}", "valor":{2}}}'.format(self.parameters.id,self.parameters.event,self.parameters.value)
        print (json)
        #chamar tratador de evento

    @rule_action(params = {"inf": FIELD_TEXT})
    def test_post_Event(self, inf):
        sender = 'tainaribeiro.rs@gmail.com'
        receivers = ['tainaribeiro.rs@hotmail.com']

        message = "Houve um erro de leitura no sensor{0}.\n Por favor, verifique a situação do sensor assim como a sua comunicação com o gateway".format(self.parameters.id)
        subject = "Problema no sensor {0}".format(self.parameters.id)

        # build the message
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = ', '.join(receivers)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        print(msg.as_string())
        try:
          smtpObj = smtplib.SMTP('smtp.gmail.com',587)
          smtpObj.ehlo()
          smtpObj.starttls()
          smtpObj.login(sender,"3123123123121")
          smtpObj.sendmail(sender, receivers, msg.as_string())
          print ("Successfully sent email")
          smtpObj.quit()
        except :
          print ("Error: unable to send email")
          smtpObj.quit()
