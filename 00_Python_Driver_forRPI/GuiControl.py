from tkinter import *
import time
from RPI_Drive_Motor import Driver_Wheels 



wheel = Driver_Wheels.Driver_Wheels()


def go_straight():
    print('Forward_keeprun') 
    wheel.Forward_keeprun()
    time.sleep(0.2)
    wheel.Brake()

def turn_left():
    print('turn right') 
    wheel.Turn(180)
    time.sleep(0.1)
    wheel.Brake()
    

def turn_right():
    print('turn right') 
    wheel.Turn(0)
    time.sleep(0.1)
    wheel.Brake()


def backward():
    print('Backward_keeprun') 
    wheel.Backward_keeprun()
    time.sleep(0.2)
    wheel.Brake()



root = Tk()
root.title("AutoCar")
# w = 400
# h = 300
# x = 600
# y = 300
# root.geometry("%dx%d+%d+%d" % (w, h, x, y))
 
wd = 20
hd = 10

Label(root, width=wd, height = hd, text ="      ").grid(column= 1, row =0)
Button(root, width=wd, height = hd, text ="Forward ",bg = 'green', command = lambda:go_straight()).grid(column= 2, row =0)
Label(root, width=wd, height = hd, text ="      ").grid(column= 3, row =0)


Button(root, width=wd, height = hd, text =" Left ",bg = 'green', command = lambda:turn_left()).grid(column= 1, row =1)
Label(root, width=wd, height = hd, text ="      ").grid(column= 2, row =1)
Button(root, width=wd, height = hd, text ="Right ",bg = 'green', command = lambda:turn_right()).grid(column= 3, row =1)


Label(root, width=wd, height = hd, text ="      ").grid(column= 1, row =2)
Button(root, width=wd, height = hd, text ="Backword",bg = 'green', command = lambda:backward()).grid(column= 2, row =2)
Label(root, width=wd, height = hd, text ="      ").grid(column= 3, row =2)
 

root.mainloop()