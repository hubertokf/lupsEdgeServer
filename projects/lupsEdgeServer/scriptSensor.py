#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('db.sqlite3')

with con:
    
    cur = con.cursor()
    x = 7
    start = 31
    for gateway_id in range(8,14):
        #print("Gateway: "+str(gateway_id))
        sufix = gateway_id-7
        for i in range(start,start+5):
            #print("Sensor: "+str(start))
            if i>=10:
                sensor_uuid = "b9d17987-de24-0002-000"+str(abs(sufix))+"-0000000000"+str(i)
            else:
                sensor_uuid = "b9d17987-de24-0002-000"+str(abs(sufix))+"-00000000000"+str(i)
            print(sensor_uuid)
            cur.execute("INSERT INTO API_RestFul_sensor(model,gateway_id,manufacturer_id, sensorType_id,uuID) VALUES(1,"+str(gateway_id)+",1,3,'"+str(sensor_uuid)+"');")
            start = i+1
            pass