from gpiozero import LightSensor, Buzzer, Button, CamJamKitRobot
from picamera import PiCamera
from time import sleep
from math import fabs
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import base64
import xml.etree.ElementTree as ET

def decode(enc , key):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def moveRobot():
    global robot
    motorspeed = random.randint(-100, 100)/100.0

    motorforward = (motorspeed, motorspeed)
    motorspeed = random.randint(-100, 100)/100.0
    motorbackward = (-motorspeed, -motorspeed)
    motorspeed = random.randint(-100, 100)/100.0
    motorleft = (motorspeed, 0)
    motorright = (0, motorspeed)

    robot.value = motorforward
    sleep(1)

    robot.value = motorbackward
    sleep(1)  

    robot.value = motorleft
    sleep(1)  

    robot.value = motorright
    sleep(1)  

    robot.stop()


def sendPic():    
    tree = ET.parse('config.xml')
    root = tree.getroot()

    print(root.find('email').text)
    password = root.find('password').text

    email_user = root.find('email').text
    password = decode(password,"malincoh")
    subject = 'Test email'
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_user
    msg['Subject'] = subject

    body = "Hi, there"
    msg.attach(MIMEText(body,'plain'))

    filename = 'catpic.jpg'
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)

    text = msg.as_string()

    server = smtplib.SMTP( 'smtp.gmail.com', 587 )
    server.starttls()
    server.login( email_user, password )

    server.sendmail( email_user, email_user, text )
    server.quit()

    
def takePic():
    print("ZA")
    isNotTakingPic = False
    
    print("ZA WARUDO")
    global environment
    global camera
    global ldr
    # checking if the light is sufficient to take a picture
    if ldr.value > 0.6:
        camera.start_preview()
        sleep(2)
        camera.capture('catpic.jpg')
        camera.stop_preview()
        sendPic()
    #reser all conditions including the previous and current value of the ldr, because 2 seconds have passed
    isNotTakingPic = True
    global currentValue
    currentValue = ldr.value
    global previousValue
    previousValue = ldr.value
    


#button = Button(18)
camera = PiCamera()
camera.rotation = 180
ldr = LightSensor(17)
robot = CamJamKitRobot()
print("Hello")
previousValue = ldr.value
print(ldr.value)
isNotTakingPic = True

#connecting a pushbutton to the taking of picture
#button.when_pressed = takePic

while True:
    currentValue = ldr.value
    if fabs( currentValue - previousValue ) > 0.0165 and isNotTakingPic:
        print("isNotTakingPic", isNotTakingPic)
        moveRobot()
        takePic()
    previousValue = currentValue
    sleep(0.1)






