import asyncio
import time
import RPi.GPIO as gpio

LedVerde = 23

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(LedVerde, gpio.IN)

def funcion_que_cuenta():
    i = 0

    while i < 10:
        time.sleep(1)
        print("i vale: ",i)
        i += 1
        if gpio.input(LedVerde) == gpio.HIGH:
            print("El MPO se completó antes")
            break
        else:
            #print("Se continua")
            continue
            
    print("Se acabó el tiempo")

try:
    while True:
        funcion_que_cuenta()
        
        time.sleep(2)
            
finally:
    i = 0

    while i < 20:
        if gpio.input(LedVerde) == gpio.LOW:
            print("El MPO se completó antes")
            break
        else:
            continue
            print("Se continua")