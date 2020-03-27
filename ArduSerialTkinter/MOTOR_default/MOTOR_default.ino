//Use with MOTOR_default.py (tkinter exampl)

int greenLed = 5;
int redLed = 6;
char data;

void setup() {
  Serial.begin(9600);
  Serial.println("startas");
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);
  digitalWrite(greenLed,LOW);
  digitalWrite(redLed,LOW);
}

void loop() {
  while(Serial.available()>0)
  {
    data = Serial.read();
  }
  if (data =='A')
  {
    digitalWrite(greenLed,HIGH);
    digitalWrite(redLed,LOW);
    delay(10);
    Serial.println("greenLED on");
  }
  if (data =='B')
  {
    digitalWrite(redLed,HIGH);
    digitalWrite(greenLed,LOW);
    delay(10);
    Serial.println("redLED on");
  }
  if (data =='C')
  {
    digitalWrite(redLed,LOW);
    digitalWrite(greenLed,LOW);
    delay(10);
    Serial.println("LEDs off");
  }
}
