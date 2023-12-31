#include <WiFi.h>
#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <Wire.h>

// Replace with your network credentials
const char* ssid = "";
const char* password = "";


//BME280
unsigned status;
Adafruit_BME280 bme;

//Calculated Values
double temperature;
double humidity;
double pressure;

void collect();


void setup() {
  Serial.begin(115200); //Connect to Serial
  while (!Serial);      //Pause code while we wait for Serial to connect


  // Operate in WiFi Station mode
  WiFi.mode(WIFI_STA);
 
  // Start WiFi with supplied parameters
  WiFi.begin(ssid, password);
 
  // Print periods on monitor while establishing connection
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
 
  // Connection established
  Serial.println("");
  Serial.print("Pico W is connected to WiFi network ");
  Serial.println(WiFi.SSID());
 
  // Print IP Address
  Serial.print("Assigned IP Address: ");
  Serial.println(WiFi.localIP());
 

  //Configure the BME
  Wire.setSDA(0);
  Wire.setSCL(1);

  status = bme.begin(0x77, &Wire);

  if (!status) {
    Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!");    
  } else {
    Serial.println("bme status ok");
  }


}

void loop() {
  
  delay(5000); //Wait 5 seconds
  collect();

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println("°C");

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println("%");

  Serial.print("Barometric Pressure: ");
  Serial.print(pressure);
  Serial.println(" kPa");  
}

void collect() {
  //BME280
  humidity = bme.readHumidity();
  pressure = bme.readPressure() / 1000; //Convert to kPa by dividing the result by 1000.
  temperature = bme.readTemperature();
}


