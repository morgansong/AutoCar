# -*- coding: utf-8 -*- 
import RPi.GPIO as GPIO

class Driver_Wheels():
    def __init__(self):
        self.INT1 = []
        self.INT2 = []

        #def PWM
        # self.PWM = []
        init_freq = 100

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False) 
        GPIO.setup([13, 18, 33, 40], GPIO.OUT)

        #wheel 1
        w1_INT1 = 11
        w1_INT2 = 12
        EN1 =13
        self.INT1.append(w1_INT1)
        self.INT2.append(w1_INT2)
        self.PWM1 = GPIO.PWM(EN1, init_freq)

        #wheel 2
        w2_INT1 = 15
        w2_INT2 = 16
        EN2 =18
        self.INT1.append(w2_INT1)
        self.INT2.append(w2_INT2)
        self.PWM2 = GPIO.PWM(EN2, init_freq)

        #wheel3
        w3_INT1 = 35
        w3_INT2 = 36
        EN3 = 33
        self.INT1.append(w3_INT1)
        self.INT2.append(w3_INT2)
        self.PWM3 = GPIO.PWM(EN3, init_freq)

        #wheel4
        w4_INT1 = 37
        w4_INT2 = 38
        EN4 = 40
        self.INT1.append(w4_INT1)
        self.INT2.append(w4_INT2)
        self.PWM4 = GPIO.PWM(EN4, init_freq) 

        GPIO.setup(self.INT1,GPIO.OUT)
        GPIO.setup(self.INT2,GPIO.OUT) 

        #start the PCB with 100% duty cycle
        self.PWM1.start(80)
        self.PWM2.start(80)
        self.PWM3.start(80)
        self.PWM4.start(80)

    def Forward_keeprun(self):
        for i in range(len(self.INT1)):
            GPIO.output(self.INT1[i], GPIO.HIGH)   #weel1-AIN1-High
            GPIO.output(self.INT2[i], GPIO.LOW)    #weel1-AIN2-Low
        
        self.PWM1.ChangeDutyCycle(80)
        self.PWM2.ChangeDutyCycle(80)
        self.PWM3.ChangeDutyCycle(80)
        self.PWM4.ChangeDutyCycle(80)

    def Backward_keeprun(self):
        for i in range(len(self.INT1)):
            GPIO.output(self.INT1[i], GPIO.LOW)   #weel1-AIN1-LOW
            GPIO.output(self.INT2[i], GPIO.HIGH)    #weel1-AIN2-HIGH
        
        self.PWM1.ChangeDutyCycle(80)
        self.PWM2.ChangeDutyCycle(80)
        self.PWM3.ChangeDutyCycle(80)
        self.PWM4.ChangeDutyCycle(80)

    def Turn(self, angel):
        if 0<=angel<80:
            print("0<=angel<80")
            for i in range(len(self.INT1)):
                # self.Backward_keeprun()
                GPIO.output(self.INT1[i], GPIO.LOW)   #weel1-AIN1-LOW
                GPIO.output(self.INT2[i], GPIO.HIGH)    #weel1-AIN2-HIGH
            self.PWM1.ChangeDutyCycle(0)
            self.PWM2.ChangeDutyCycle(90)
            self.PWM3.ChangeDutyCycle(0)
            self.PWM4.ChangeDutyCycle(90)

        if 80<= angel <100: 
            print("80<= angel <100")
            for i in range(len(self.INT1)):
                # self.Backward_keeprun()
                GPIO.output(self.INT1[i], GPIO.LOW)   #weel1-AIN1-LOW
                GPIO.output(self.INT2[i], GPIO.HIGH)    #weel1-AIN2-HIGH
            self.PWM1.ChangeDutyCycle(80)
            self.PWM2.ChangeDutyCycle(80)
            self.PWM3.ChangeDutyCycle(80)
            self.PWM4.ChangeDutyCycle(80) 

        if 100<= angel <170:
            print("100<= angel <170")
            for i in range(len(self.INT1)):
                # self.Backward_keeprun()
                GPIO.output(self.INT1[i], GPIO.LOW)   #weel1-AIN1-LOW
                GPIO.output(self.INT2[i], GPIO.HIGH)    #weel1-AIN2-HIGH
            self.PWM1.ChangeDutyCycle(90)
            self.PWM2.ChangeDutyCycle(1)
            self.PWM3.ChangeDutyCycle(90)
            self.PWM4.ChangeDutyCycle(1)
        
        if 170<= angel < 190:
            print("170<= angel < 190")
            for i in range(len(self.INT1)):
                GPIO.output(self.INT1[i], GPIO.HIGH)   #weel1-AIN1-High
                GPIO.output(self.INT2[i], GPIO.LOW)    #weel1-AIN2-Low
            self.PWM1.ChangeDutyCycle(80)
            self.PWM2.ChangeDutyCycle(80)
            self.PWM3.ChangeDutyCycle(80)
            self.PWM4.ChangeDutyCycle(80) 
        
        if 190<= angel <260: 
            print("190<= angel <260")
            for i in range(len(self.INT1)):
                GPIO.output(self.INT1[i], GPIO.HIGH)   #weel1-AIN1-High
                GPIO.output(self.INT2[i], GPIO.LOW)    #weel1-AIN2-Low
            self.PWM1.ChangeDutyCycle(90)
            self.PWM2.ChangeDutyCycle(1)
            self.PWM3.ChangeDutyCycle(90)
            self.PWM4.ChangeDutyCycle(1)

        if 260<= angel <280: 
            print("260<= angel <280")
            for i in range(len(self.INT1)):
                GPIO.output(self.INT1[i], GPIO.HIGH)   #weel1-AIN1-High
                GPIO.output(self.INT2[i], GPIO.LOW)    #weel1-AIN2-Low
            self.PWM1.ChangeDutyCycle(80)
            self.PWM2.ChangeDutyCycle(80)
            self.PWM3.ChangeDutyCycle(80)
            self.PWM4.ChangeDutyCycle(80) 
        
        if 280<= angel <=360: 
            print("280<= angel <=360")
            for i in range(len(self.INT1)):
                GPIO.output(self.INT1[i], GPIO.HIGH)   #weel1-AIN1-High
                GPIO.output(self.INT2[i], GPIO.LOW)    #weel1-AIN2-Low
            self.PWM1.ChangeDutyCycle(1)
            self.PWM2.ChangeDutyCycle(90)
            self.PWM3.ChangeDutyCycle(1)
            self.PWM4.ChangeDutyCycle(90)
        
    def Brake(self):
        for i in range(len(self.INT1)):
            GPIO.output(self.INT1[i], GPIO.HIGH)   #weel1-AIN1-HIGH
            GPIO.output(self.INT2[i], GPIO.HIGH)    #weel1-AIN2-HIGH
 
    def STOP(self):
        for i in range(len(self.INT1)):
            GPIO.output(self.INT1[i], GPIO.LOW)   #weel1-AIN1-Low
            GPIO.output(self.INT2[i], GPIO.LOW)    #weel1-AIN2-Low

