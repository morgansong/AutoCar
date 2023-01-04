import RPi.GPIO as gpio
import time
import random
 


gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)


Pin_Setting = [[13,[11,12]], [18,[15,16]], [33, [35,36]], [40, [37,38]]]

for ENA in Pin_Setting:
    
    gpio.setup(ENA[0], gpio.OUT)
    gpio.setup(ENA[1][0], gpio.OUT) 
    gpio.setup(ENA[1][1], gpio.OUT)



init_freq = 100  # initial frequency in Hz
init_dc = 10
PWM1 = gpio.PWM(Pin_Setting[0][0], init_freq)
PWM1.start(init_dc)
PWM2 = gpio.PWM(Pin_Setting[1][0], init_freq)
PWM2.start(init_dc)
PWM3 = gpio.PWM(Pin_Setting[2][0], init_freq)
PWM3.start(init_dc)
PWM4 = gpio.PWM(Pin_Setting[3][0], init_freq)
PWM4.start(init_dc)


def try_angle(angel):
    print(angel)
    if angel<361:
        if 0<=angel<=180: 
            print("backword")
            for ENA in Pin_Setting: 
                gpio.output(ENA[1][0], gpio.LOW)    #weel1-AIN1-Low
                gpio.output(ENA[1][1], gpio.HIGH)   #weel1-AIN2-High
        else: 
            print("forword")
            for ENA in Pin_Setting: 
                gpio.output(ENA[1][0], gpio.HIGH)    #weel1-AIN1-High
                gpio.output(ENA[1][1], gpio.LOW)   #weel1-AIN2-LOW

        PWM1.ChangeDutyCycle(0)
        PWM2.ChangeDutyCycle(0)
        PWM3.ChangeDutyCycle(0)
        PWM4.ChangeDutyCycle(0)
            
        if 0<=angel<80:
            PWM1.ChangeDutyCycle(0)
            PWM2.ChangeDutyCycle(90)
            PWM3.ChangeDutyCycle(0)
            PWM4.ChangeDutyCycle(90)

        if 80<= angel <100:  
            print("80<= angel <100") 
            PWM1.ChangeDutyCycle(90)
            PWM2.ChangeDutyCycle(90)
            PWM3.ChangeDutyCycle(90)
            PWM4.ChangeDutyCycle(90) 
            
        if 100<= angel <180:
            print("80<= angel <180") 
            PWM1.ChangeDutyCycle(90)
            PWM2.ChangeDutyCycle(1)
            PWM3.ChangeDutyCycle(90)
            PWM4.ChangeDutyCycle(1) 
                        
        if 180<= angel <260: 
            print("180<= angel <260")
            PWM1.ChangeDutyCycle(90)
            PWM2.ChangeDutyCycle(1)
            PWM3.ChangeDutyCycle(90)
            PWM4.ChangeDutyCycle(1)
            
        if 260<= angel <280: 
            print("260<= angel <280") 
            PWM1.ChangeDutyCycle(90)
            PWM2.ChangeDutyCycle(90)
            PWM3.ChangeDutyCycle(90)
            PWM4.ChangeDutyCycle(90) 
            
        if 280<= angel <=360: 
            print("280<= angel <=360:")
            PWM1.ChangeDutyCycle(1)
            PWM2.ChangeDutyCycle(90)
            PWM3.ChangeDutyCycle(1)
            PWM4.ChangeDutyCycle(90)

        time.sleep(0.1)
 
        # print('break')
        # for ENA in Pin_Setting: 
        #     gpio.output(ENA[1][0], gpio.HIGH)    #weel1-AIN2-HIGH
        #     gpio.output(ENA[1][1], gpio.HIGH)   #weel1-AIN1-High

 
for k in range(5):
    angle = random.randint(0,80)
    try_angle(angle)


    
for k in range(5):
    angle = random.randint(280,360)
    try_angle(angle)



for k in range(5):
    angle = random.randint(180,260)
    try_angle(angle)



for k in range(5):
    angle = random.randint(100,180)
    try_angle(angle)

for k in range(5):
    angle = random.randint(80,100)
    try_angle(angle)

    

for k in range(5):
    angle = random.randint(260,280)
    try_angle(angle)
