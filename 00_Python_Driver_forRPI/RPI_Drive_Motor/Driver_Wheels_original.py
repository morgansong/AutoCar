# -*- coding: utf-8 -*- 
import RPi.GPIO as GPIO
import time

class Driver_Wheels():
    def __init__(self):
        self.INT1 = []
        self.INT2 = []
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        self.relay = 0.1

        #wheel 1
        w1_INT1 = 12
        w1_INT2 = 11
        self.INT1.append(w1_INT1)
        self.INT2.append(w1_INT2)

        GPIO.setup(w1_INT1,GPIO.OUT)
        GPIO.setup(w1_INT2,GPIO.OUT)

        #wheel 2
        w2_INT1 = 16
        w2_INT2 = 15
        self.INT1.append(w2_INT1)
        self.INT2.append(w2_INT2)

        GPIO.setup(w2_INT1,GPIO.OUT)
        GPIO.setup(w2_INT2,GPIO.OUT)

        #wheel3
        w3_INT1 = 36
        w3_INT2 = 35
        self.INT1.append(w3_INT1)
        self.INT2.append(w3_INT2)

        GPIO.setup(w3_INT1,GPIO.OUT)
        GPIO.setup(w3_INT2,GPIO.OUT)

        #wheel4
        w4_INT1 = 38
        w4_INT2 = 37
        self.INT1.append(w4_INT1)
        self.INT2.append(w4_INT2)

        GPIO.setup(w4_INT1,GPIO.OUT)
        GPIO.setup(w4_INT2,GPIO.OUT) 

    def Forward(self):
        for i in range(len(self.INT1)):
            GPIO.output(self.INT1[i], GPIO.HIGH)   #weel1-AIN1-High
            GPIO.output(self.INT2[i], GPIO.LOW)    #weel1-AIN2-Low

        time.sleep(self.relay)
        self.STOP()

    def Backward(self):
        for i in range(len(self.INT1)):
            GPIO.output(self.INT1[i], GPIO.LOW)   #weel1-AIN1-LOW
            GPIO.output(self.INT2[i], GPIO.HIGH)    #weel1-AIN2-HIGH

        time.sleep(self.relay)
        self.STOP()

    def Forward_keeprun(self):
        for i in range(len(self.INT1)):
            GPIO.output(self.INT1[i], GPIO.HIGH)   #weel1-AIN1-High
            GPIO.output(self.INT2[i], GPIO.LOW)    #weel1-AIN2-Low 

    def Backward_keeprun(self):
        for i in range(len(self.INT1)):
            GPIO.output(self.INT1[i], GPIO.LOW)   #weel1-AIN1-LOW
            GPIO.output(self.INT2[i], GPIO.HIGH)    #weel1-AIN2-HIGH 

    def Turnright_Minidelay(self):
        #run wheel 1 and 3
        GPIO.output(self.INT1[0], GPIO.HIGH)   #weel1-AIN1-High
        GPIO.output(self.INT2[0], GPIO.LOW)    #weel1-AIN2-Low


        GPIO.output(self.INT1[2], GPIO.HIGH)   #weel1-AIN1-High
        GPIO.output(self.INT2[2], GPIO.LOW)    #weel1-AIN2-Low

        time.sleep(self.relay)
        self.STOP()


    def Trunleft_Minidelay(self):
        #run wheel 1 and 3
        GPIO.output(self.INT1[1], GPIO.HIGH)   #weel1-AIN1-High
        GPIO.output(self.INT2[1], GPIO.LOW)    #weel1-AIN2-Low


        GPIO.output(self.INT1[3], GPIO.HIGH)   #weel1-AIN1-High
        GPIO.output(self.INT2[3], GPIO.LOW)    #weel1-AIN2-Low

        time.sleep(self.relay)
        self.STOP()

    def Brake(self):
        for i in range(len(self.INT1)):
            GPIO.output(self.INT1[i], GPIO.HIGH)   #weel1-AIN1-HIGH
            GPIO.output(self.INT2[i], GPIO.HIGH)    #weel1-AIN2-HIGH
 
    def STOP(self):
        for i in range(len(self.INT1)):
            GPIO.output(self.INT1[i], GPIO.LOW)   #weel1-AIN1-Low
            GPIO.output(self.INT2[i], GPIO.LOW)    #weel1-AIN2-Low

