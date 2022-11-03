import time                             
from time import sleep                  #importing time library and its sleep function
import RPi.GPIO as pin                  
from gpiozero import DistanceSensor
from gpiozero import PWMLED

pin.setmode(pin.BOARD)                  #using GPIO naming convention

buzzer = PWMLED(18)                     #setting GPIO 18 as pin for buzzer, as it is a PWM pin.
sensor = DistanceSensor(echo=23, trigger=24)    #setting ultrasonic sensor and definig its pins

while True:                             #while loop for if any value is availible
    distance = sensor.distance * 100    #converting distance calculated from sensor into cm from metre
    print('Distance = ', distance)      #printing the value to terminal
    if (distance > 20):                 #if else loop to change the value of buzzer dependong upon the distance.
        buzzer.value = 0
    elif (distance < 20 and distance > 15):
        buzzer.value = 0.25
    elif (distance < 15 and distance > 10):
        buzzer.value = 0.5
    elif (distance < 10 and distance > 8):
        buzzer.value = 0.75
    elif (distance < 8):
        buzzer.value = 1

    
    sleep(1)

buzzer.off()
    

    

