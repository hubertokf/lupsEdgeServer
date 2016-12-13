#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('db.sqlite3')

with con:
    
    cur = con.cursor()
    x = 7
    start = 1
    for sensor_id in range(176,206):
        cur.execute("INSERT INTO API_RestFul_schedule(status,sensor_id,year,day,hour,month,minute,second,event) VALUES(1,"+str(sensor_id)+",'*','*','*','*','*/5','0','gathering');")
