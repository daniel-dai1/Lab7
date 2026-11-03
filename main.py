from machine import Pin, PWM
from servo_translator import translate

# Initialize your servos on the Expansion board (J1, J2, J3)
shoulder = PWM(Pin(0))
shoulder.freq(50)

elbow = PWM(Pin(1))
elbow.freq(50)

wrist = PWM(Pin(2))
wrist.freq(50)
