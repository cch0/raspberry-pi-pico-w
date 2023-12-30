from machine import Pin
import time

led = Pin('LED', Pin.OUT)

while True:
    led.toggle()
    print(led.value())
    time.sleep(1.0)
    
