import asyncio
import RPi.GPIO as gpio

LedVerde = 23

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(LedVerde, gpio.IN)

async def funcion_que_cuenta():
    i = 0
    while i < 10:
        await asyncio.sleep(1)
        print("i vale: {0}".format(i))
        i += 1
    print("Se cumplieron los 10 segundos")
    return i
        
async def funcion_que_espera_evento():
        
    cuenta = asyncio.ensure_future(funcion_que_cuenta())
    while gpio.input(LedVerde) == gpio.LOW:
        await asyncio.sleep(1)
        print("LA ENTRADA ESTÁ EN BAJO / MPO PENDIENTE")
        
    print("******LA ENTRADA PASÓ A ALTO / MPO FINALIZADO ANTES")
    return
 
        

evento = asyncio.ensure_future(funcion_que_espera_evento())



loop = asyncio.get_event_loop()
loop.run_forever()