#LED "on/off" from Tkinter window.
#Can be used in a DC-motor-drive regulator L298N project.
#MOTOR_default.ino from arduino.

import serial
import time
import tkinter

arduino = serial.Serial('COM3', baudrate=9600, timeout=1)
time.sleep(2)

window = tkinter.Tk()
window.configure(background='gray')
window.geometry('330x120')
window.title('MOTOR CTRL - PYTHON GUI')

def motor_control():
    print(">>>MOTOR CTRL PROGRAM<<<\n")
    def forward():
        print("FORWARD>>>")
        arduino.write(b'A')

    def reverse():
        print("REVERSE<<<")
        arduino.write(b'B')

    def stop():
        print("<<STOP>>")
        arduino.write(b'C')

    def quit():
        print("\n **END PROGRAM**")
        arduino.write(b'C')
        arduino.close()
        window.destroy()

    b1 = tkinter.Button(window, text="FORWARD>>>", command=forward, bg="forest green",
                   fg="gray7", font=("Comic Sans MS", 12))
    b2 = tkinter.Button(window, text="<STOP>", command=stop, bg="gold",
                        fg="gray7", font=("Comic Sans MS", 12))
    b3 = tkinter.Button(window, text="REVERSE<<<", command=reverse, bg="firebrick2",
                   fg="ghost white", font=("Comic Sans MS", 12))
    b4 = tkinter.Button(window, text="EXIT", command=quit, bg="gold",
                   fg="gray7", font=("Comic Sans MS", 12))

    b1.grid(row=1, column=0, padx=5, pady=10)
    b2.grid(row=1, column=1, padx=5, pady=10)
    b3.grid(row=1, column=2, padx=5, pady=10)
    b4.grid(row=2, column=1, padx=5, pady=10)

    window.mainloop()


motor_control()





















