#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import serial 
import mysql.connector

#Enable Serial Communication
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.01)
counter=0
rcv=[]

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="sysadmin",
  database="Autoelevadores"
)



cursor = db.cursor()
sql_insert = ""

try:
  while True:
    #print(db)
    data = ""
    print('Coloque su Tarjeta en el Lector..')
    
    #agrego linea para limpieza del puerto para evitar repeticion de lecturas
    #port.flushInput()
    
    data = port.readline()
    #print(data)
    dato = str(data)
    #print(dato)

    tagID = dato[8:]
    tagID = tagID[:8]

    tagID = '0x00'+tagID

    tagIDd = int(tagID,16)
    
    #print(tagIDd)


    if len(data) > 0:
        print(tagIDd)
        cursor.execute("SELECT id FROM Usuarios WHERE rfid_uid="+str(tagIDd))
        cursor.fetchone()

        if cursor.rowcount >= 1:

          print("Sobreescribir usuario existente?")
          overwrite = input("Sobreescribir (Y/N)? ")
          if overwrite[0] == 'Y' or overwrite[0] == 'y':
        
            print("Sobreescribiendo usuario.")
            time.sleep(1)
            sql_insert = "UPDATE Usuarios SET name = %s WHERE rfid_uid=%s"
          else:
            continue;
        else:
          sql_insert = "INSERT INTO Usuarios (name, rfid_uid) VALUES (%s, %s)"
    
        print('Ingrese nuevo Nombre')
        new_name = input("Nombre: ")

        cursor.execute(sql_insert, (new_name, str(tagIDd)))

        db.commit()

        print("Usuario " + new_name + "\nGuardado")
    
    #agrego linea para limpieza del puerto para evitar repeticion de lecturas
    port.flushInput()
    
    time.sleep(2)
finally:
    time.sleep(2)

