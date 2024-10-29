from gpiozero import AngularServo

import time

# Create an AngularServo object with the specified GPIO pin,

# minimum pulse width, and maximum pulse width

servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo.angle = 80

servo.angle = 80

time.sleep(2)

servo.angle = 0

time.sleep(2)

servo.angle = -80

time.sleep(2)

servo.angle = 0

time.sleep(2)

servo.value = None

print('Servo testing completed')
