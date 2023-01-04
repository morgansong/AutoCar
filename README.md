#AutoCar


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