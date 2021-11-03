from machine import UART, Pin
import time
import json

uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

button_1 = Pin(2, Pin.IN, Pin.PULL_DOWN)
button_2 = Pin(3, Pin.IN, Pin.PULL_DOWN)

while True:
    if button_1.value():
        texttowrite = json.dumps({"position":"Front"})
        uart1.write(b'' + texttowrite + '\n\r')
        time.sleep(0.1)
        rxData = bytes()
        while uart0.any() > 0:
            rxData += uart0.read(1)
        toprint = json.loads(rxData)
        print(toprint["position"])
        #print(rxData.decode('utf-8'))
        

    if button_2.value():
        texttowrite = json.dumps({"position":"Back"})
        uart0.write(b'' + texttowrite + '\n\r')
        time.sleep(0.1)
        rxData = bytes()
        while uart1.any() > 0:
            rxData += uart1.read(1)
        toprint = json.loads(rxData)
        print(toprint["position"])
        #print(rxData.decode('utf-8'))