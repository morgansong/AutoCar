
# -*- coding: utf-8 -*-            #通过声明可以在程序中书写中文
import RPi.GPIO as GPIO         #引入RPi.GPIO库函数命名为GPIO
import time

# BOARD编号方式，基于插座引脚编号
GPIO.setmode(GPIO.BOARD)   #将GPIO编程方式设置为BOARD模式

#接口定义
AIN1 = 11                               #将L298 AIN1口连接到树莓派Pin11
AIN2 = 12                               #将L298 AIN2口连接到树莓派Pin12

#输出模式
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)


GPIO.output(AIN1,GPIO.HIGH)   #weel1-AIN1-High
GPIO.output(AIN2,GPIO.LOW)    #weel1-AIN2-Low

time.sleep(10)

GPIO.output(AIN1,GPIO.LOW)   #weel1-AIN1-Low
GPIO.output(AIN2,GPIO.LOW)    #weel1-AIN2-Low



GPIO.output(AIN1,GPIO.LOW)   #weel1-AIN1-LOW
GPIO.output(AIN2,GPIO.HIGH)    #weel1-AIN2-HIGH




time.sleep(10)

GPIO.output(AIN1,GPIO.LOW)   #weel1-AIN1-Low
GPIO.output(AIN2,GPIO.LOW)    #weel1-AIN2-Low