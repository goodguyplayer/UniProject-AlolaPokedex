from machine import UART, Pin
import time

uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))

uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

button_1 = Pin(2, Pin.IN, Pin.PULL_DOWN)
button_2 = Pin(3, Pin.IN, Pin.PULL_DOWN)

while True:
    if button_1.value():
        uart1.write(b'Front\n\r')
        time.sleep(0.1)
        rxData = bytes()
        while uart0.any() > 0:
            rxData += uart0.read(1)
        print(rxData.decode('utf-8'))

    if button_2.value():
        uart0.write(b'Back\n\r')
        time.sleep(0.1)
        rxData = bytes()
        while uart1.any() > 0:
            rxData += uart1.read(1)
        print(rxData.decode('utf-8'))