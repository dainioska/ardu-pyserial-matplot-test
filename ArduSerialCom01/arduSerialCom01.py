#Two Arduino boards( UNO/nano) communication to PC(Win10/Ubuntu) over pyserial example.
#Init to Arduino boards arduinoCharInput.ino before.
import serial
import time

#Ubuntu establish connection on a specific port:
#ser5 = serial.Serial('/dev/tty.usbmodem1d05', baudrate=9600, timeout=1)
#ser6 = serial.Serial('/dev/tty.usbmodem1d06', baudrate=9600, timeout=1)
# Win10 establish connection on a specific port:
ser5 = serial.Serial('COM5', baudrate=9600, timeout=1)
ser6 = serial.Serial('COM6', baudrate=9600, timeout=1)
time.sleep(2)

def getValues5():
    ser5.write(b'z')
    arduinoData5 = ser5.readline().decode('ascii')
    return arduinoData5

def getValues6():
    ser6.write(b'z')
    arduinoData6 = ser6.readline().decode('ascii')
    return arduinoData6

while (1):

    userInput = input('Get data point?: ')

    if userInput == 'y':
        print(getValues5() + getValues6())
