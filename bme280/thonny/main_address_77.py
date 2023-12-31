from time import sleep
import bme280
import machine


i2c=machine.I2C(id=0, sda=machine.Pin(0, pull=machine.Pin.PULL_UP), scl=machine.Pin(1, pull=machine.Pin.PULL_UP), freq=200000)

print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))
    

while True:
    bme = bme280.BME280(i2c=i2c, address=0x77)
    temp = bme.values[0]
    pressure = bme.values[1]
    humidity = bme.values[2]
    reading = 'Temperature: ' + temp + '. Humidity: ' + humidity + '. Pressure: ' + pressure
    print(reading)
    sleep(1)
    
