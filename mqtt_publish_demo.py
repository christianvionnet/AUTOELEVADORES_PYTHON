import paho.mqtt.publish as publish
import mysql.connector
import os
import serial
import time

db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="sysadmin",
    database="Autoelevadores"
)

#Enable Serial Communication
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.01)

cursor = db.cursor()

def lectura(self):
    #cursor.execute("SELECT * FROM TABLA_MPO_1 ORDER BY id DESC LIMIT 1")
    cursor.execute("SELECT mpo_1, mpo_2, mpo_3, mpo_4, mpo_5, mpo_6, mpo_7, mpo_8, mpo_9, mpo_10, mpo_11, mpo_12 FROM TABLA_MPO_1, TABLA_MPO_2, TABLA_MPO_3 ORDER BY TABLA_MPO_1.id DESC, TABLA_MPO_2.id DESC, TABLA_MPO_3.id DESC LIMIT 1")
    
    resultado = cursor.fetchone()
    mpo1=resultado[0]
    mpo2=resultado[1]
    mpo3=resultado[2]
    mpo4=resultado[3]
    mpo5=resultado[4]
    mpo6=resultado[5]
    mpo7=resultado[6]
    mpo8=resultado[7]
    mpo9=resultado[8]
    mpo10=resultado[9]
    mpo11=resultado[10]
    mpo12=resultado[11]
    
    db.commit()

    #msgs = [{'topic': "MPO/pedales", 'payload': mpo1}, ("MPO/pedales", mpo2, 0, False)]
    #publish.multiple(msgs, hostname="test.mosquitto.org")
    
    publish.single("MPO/mpo1", mpo1, hostname="test.mosquitto.org")
    publish.single("MPO/mpo2", mpo2, hostname="test.mosquitto.org")
    publish.single("MPO/mpo3", mpo3, hostname="test.mosquitto.org")
    publish.single("MPO/mpo4", mpo4, hostname="test.mosquitto.org")
    publish.single("MPO/mpo5", mpo5, hostname="test.mosquitto.org")
    publish.single("MPO/mpo6", mpo6, hostname="test.mosquitto.org")
    publish.single("MPO/mpo7", mpo7, hostname="test.mosquitto.org")
    publish.single("MPO/mpo8", mpo8, hostname="test.mosquitto.org")
    publish.single("MPO/mpo9", mpo9, hostname="test.mosquitto.org")
    publish.single("MPO/mpo10", mpo10, hostname="test.mosquitto.org")
    publish.single("MPO/mpo11", mpo11, hostname="test.mosquitto.org")
    publish.single("MPO/mpo12", mpo12, hostname="test.mosquitto.org")

    cursor.execute("SELECT nombre FROM USUARIO_ACTIVO")
    resultado2 = cursor.fetchone()
    nombre = resultado2[0]
    db.commit()
    
    publish.single("MPO/usuario_activo", nombre, hostname="test.mosquitto.org")
    print("hecho")
    
try:
    while True:
        lectura(1)
        time.sleep(1)

finally:
    while True:
        lectura(1)
        time.sleep(1)

