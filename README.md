#AutoCar

project decription: 
- Flask server in Raspiberry PI
- GPIO pins to generator PWM signal to control speed of 4 motors (4wheels) through chip TB6612FNG
- battery driver for 4motors
- app in phone to generate the control signal 
- the control signal is sent out through websocket
- key notices: 
    - very short delay of sending the signal, in order to send the command out correctly without any broken between signal transfering
    - flask server to recognize the signal and control the car to change the action only when the received signal is changed

difination actions:
- default: 000000
- go: x1xxxx
- accerlate: xx1xxx
- turn left: xxx1xx
- backward: xxxx1x
- turn right: xxxxx1

2 steps for the project:
- First step:
    - raspeberry is controller
    - python code
    - control signal is pwm
    - pwm signal is to control the speed and turning
    - flask server on the car
    - 2 threads:
      - one for host (flask server)
       - one for car actions
      - data transfer by global parameters

- second step(app on phone):
    - button control
    - Java
    - websocket
    - steam control is the next version