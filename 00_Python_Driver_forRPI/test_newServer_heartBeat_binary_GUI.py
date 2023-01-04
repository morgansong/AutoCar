#coding: utf-8
from flask import Flask, request 
import time
import threading


app = Flask("my-app")  

default_flags = {'data':'000000'} 
default_flags = {'data':'00000000'} 


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
                if float(current_time)>float(old_time) + 4:
                    # print('long time no post')
                    flags = default_flags
 
                getstr = flags['data']

                if getstr[1]=='1':
                    flag_go = True
                else: 
                    flag_go = False

                if getstr[2]=='1':
                    flag_speedup = True
                else: 
                    flag_speedup = False

                if getstr[3]=='1':
                    flag_left = True
                else: 
                    flag_left = False

                    
                if getstr[4]=='1':
                    flag_back = True
                else: 
                    flag_back = False

                    
                if getstr[5]=='1':
                    flag_right = True
                else: 
                    flag_right = False 

                mystr = getstr[6:8]
                
                print(int(current_time), mystr)

                #print(flag_go, flag_speedup, flag_left, flag_back, flag_right) 

                # if '1' in str(flags):
                #     print('yes, found True', flags)
                # else:
                #     print('there is no Ture', flags)

            except Exception as e:
                flags = default_flags
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
    global flags, old_time 

    flags = request.json
 
    if request.method == "POST":  
        old_time = time.time() 

    return "ACK"


app.run(host='0.0.0.0', port=5000, debug=False)
