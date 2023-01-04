#coding: utf-8
from flask import Flask, request
import RPi.GPIO as gpio
import time

app = Flask("my-app")
Pin_Setting = [[13,[11,12]], [18,[15,16]], [33, [35,36]], [40, [37,38]]]

for ENA in Pin_Setting:
    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)
    
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


@app.route('/myCar', methods=['POST'])
def add():
    # print(request.json)
    # print(request.json['angle']) 

    angle = request.json['angle']
    print(angle)

    if angle<361:
        if 0<=angle<80:
            print("0<=angel<80")
            for ENA in Pin_Setting: 
                gpio.output(ENA[1][0], gpio.LOW)    #weel1-AIN1-Low
                gpio.output(ENA[1][1], gpio.HIGH)   #weel1-AIN2-High
            PWM1.ChangeDutyCycle(0)
            PWM2.ChangeDutyCycle(90)
            PWM3.ChangeDutyCycle(0)
            PWM4.ChangeDutyCycle(90)

        if 80<= angle <100:  
            print("80<= angel <100")
            print(Pin_Setting)
            for ENA in Pin_Setting: 
                gpio.output(ENA[1][0], gpio.HIGH)    #weel1-AIN1-HIGH
                gpio.output(ENA[1][1], gpio.LOW)   #weel1-AIN2-LOW 
            PWM1.ChangeDutyCycle(90)
            PWM2.ChangeDutyCycle(90)
            PWM3.ChangeDutyCycle(90)
            PWM4.ChangeDutyCycle(90) 
            
        if 100<= angle <260:
            print("100<= angle <260")
            for ENA in Pin_Setting: 
                gpio.output(ENA[1][0], gpio.LOW)    #weel1-AIN1-Low
                gpio.output(ENA[1][1], gpio.HIGH)   #weel1-AIN2-High
            PWM1.ChangeDutyCycle(90)
            PWM2.ChangeDutyCycle(1)
            PWM3.ChangeDutyCycle(90)
            PWM4.ChangeDutyCycle(1)
                         
            
        if 260<= angle <280: 
            print("260<= angel <280")
            for ENA in Pin_Setting: 
                gpio.output(ENA[1][0], gpio.LOW)    #weel1-AIN1-Low
                gpio.output(ENA[1][1], gpio.HIGH)   #weel1-AIN2-High
            PWM1.ChangeDutyCycle(90)
            PWM2.ChangeDutyCycle(90)
            PWM3.ChangeDutyCycle(90)
            PWM4.ChangeDutyCycle(90) 
            
        if 280<= angle <=360: 
            print("280<= angel <=360")
            for ENA in Pin_Setting: 
                gpio.output(ENA[1][0], gpio.LOW)    #weel1-AIN1-Low
                gpio.output(ENA[1][1], gpio.HIGH)   #weel1-AIN2-High
            PWM1.ChangeDutyCycle(1)
            PWM2.ChangeDutyCycle(90)
            PWM3.ChangeDutyCycle(1)
            PWM4.ChangeDutyCycle(90)

        time.sleep(1)

    else:
        print('stop')
        for ENA in Pin_Setting: 
            gpio.output(ENA[1][0], gpio.LOW)    #weel1-AIN2-LOW
            gpio.output(ENA[1][1], gpio.LOW)   #weel1-AIN1-LOW

    
    return "ACK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)