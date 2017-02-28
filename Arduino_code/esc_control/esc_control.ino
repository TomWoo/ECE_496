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
  Serial.println("Begin");
  PWM(PIN,0);//initilisation
}

void loop() {
  if(Serial.available()) {
    char ch=Serial.read();//I think this is the name of that function
    int val=ch-'0';
    if(val!=value){
      PWM(PIN,val);
      value=val;
    }
  }
}

