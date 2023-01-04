# -*- coding: utf-8 -*- 
import time
from RPI_Drive_Motor import Driver_Wheels


 
wheel = Driver_Wheels.Driver_Wheels()

print('forward')
wheel.Forward_keeprun() 

time.sleep(6)
wheel.Brake()

print('backward')
wheel.Backward_keeprun() 
time.sleep(6)
wheel.Brake()

 


# print('turn right')
# wheel.Turnright_Angle()  
# wheel.Brake()



# print('turn left')
# wheel.Trunleft_angle()  
# wheel.Brake()
