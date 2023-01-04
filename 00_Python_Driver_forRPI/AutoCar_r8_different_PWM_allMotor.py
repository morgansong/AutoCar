# -*- coding: utf-8 -*- 
import time
import RPi.GPIO as gpio




# 定义使能引脚 
# [[13,[11,12]], [18,[15,16]], [33, [35,36]], [40, [37,38]]]

for ENA in [[13,[11,12]], [18,[15,16]], [33, [35,36]], [40, [37,38]]]:
    print(ENA)

    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)
    
    gpio.setup(ENA[1][0], gpio.OUT) 
    gpio.setup(ENA[1][1], gpio.OUT)

    gpio.output(ENA[1][1], gpio.HIGH)   #weel1-AIN1-High
    gpio.output(ENA[1][0], gpio.LOW)    #weel1-AIN2-Low

    gpio.setup(ENA[0], gpio.OUT)

    init_freq = 100  # initial frequency in Hz

    # 对使能引脚开启pwm控制
    pwm1 = gpio.PWM(ENA[0], init_freq)
    # pwm2 = gpio.PWM(ENB, 50)

    # Start pwm ,initial duty cycle in 0.0 ,10.0
    init_dc = 50  
    pwm1.start(init_dc)

    time.sleep(1)  
    
    # para_freq = 100
    # para_duty = 90
    # pwm1.ChangeFrequency(para_freq)
    # pwm1.ChangeDutyCycle(para_duty)
    
    init_dc = 90  
    pwm1.start(init_dc)
    time.sleep(2)



    
    gpio.cleanup()
    pwm1.stop()




# Change frequency and duty cycle 
# para_freq = 1000
# para_duty = 50
# pwm1.ChangeFrequency(para_freq)
# pwm1.ChangeDutyCycle(para_duty)
# time.sleep(3)
# wheel.Brake()


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
#pwm2.stop()