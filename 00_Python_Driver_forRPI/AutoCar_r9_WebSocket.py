#coding: utf-8
from flask import Flask, request
import time
from RPI_Drive_Motor import Driver_Wheels 

app = Flask("my-app")
wheel = Driver_Wheels.Driver_Wheels()


@app.route('/myCar', methods=['POST'])
def add():
    # print(request.json)
    # print(request.json['angle']) 

    angle = request.json['angle']

    if angle<361:
        print(angle)
        wheel.Turn(angle) 
    else:
        wheel.STOP()


    return "ACK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)