# -*- coding: utf-8 -*- 
import time
from RPI_Drive_Motor import Driver_Wheels 

wheel = Driver_Wheels.Driver_Wheels()


print('Forward_keeprun')
wheel.Forward_keeprun()
time.sleep(3)


print('Backward_keeprun')
wheel.Backward_keeprun()
time.sleep(3)



print('Turn 0')
wheel.Turn(0)

time.sleep(3)


print('Turn 270')
wheel.Turn(270)
time.sleep(3)
