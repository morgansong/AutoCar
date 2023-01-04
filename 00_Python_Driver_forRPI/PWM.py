import RPi.GPIO as GPIO

# Use BCM chip number as handle
GPIO.setmode(GPIO.BCM)

# Set useful channel
RELAY_1 = 20
RELAY_2 = 21
PWM_1   = 26

# Collect chip channel as setting list
output_list = [RELAY_1,RELAY_2,PWM_1]

# Set GPIO and PWM peripheral
GPIO.setup(output_list, GPIO.OUT, initial=GPIO.HIGH)
init_freq = 50  # initial frequency in Hz
pwm_pin37 = GPIO.PWM(PWM_1, init_freq)

# Set gpio as low output ,if high output then use GPIO.HIGH
GPIO.output(RELAY_1,GPIO.LOW)

# Start pwm ,initial duty cycle in 0.0 ,100.0
init_dc = 50  
pwm_pin37.start(init_dc)

# Change frequency and duty cycle
para_freq = 60
para_duty = 20
pwm_pin37.ChangeFrequency(para_freq)
pwm_pin37.ChangeDutyCycle(para_duty)

# Stop PWM out
pwm_pin37.stop()

# Release system resource and close gpio control
GPIO.cleanup()
