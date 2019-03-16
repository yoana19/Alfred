from gpiozero import LightSensor, Buzzer, Button
from picamera import PiCamera
from time import sleep
from math import fabs

def takePic():
    import car
    print("ZA WARUDO")
    global environment
    global camera
    # checking if the light is sufficient to take a picture
    #if environment.value > e:
##        camera.start_preview()
##        sleep(2)
##        camera.capture('/home/pi/Desktop/catpic.jpg')
##        camera.stop_preview()
   # import sendingMail
    # TODO car movement


#button = Button(18)
##camera = PiCamera()
##camera.rotation = 180
ldr = LightSensor(17)
print("Hello")
previousValue = ldr.value
print(ldr.value)

#connecting a pushbutton to the taking of picture
#button.when_pressed = takePic

while True:
    currentValue = ldr.value
    if fabs( currentValue - previousValue ) > 0.0145:
        takePic()
    previousValue = currentValue
    sleep(0.1)






