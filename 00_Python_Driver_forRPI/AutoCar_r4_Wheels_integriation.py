# -*- coding: utf-8 -*- 
import time
from RPI_Drive_Motor import Driver_Wheels_All


 
wheel = Driver_Wheels_All.Driver_Wheels_All()

wheel.Forward()
time.sleep(0.5)
wheel.STOP()

time.sleep(0.5)

wheel.Backward()
time.sleep(0.5)
wheel.STOP()


 


