#coding: utf-8
from flask import Flask, request 
import RPi.GPIO as gpio
import time
import threading


app = Flask("my-app") 

default_flags = {'data':'data',"flag_start":False,"flag_go":False,"flag_speedup":False,"flag_left":False,"flag_back":False,"flag_right":False}
# flags = {} 

old_time = time.time()
current_time = old_time  


class GUI_DataShow():
    def __init__(self): 
        gpio.setmode(gpio.BOARD)
        gpio.setwarnings(False) 

        self.Pin_Setting = [[13,[11,12]], [18,[15,16]], [33, [35,36]], [40, [37,38]]]

        for ENA in self.Pin_Setting:
            gpio.setup(ENA[0], gpio.OUT)
            gpio.setup(ENA[1][0], gpio.OUT)
            gpio.setup(ENA[1][1], gpio.OUT) 

        init_freq = 100  # initial frequency in Hz
        init_dc = 0
        self.PWM1 = gpio.PWM(self.Pin_Setting[0][0], init_freq)
        self.PWM1.start(init_dc)
        self.PWM2 = gpio.PWM(self.Pin_Setting[1][0], init_freq)
        self.PWM2.start(init_dc)
        self.PWM3 = gpio.PWM(self.Pin_Setting[2][0], init_freq)
        self.PWM3.start(init_dc)
        self.PWM4 = gpio.PWM(self.Pin_Setting[3][0], init_freq)
        self.PWM4.start(init_dc)  
        
    def Send_Control(self):
        global default_flags, flags, old_time, current_time 

        while True:  
            current_time = time.time() 
            # print('old_time',old_time)
            # print('current_time',current_time)
 
            try: 

                if float(current_time)>float(old_time) + 3:
                    # print('long time no post')
                    flags = default_flags
 
                flag_go = flags["flag_go"]
                flag_speedup = flags["flag_speedup"]
                flag_left = flags["flag_left"]
                flag_back = flags["flag_back"]
                flag_right = flags["flag_right"]
                
                print(flag_go, flag_speedup, flag_left, flag_back, flag_right)
 
                if 'True' in str(flags):
                    if flag_go:
                        print("forword")
                        for ENA in self.Pin_Setting: 
                            gpio.output(ENA[1][0], gpio.HIGH)    #weel1-AIN1-High
                            gpio.output(ENA[1][1], gpio.LOW)   #weel1-AIN2-LOW

                        self.PWM1.ChangeDutyCycle(50)
                        self.PWM2.ChangeDutyCycle(50)
                        self.PWM3.ChangeDutyCycle(50)
                        self.PWM4.ChangeDutyCycle(50)
                                
                    if flag_back:
                        print("backword")
                        for ENA in self.Pin_Setting: 
                            gpio.output(ENA[1][0], gpio.LOW)    #weel1-AIN1-Low
                            gpio.output(ENA[1][1], gpio.HIGH)   #weel1-AIN2-High
                            
                        self.PWM1.ChangeDutyCycle(50)
                        self.PWM2.ChangeDutyCycle(50)
                        self.PWM3.ChangeDutyCycle(50)
                        self.PWM4.ChangeDutyCycle(50)

                    if flag_speedup: 
                        print("forward speedup")
                        self.PWM1.ChangeDutyCycle(90)
                        self.PWM2.ChangeDutyCycle(90)
                        self.PWM3.ChangeDutyCycle(90)
                        self.PWM4.ChangeDutyCycle(90) 

                    if flag_left:
                        print("trun left")
                        self.PWM1.ChangeDutyCycle(0)
                        self.PWM2.ChangeDutyCycle(90)
                        self.PWM3.ChangeDutyCycle(0)
                        self.PWM4.ChangeDutyCycle(90)

                    if flag_right:
                        print("trun right")
                        self.PWM1.ChangeDutyCycle(90)
                        self.PWM2.ChangeDutyCycle(0)
                        self.PWM3.ChangeDutyCycle(90)
                        self.PWM4.ChangeDutyCycle(0) 
                else:
                    for ENA in self.Pin_Setting: 
                        gpio.output(ENA[1][0], gpio.LOW)    #weel1-AIN1-Low
                        gpio.output(ENA[1][1], gpio.LOW)   #weel1-AIN2-LOW

            except Exception as e:
                print('error', e)
                pass
            
            time.sleep(1)
 
    def ThreadingExample(self):
            # print("thread starts")
            self.thread = threading.Thread(target=self.Send_Control, args=())
            self.thread.daemon = False
            self.thread.start()
 
GUI_DataShow().ThreadingExample()


@app.route('/myFerrari', methods=['POST'])
def add():
    global flags, old_time, current_time 

    getJson = request.json
 
    if request.method == "POST":  
        old_time = time.time()

    if getJson['data'] == 'data':
        flags = getJson
        print('new data', flags) 

    return "ACK"


app.run(host='0.0.0.0', port=5000, debug=False)