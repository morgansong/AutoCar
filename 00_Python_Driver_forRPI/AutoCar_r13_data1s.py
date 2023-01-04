#coding: utf-8
from flask import Flask, request 
import RPi.GPIO as gpio
import time
import threading


app = Flask("my-app") 

# default_flags = {'data':'data',"flag_start":False,"flag_go":False,"flag_speedup":False,"flag_left":False,"flag_back":False,"flag_right":False}
# default_flags = {'data':'000000'} 

old_time = time.time()
current_time = old_time  

str_share = '000000'
str_default = str_share


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
        global str_default, str_share, old_time, current_time 

        while True:
            print(str_share)
            current_time = time.time() 
            # print('old_time',old_time)
            # print('current_time',current_time)
 
            try: 
                if float(current_time)>float(old_time) + 1:
                    # print('long time no post')
                    str_share = str_default 
                
                if str_share[1]=='1':
                    flag_go = True
                else: 
                    flag_go = False

                if str_share[2]=='1':
                    flag_speedup = True
                else: 
                    flag_speedup = False

                if str_share[3]=='1':
                    flag_left = True
                else: 
                    flag_left = False

                    
                if str_share[4]=='1':
                    flag_back = True
                else: 
                    flag_back = False

                    
                if str_share[5]=='1':
                    flag_right = True
                else: 
                    flag_right = False 
                
                # print(flag_go, flag_speedup, flag_left, flag_back, flag_right)

                if '1' in str(str_share):
                    if flag_back:
                        print("backword")
                        for ENA in self.Pin_Setting: 
                            gpio.output(ENA[1][0], gpio.HIGH)    #weel1-AIN1-High
                            gpio.output(ENA[1][1], gpio.LOW)   #weel1-AIN2-LOW

                        self.PWM1.ChangeDutyCycle(50)
                        self.PWM2.ChangeDutyCycle(50)
                        self.PWM3.ChangeDutyCycle(50)
                        self.PWM4.ChangeDutyCycle(50)
                        
                    if flag_go:
                        print("forword")
                        for ENA in self.Pin_Setting: 
                            gpio.output(ENA[1][0], gpio.LOW)    #weel1-AIN1-Low
                            gpio.output(ENA[1][1], gpio.HIGH)   #weel1-AIN2-High
                            
                        self.PWM1.ChangeDutyCycle(50)
                        self.PWM2.ChangeDutyCycle(50)
                        self.PWM3.ChangeDutyCycle(50)
                        self.PWM4.ChangeDutyCycle(50)

                    if flag_speedup: 
                        for ENA in self.Pin_Setting: 
                            gpio.output(ENA[1][0], gpio.LOW)    #weel1-AIN1-Low
                            gpio.output(ENA[1][1], gpio.HIGH)   #weel1-AIN2-High

                        print("forward speedup")
                        self.PWM1.ChangeDutyCycle(90)
                        self.PWM2.ChangeDutyCycle(90)
                        self.PWM3.ChangeDutyCycle(90)
                        self.PWM4.ChangeDutyCycle(90) 

                    if flag_left:
                        print("trun left")
                        self.PWM1.ChangeDutyCycle(0)
                        self.PWM2.ChangeDutyCycle(50)
                        self.PWM3.ChangeDutyCycle(0)
                        self.PWM4.ChangeDutyCycle(50)

                    if flag_right:
                        print("trun right")
                        self.PWM1.ChangeDutyCycle(50)
                        self.PWM2.ChangeDutyCycle(0)
                        self.PWM3.ChangeDutyCycle(50)
                        self.PWM4.ChangeDutyCycle(0) 
                else:
                    for ENA in self.Pin_Setting: 
                        gpio.output(ENA[1][0], gpio.LOW)    #weel1-AIN1-LOW
                        gpio.output(ENA[1][1], gpio.LOW)   #weel1-AIN2-LOW

            except Exception as e:
                str_share = str_default
                print('error', e)
                pass
            
            time.sleep(0.1)
 
    def ThreadingExample(self):
            # print("thread starts")
            self.thread = threading.Thread(target=self.Send_Control, args=())
            self.thread.daemon = False
            self.thread.start()
 
GUI_DataShow().ThreadingExample()


@app.route('/myFerrari', methods=['POST'])
def add():
    global old_time, str_share

    flags = request.json
    getstr = flags['data'] 

    if getstr != str_share:
        str_share = getstr 
        # str_count = getstr

    if request.method == "POST":
        old_time = time.time() 

    return "ACK"


app.run(host='0.0.0.0', port=5000, debug=False)
