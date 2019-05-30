        
import time
import pymysql
import datetime
now=datetime.datetime.now()
connection =pymysql.connect(host='192.168.1.150',port=3306,user='******',password="*******",database="state")
cursor=connection.cursor()

cursor.execute("""SELECT * FROM `processingFun` where 1;""")
stuff=cursor.fetchall()
connection.close()
toggle=int(stuff[0][1])
lastToggle=toggle
def watering(toggle):
        print("watering toggle :"+str(toggle))
        if toggle==0:
                cursor.execute("""UPDATE `processingFun` set a=1 where id=1;""")# 2 is light on 3 is light off 0, 1 toggle for water
                stuff=cursor.fetchall()
        else:
                cursor.execute("""UPDATE `processingFun` set a=0 where id=1;""")# 2 is light on 3 is light off 0, 1 toggle for water
                stuff=cursor.fetchall()
        print(stuff)
        connection.commit()
        time.sleep(5)


def lightOff():
        print("lightsOff")
        cursor.execute("""UPDATE `processingFun` set a=3 where id=1;""") 
        stuff=cursor.fetchall()              
        connection.commit()
        time.sleep(5)


def lightOn():
        print("lightsOn")
        cursor.execute("""UPDATE `processingFun` set a=2 where id=1;""")
        stuff=cursor.fetchall()
        connection.commit()
        time.sleep(5)

lastNow=now
try:
        connection =pymysql.connect(host='192.168.1.150',port=3306,user='stateuser',password="",database="state")
        cursor=connection.cursor()
        cursor.execute("""SELECT * FROM `processingFun` where 1;""")
        stuff=cursor.fetchall()
        toggle=int(stuff[0][1])
        lastToggle=toggle

        while True:
                now=datetime.datetime.now()
                cursor.execute("""SELECT * FROM `processingFun` where 1;""")
                stuff=cursor.fetchall()
                toggle=int(stuff[0][1])
                if now.hour==10 and lastNow != 10:
                        watering(toggle)
                if now.hour==18 and lastNow != 18:
                        watering(toggle)
                if now.hour==20 and lastNow != 20:
                        lightOff()
                if now.hour==9 and lastNow !=9:
                        lightOn()
                lastNow=now.hour
except:
        print("trying to reconnect")
finally:
        connection.close()


