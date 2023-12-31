from machine import Pin, I2C, SoftI2C
from time import sleep
import bme280


i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)


while True:
    bme = bme280.BME280(i2c=i2c)
    temp = bme.values[0]
    pressure = bme.values[1]
    humidity = bme.values[2]
    reading = 'Temperature: ' + temp + '. Humidity: ' + humidity + '. Pressure: ' + pressure
    print(reading)
    sleep(1)
    



