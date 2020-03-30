/*
 *If code initiated on arduino LCD_shield can take values analogVal to push a buttons.
 *Use with arduPyserialPlt.py.
*/
const int analogIn = 0;
int analogVal = 0;

void setup() {
Serial.begin(9600);
}
void loop() 
{
analogVal = analogRead(analogIn);
Serial.println(analogVal);
delay(1000); 
}
