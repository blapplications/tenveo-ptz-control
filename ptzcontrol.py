from tkinter import *
import serial

ser = serial.Serial()
ser.baudrate = 9600
#ser.port = 'COM4'
#ser.open()
print(ser.is_open)

def run(hex):
    #ser.write(bytearray.fromhex(hex))
    print('1')

def recallPreset1():
    run('FF010007000109')

def recallPreset2():
    run('FF01000700020A')

def recallPreset3():
    run('FF01000700030B')

def recallPreset4():
    run('FF01000700040C')

def recallPreset5():
    run('FF01000700050D')

def recallPreset6():
    run('FF01000700060E')

def recallPreset7():
    run('FF01000700070F')

def recallPreset8():
    run('FF010007000810')

def recallPreset9():
    run('FF010007000911')

def up():
    run('FF010008101019')

def down():
    run('FF010010101031')
    
def left():
    run('FF010004101025')
    
def right():
    run('FF010002101023')

def stop():
    run('FF010000000001')

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

up = Button(root, text="Up", width=40, command=up).pack()
down = Button(root, text="Down", width=40, command=up).pack()
left = Button(root, text="Left", width=40, command=up).pack()
right = Button(root, text="Right", width=40, command=up).pack()

stop = Button(root, text="Stop", width=40, command=up).pack()


root.mainloop()