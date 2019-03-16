from gpiozero import LightSensor, Buzzer, Button
from picamera import PiCamera
from time import sleep

button = Button(2)
camera = PiCamera()
camera.rotation = 180
environment = LightSensor(4)
e = 0.9
i = 0

while True:
    button.wait_for_press()
    print("ZA WARUDO")
    if environment.value > e:
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/Desktop/catpic%s.jpg' % i)
        camera.stop_preview()
        i += 1




