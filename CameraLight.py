from gpiozero import LightSensor, Buzzer, Button
from picamera import PiCamera
from time import sleep

def takePic():
    print("ZA WARUDO")
    global environment
    global e
    global camera
    # checking if the light is sufficient to take a picture
    if environment.value > e:
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/Desktop/catpic.jpg')
        camera.stop_preview()
    import sendingMail
    # TODO car movement


button = Button(2)
camera = PiCamera()
camera.rotation = 180
environment = LightSensor(4)
e = 0.9

#connecting a pushbutton to the taking of picture
button.when_pressed = takePic

# TODO detect movement





