from machine import UART, Pin
import json
import time

# Serial 
def sendUART(data, uart):
    jsonstring = json.dumps(data)
    uart.write(b'' + jsonstring + '\n\r')
    time.sleep(0.1)

# DEBUG
def readSERIAL(uart):
    rxData = bytes()
    while uart.any() > 0:
            rxData += uart.read(1)
    toprint = json.loads(rxData)
    print(toprint["file"])

# Counter
count = 0

# Porta serial
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
# Porta serial raspberry pi pico - Debug
#uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))

# Push button
front = Pin(2, Pin.IN, Pin.PULL_DOWN)
back = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Load file
text_file = open("pokemon.txt", "r")
lines = text_file.readlines()
pokemons = lines[0].split(",")
text_file.close()

# Logic
while True:
    if front.value():
        if ((count + 1) == len(pokemons)):
            count = 0
        else:
            count += 1
        
        sendUART({"file": pokemons[count] + ".bmp" }, uart)
        #readSERIAL(uart1) # Debug 
        
    if back.value():
        if ((count - 1) == -1):
            count = len(pokemons) - 1
        else:
            count -= 1
        sendUART({"file": pokemons[count] + ".bmp" }, uart)
        #readSERIAL(uart1) # Debug 
        
    time.sleep(0.5)
