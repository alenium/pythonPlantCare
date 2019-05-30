#!/usr/bin/python3

from time import sleep

import RPi.GPIO as GPIO
import sys
import os
import pymysql
from subprocess import Popen



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

connection =pymysql.connect(host='192.168.1.150',port=3306,user='stateuser',password="",database="state")
cursor=connection.cursor()
'''
cursor.execute("""SELECT * FROM `processingFun` where 1;""")
string=cursor.fetchall()
'''
#settup GPIO
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
#player2=OMXPlayer(clip4,args=['-b','--no-osd'])
#player2.hide_video()
#player2.pause()
#player2.mute()
GPIO.output(23,1)
for i in range(3):
        GPIO.output(24,0)
        sleep(0.5)
        GPIO.output(24,1)
        sleep(0.5)
done=0
toggle=0
lastData=0
first=1
light=False
while not done:
        cursor.execute("""SELECT * FROM `processingFun` where 1;""")
        stuff=cursor.fetchall()
        data=stuff[0][1]
        print(stuff)
        if first==1:
                lastData=data
                first=0
        os.system("echo hello")
        if data !=lastData:
                if data==1 or data==0:
                        toggle=1
                elif data==2:
                        toggle=2
                else:
                        toggle=3
        lastData=data
        if toggle==1:
                toggle=0
                GPIO.output(23,0)
                sleep(1.5)
                GPIO.output(23,1)
        else:
                GPIO.output(23,1)
        if toggle==2:
                toggle=0
                light=True
        if toggle==3:
                toggle=0
                light=False
        if light==True:
                GPIO.output(24,0)
        else:
                GPIO.output(24,1)
        connection.commit()
        sleep(0.6)
connection.close()
