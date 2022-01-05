from tkinter import *
import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM4'
ser.open()
print(ser.is_open)

def recallPreset1():
    ser.write(bytearray.fromhex('FF010007000100'))

def recallPreset2():
    ser.write(bytearray.fromhex('FF010007000200'))

def recallPreset3():
    ser.write(bytearray.fromhex('FF010007000300'))

def recallPreset4():
    ser.write(bytearray.fromhex('FF010007000400'))

def recallPreset5():
    ser.write(bytearray.fromhex('FF010007000500'))

def recallPreset6():
    ser.write(bytearray.fromhex('FF010007000600'))

def recallPreset7():
    ser.write(bytearray.fromhex('FF010007000700'))

def recallPreset8():
    ser.write(bytearray.fromhex('FF010007000800'))

def recallPreset9():
    ser.write(bytearray.fromhex('FF010007000900'))

root = Tk(className=" PTZ Controller")

w = Label(root, text="Camera 1").pack()

p1 = Button(root, text="Altar", width=40, command=recallPreset1).pack()
p2 = Button(root, text="Kanzel", width=40, command=recallPreset2).pack()
p3 = Button(root, text="Wide", width=40, command=recallPreset3).pack()
p4 = Button(root, text="Empore Unten Links", width=40, command=recallPreset4).pack()
p5 = Button(root, text="Empore Unten Rechts", width=40, command=recallPreset5).pack()
p6 = Button(root, text="Preset 6", width=40, command=recallPreset6).pack()
p7 = Button(root, text="Preset 7", width=40, command=recallPreset7).pack()
p8 = Button(root, text="Preset 8", width=40, command=recallPreset8).pack()
p9 = Button(root, text="Preset 9", width=40, command=recallPreset9).pack()


root.mainloop()