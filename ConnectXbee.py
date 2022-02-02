######################### ConnectXbee.PY ###############################

# Description: Serial Connection to XBee Radio
#
# Inputs: 
#
# Author: Ben Capeloto
#Original use: ASEN 4018 Senior Projects DROPS team GUI Display
# Last edited by: Ben Capeloto
#Last edited date: 1/26/2022

                ###### Version History ##########
# V1.1 - 1/26/2022 - ConnectXbee.py created, very basic functionality
# V2.1 - 1/29/2022 - Sending and recieving packets between the two radios using python

###################################################################

## Libraries
from digi.xbee.devices import *
import tkinter as tk
import os
import datetime as datetime
import numpy as np
import pandas as pd
import matplotlib as plt
plt.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from getData import getData
#Set system display
#os.system("Xvfb :1 -screen 0 720x720x16 &")
#os.environ['Display'] = ":0.0"


window = tk.Tk() #Window instance

# Instatiate home Xbee and open
baudRate = 9600
homeXbee = XBeeDevice("COM5", baudRate)
homeXbee.open(force_settings=True)

# Instatiate remote xbee and open
remoteXbeeAddress = "0013A200419F1EF1"
remoteXbee = RemoteXBeeDevice(homeXbee, XBee64BitAddress.from_hex_string(remoteXbeeAddress))

def latchCommand():
    # Send Data Asynchronously
    homeXbee.send_data_async(remoteXbee, "Bing Bong")
    print("Latch/Unlatch Command Sent \n")

buttonBackgroundP = "#c27272" #Passive background button color
buttonBackgroundA = "#c72020" #Active background button color

## Set screen size and color
winLength = 1000
winHeight = 600
hexColor = '#15325B'

## Define Geometry and time
geoString = str(winLength)+"x"+str(winHeight)
startHeight = winHeight/6

## Battery full voltage
battFull = 49.5

## Create window
window.title("DROPS GUI V2.1") #Title the window after drops version
window.geometry(geoString) #Set the window size
window.configure(background=hexColor) #Set window background color in Hex

## Button for latch/unlatch
latch = tk.Button(window, text = "Fire Latch Command", font=('Lekton 20'),borderwidth = 3,
command = latchCommand,
relief="solid", bg=buttonBackgroundP, activebackground=buttonBackgroundA)
latch.pack()
latch.place(relwidth=(1/2), relheight=1/2, relx = 1/4, rely = 1/4)

## Test some code

## Send Test Data ##
#homeXbee.send_data_broadcast("Latch")
def Receive():
    try:
        ## Recieve Data Test ##
        testReadData = homeXbee.read_data_from(remoteXbee, 4)
        remote = testReadData.remote_device
        data = testReadData.data
        is_broadcast = testReadData.is_broadcast
        timestamp = testReadData.timestamp
        print(testReadData.data)
    except TimeoutException: 
        print("Timeout Exception \n")
    window.after(1000, Receive)



Receive()
window.mainloop()
homeXbee.close()
print("Closed Connection \n")
        

#finally:
    #if homeXbee is not None and homeXbee.is_open():



## RECIEVED DATA



# bytearray(b'xxxxxxxxxxxxxxxxxxxx test packet xxxxxxx')

