//check condition Serial.available()>0
//read data from analogPin0 and print if condition "z" true
//if condition "c" true print timestamp
//used together with arduSerialCom7.py
  
int analogPin = 0;     
int data = 0;           
char userInput;
unsigned long currentTime =0;
unsigned long previousTime = 0;

void setup(){
  Serial.begin(9600);  //setup serial
  //Serial.println("333");
}

void loop(){

if(Serial.available()> 0){ 
    
    userInput = Serial.read();               // read user input
      
      if(userInput == 'z'){                  // if we get expected value 

            data = analogRead(analogPin);    // read the input pin
            Serial.println(data);                       
      } 
      if(userInput ==  'c'){
        previousTime = currentTime;
        currentTime = millis();

        data = analogRead(analogPin);
        Serial.print(data);
        Serial.print('-');
        Serial.print(currentTime-previousTime);
        Serial.println("ms");
      }       
 } 
} 
