#Arduino ( UNO/nano) communication to PC(Win10/Ubuntu) over pyserial example.
#Init array, count avergage, write to 'dataFile.txt'
#Init to Arduino boards arduinoCharInput.ino before.
import serial
import time

#Ubuntu establish connection on a specific port:
#ser = serial.Serial('/dev/tty.usbmodem1d03', baudrate=9600, timeout=1)
# Win10 establish connection on a specific port:
ser = serial.Serial('COM3', baudrate=9600, timeout=1)
time.sleep(2)

numPoints = 10
dataList = [0]*numPoints
dataFile = open('dataFile.txt', 'w')

def getValues():
    ser.write(b'z')
    arduinoData = ser.readline().decode().split('\r\n')
    return arduinoData[0]


while (1):

    userInput = input('Get data point?: ')

    if userInput == 'y':
        for i in range(0, numPoints):
            data = getValues()
            dataFile.write(data + ', ')
            data = int(data)
            dataList[i] = data
        print(sum(dataList) / numPoints)
        print(dataList)

        dataFile.close()
        break
