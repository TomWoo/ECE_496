#include <RH_ASK.h>
#include <SPI.h> // Not actually used but needed to compile

RH_ASK driver;

// NOTE: Pin 12  is reserved for tx.
char *msg = "0";

void setup() {
  Serial.begin(9600);
  Serial.println("Begin"); // TODO: remove all prints
  if (!driver.init()) {
     Serial.println("init failed");
  }
}

void loop() {
  if(Serial.available()) {
    *msg = Serial.read();
    driver.send((uint8_t *)msg, strlen(msg));
    driver.waitPacketSent();
    Serial.println("sent");
    delay(100); // TODO: reduce
  }
}

