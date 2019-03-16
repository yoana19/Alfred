from gpiozero import LightSensor, Buzzer, Button
from math import fabs
from time import sleep

##button = Button(2)
##button.wait_for_press()
##print('You pushed me')
##print("Hello")
ldr = LightSensor(17)
print("Hello")
previousValue = ldr.value
print(ldr.value)
while True:
    currentValue = ldr.value
##    print(currentValue)
##    print(previousValue)
    
    if fabs( currentValue - previousValue ) > 0.0145:
        print("You moved")
    previousValue = currentValue
    sleep(0.1)
