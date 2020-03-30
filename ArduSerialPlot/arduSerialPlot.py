#Arduino ( UNO/nano) communication to PC(Win10/Ubuntu) over pyserial example.
#Python script over pyserial get data from Arduino analog port(A0) and plotting  Matplotlib graph.
#Init to Arduino boards arduinoSerialPlot.ino before.

import serial
import matplotlib.pyplot as plt
from drawnow import *
import atexit
import time

values = []

plt.ion()
cnt = 0

#Ubuntu establish connection on a specific port:
#ser = serial.Serial('/dev/tty.usbmodem1d03', baudrate=9600, timeout=1)
# Win10 establish connection on a specific port:
serialArdu = serial.Serial('COM3', baudrate=9600, timeout=1)
time.sleep(2)

def plotValues():
    plt.title('Analog port(A0) value from Arduino')
    plt.grid(True)
    plt.ylabel('Values')
    plt.plot(values, 'rx-', label='values')
    plt.legend(loc='upper right')


def doAtExit():
    serialArdu.close()
    print("Close serial")
    print("serialArduino.isOpen() = " + str(serialArdu.isOpen()))


atexit.register(doAtExit)

print("serialArduino.isOpen() = " + str(serialArdu.isOpen()))

# pre-load dummy data
for i in range(0, 26):
    values.append(0)

while True:
    while (serialArdu.inWaiting() == 0):
        pass
    print("readline()")
    valueRead = serialArdu.readline(500)

    # check if valid value can be casted
    try:
        valueInInt = int(valueRead)
        print(valueInInt)
        if valueInInt <= 1024:
            if valueInInt >= 0:
                values.append(valueInInt)
                values.pop(0)
                drawnow(plotValues)
            else:
                print("Invalid! negative number")
        else:
            print("Invalid! too large")
    except ValueError:
        print("Invalid! cannot cast")

