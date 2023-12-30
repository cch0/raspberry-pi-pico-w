#include <Arduino.h>

int led = PIN_LED;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  digitalWrite(led, HIGH);
  Serial.println("high");

  delay(1000);

  digitalWrite(led, LOW);
  Serial.println("low");

  delay(1000);
}
