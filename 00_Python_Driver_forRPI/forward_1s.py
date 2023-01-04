# -*- coding: utf-8 -*- 
import time
from RPI_Drive_Motor import Driver_Wheels


 
wheel = Driver_Wheels.Driver_Wheels()
 

print('backward')
wheel.Backward_keeprun() 
time.sleep(1)
wheel.Brake()

 
 