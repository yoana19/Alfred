from tkinter import *
import xml.etree.ElementTree as ET
import base64

def encode(clear, key):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


    return "".join(dec)

def saveConfig():
    global emailEntry
    global passwordEntry
   
    tree = ET.parse('config.xml')
    root = tree.getroot()

    root.find('email').text = emailEntry.get()
    root.find('password').text = encode(passwordEntry.get(), "malincoh")
    tree.write('config.xml')

def runAlfred():
    import sendingMail



##class Window(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)   
##        self.master = master
##        self.init_window()
##
##    def init_window(self):


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.title("Alfred")

				

emailLabel = Label(root, text = "User e-mail")
emailLabel.grid(column=0, row=0)
emailEntry = Entry(root, bd = 10)
emailEntry.grid(column=1, row=0)
passwordLabel = Label(root, text = "Password")
passwordLabel.grid(column=0, row=1)
passwordEntry = Entry(root, show="*", bd = 10)
passwordEntry.grid(column=1, row=1)

saveButton = Button(root, text="Save configuration",command=saveConfig )
runButton = Button(root, text="Run Alfred",command=runAlfred )
saveButton.grid(column=1, row=2)
runButton.grid(column=1, row=3)

#mainloop 
root.mainloop()  
