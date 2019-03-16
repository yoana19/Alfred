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

filename = "test.png"
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
