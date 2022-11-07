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
   
    if(distance < 20):                  #if case for values lower than 20.
        buzzer.value = 1 - (distance / 20)  #setting the value of the pwm buzzer to 1 - (distance / 20). eg. - let distance be 15. in that case, pwm value will be 1 - 3/4 = 1/4.
        
    elif(distance >= 20):
        buzzer.value = 0

    
    sleep(1)
buzzer.off()

    

