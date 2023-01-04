# -*- coding: utf-8 -*- 
import time
from RPI_Drive_Motor import Driver_Wheels


 
wheel = Driver_Wheels.Driver_Wheels()

 

print('turn right')

for i in range(2):
    wheel.Turnright_Minidelay()
    time.sleep(1)
wheel.Brake()
