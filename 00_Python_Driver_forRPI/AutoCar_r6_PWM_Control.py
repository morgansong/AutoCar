# -*- coding: utf-8 -*- 
import time
from RPI_Drive_Motor import Driver_Wheels
import RPi.GPIO as gpio



wheel = Driver_Wheels.Driver_Wheels()

# 定义使能引脚
ENA = 31
ENB = 32
 

gpio.setup([ENA, ENB], gpio.OUT)

init_freq = 1000  # initial frequency in Hz

# 对使能引脚开启pwm控制
pwm1 = gpio.PWM(ENA, init_freq)
# pwm2 = gpio.PWM(ENB, 50)

# 启动pwm
pwm1.start(0)
# pwm2.start(0)

# Start pwm ,initial duty cycle in 0.0 ,10.0
init_dc = 10  
pwm1.start(init_dc)


print('forward')
wheel.Forward_keeprun()  
 
para_freq = 50
para_duty = 50
pwm1.ChangeFrequency(para_freq)
pwm1.ChangeDutyCycle(para_duty)
time.sleep(6)




# Change frequency and duty cycle 
para_freq = 1000
para_duty = 50
pwm1.ChangeFrequency(para_freq)
pwm1.ChangeDutyCycle(para_duty)
time.sleep(3)
wheel.Brake()


# print('backward')
# wheel.Backward_keeprun()  
# for i in range(11):
#     pwm1.ChangeDutyCycle(10 * i)
#     # pwm2.ChangeDutyCycle(10 * i)
#     time.sleep(1)
#     print(i,"'s speed up!")
# print("Over") 
# wheel.Brake()

 


# print('turn right')
# wheel.Turnright_Angle()  
# wheel.Brake()



# print('turn left')
# wheel.Trunleft_angle()  
# wheel.Brake()


# 释放资源
gpio.cleanup()
pwm1.stop()
#pwm2.stop()