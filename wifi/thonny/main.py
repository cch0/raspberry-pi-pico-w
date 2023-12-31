from time import sleep
from machine import Pin, I2C
import network
import socket
import bme280

ssid = '' #Your network name
password = '' #Your WiFi password

#initialize I2C 
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

def connect():
    max_retry=20
    retry=0
    
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while wlan.isconnected() == False and retry < max_retry:
        print('Waiting for connection...')
        sleep(1)
        retry += 1
        
        
    if wlan.isconnected():            
        ip = wlan.ifconfig()[0]
        print(f'Connected on {ip}')
        return ip
    else:
        print('WIFI Not connected')
        return None


def collect():
    print('start collecting...')
    
    while True:
        bme = bme280.BME280(i2c=i2c, address=0x77)
        temp = bme.values[0]
        pressure = bme.values[1]
        humidity = bme.values[2]
        reading = 'Temperature: ' + temp + '. Humidity: ' + humidity + '. Pressure: ' + pressure        
        print(reading)
        sleep(5)


ip = connect()

if ip is None:
    print('no ip acquired')

collect()





