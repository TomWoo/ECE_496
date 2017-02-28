#include <RH_ASK.h>
#include <SPI.h> // Not actualy used but needed to compile

RH_ASK driver;

// NOTE: Pin 11 is reserved for rx.
int PIN=3;//global pin variable
int value=0;

void PWM(int pin, int val) {
  //val from 0 to 9, since I have only figured out how to get one byte input from the serial
  int conver=100+val*10;//convert the one-digit input value to the coresponding value for the pwm output
  if(val==9) conver=250;//this is only for calibration purpose
  analogWrite(pin,conver);
}

void setup() {
  pinMode(PIN,OUTPUT);
  Serial.begin(9600);
  //Serial.println("Begin");
  PWM(PIN,0);//initilisation
  
  if (!driver.init()) {
     Serial.println("init failed");
  }
}

void loop() {
  uint8_t buf[1];
  uint8_t buflen = sizeof(buf);
  if(driver.recv(buf, &buflen)) {
    char ch = *buf;
    int val=ch-'0';
    if(val!=value){
      PWM(PIN,val);
      value=val;
    }
  }
}

