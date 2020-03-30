/*
 *If code initiated on arduino LCD_shield can take values analogVal to push a buttons.
 *Use with arduPyserialPlot.py.
*/
#include <LiquidCrystal.h>
//use Arduino LCD_shield pins
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

const int analogIn = 0;
int analogVal = 0;

void setup() {
Serial.begin(9600);
lcd.begin(16, 2);
analogWrite(10, 30); //LCD_shield brightness
}
void loop() 
{
analogVal = analogRead(analogIn);
Serial.println(analogVal);
lcd.setCursor(0, 0);
lcd.print("analogVal:> ");
lcd.print(analogVal);
delay(1000); 
lcd.clear();
}
