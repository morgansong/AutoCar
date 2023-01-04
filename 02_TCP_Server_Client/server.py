#coding: utf-8
#https://www.cnblogs.com/cleven/p/10858016.html
from flask import Flask, request
import time

app = Flask("my-app")


@app.route('/myCar', methods=['POST'])
def add():
    print(request.json)
    print(request.json['angle']) 
    print(request.json['flag1']) 
    print(request.json['flag2']) 

    time.sleep(1)
    
    return "ACK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)