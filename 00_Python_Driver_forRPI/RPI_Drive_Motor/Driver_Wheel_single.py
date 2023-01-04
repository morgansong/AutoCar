# -*- coding: utf-8 -*- 
import RPi.GPIO as GPIO

class Driver_Wheel_single():
    def __init__(self, AIN1, AIN2):
        self.AIN1 = AIN1
        self.AIN2 = AIN2
        
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.AIN1,GPIO.OUT)
        GPIO.setup(self.AIN2,GPIO.OUT)

    def Forward(self):
        GPIO.output(self.AIN1,GPIO.HIGH)   #weel1-AIN1-High
        GPIO.output(self.AIN2,GPIO.LOW)    #weel1-AIN2-Low

    def Backward(self):
        GPIO.output(self.AIN1,GPIO.LOW)   #weel1-AIN1-LOW
        GPIO.output(self.AIN2,GPIO.HIGH)    #weel1-AIN2-HIGH

    def Brake(self):
        GPIO.output(self.AIN1,GPIO.HIGH)   #weel1-AIN1-HIGH
        GPIO.output(self.AIN2,GPIO.HIGH)    #weel1-AIN2-HIGH


    def STOP(self):
        GPIO.output(self.AIN1,GPIO.LOW)   #weel1-AIN1-Low
        GPIO.output(self.AIN2,GPIO.LOW)    #weel1-AIN2-Low

