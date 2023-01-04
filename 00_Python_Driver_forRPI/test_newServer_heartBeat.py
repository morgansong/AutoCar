#coding: utf-8
from flask import Flask, request 
import time
import threading


app = Flask("my-app") 

default_flags = {'data':'data',"flag_start":False,"flag_go":False,"flag_speedup":False,"flag_left":False,"flag_back":False,"flag_right":False}
# flags = {} 

old_time = time.time()
current_time = old_time  


class GUI_DataShow(): 
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

                # print(flags)
                flag_go = flags["flag_go"]
                flag_speedup = flags["flag_speedup"]
                flag_left = flags["flag_left"]
                flag_back = flags["flag_back"]
                flag_right = flags["flag_right"]

                print(flag_go, flag_speedup, flag_left, flag_back, flag_right)
 
                if 'True' in str(flags):
                    print('yes, found True')
                else:
                    print('there is no Ture')

            except Exception as e:
                print('error', e)
                pass

            time.sleep(1)  #delay for car to move
 
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