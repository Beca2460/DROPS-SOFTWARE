######################### DISPLAY.PY ###############################

# Description: Program displays data sent from TBD to GUI 
#             using tkinter library
#
# Inputs:
#
# Author: Ben Capeloto
#Original use: ASEN 4018 Senior Projects DROPS team GUI Display
# Last edited by: Ben Capeloto
#Last edited date: 2/04/2022

                ###### Version History ##########
# V1.1 - 10/30/2021 - Display.py created, very basic functionality
# V2.1 - 1/22/2022 - This is what I am running now instead of GUI.py
#V2.2 - 2/4/2022 - Integrated ConnectXbee into display

###################################################################


##Import libraries
import tkinter as tk
from digi.xbee.devices import *
import os
import datetime as datetime
import random
import numpy as np
import pandas as pd
import matplotlib as plt
plt.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from getData import getData
#from ConnectXbee import Receive, latchCommand, bootXbee
#Set system display
#os.system("Xvfb :1 -screen 0 720x720x16 &")
#os.environ['Display'] = ":0.0"




################## FUNCTIONS #################### 
   
def latchCommand():
    # Send Data Asynchronously
    homeXbee.send_data_async(remoteXbee, "FUCK!")
    print("Latch/Unlatch Command Sent \n")


def getData(dataIn=None):
    
    ## Get current date and time for testing
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if dataIn is None:
        cleanData = {'Voltage': round(random.uniform(35, 49.5),2), 'Power': "yes", 'Cargo': "full", 'Latch': "1/4", \
            'Latitude': "40.0150° N", 'Longitude': "105.2705° W", 'Latch 1': "Full", 'Latch 2': "Open",
            'Latch 3': "Open", 'Latch 4': "Door", 'TimeStamp': current_time}
    #else: 
        # Will put something here when Josh can figure out his arduino code
    return cleanData

def updateData():
    try:
        ## Recieve Data Test ##
        readData = homeXbee.read_data_from(remoteXbee, 0.5)
        remote = readData.remote_device
        data = readData.data
        is_broadcast = readData.is_broadcast
        timestamp = readData.timestamp
        print(readData.data)
        data = getData(readData)
    except TimeoutException: 
        print("No data in interval \n") 
        data = getData() 
      

    BattVolt['text'] = str(data['Voltage'])
    PowStat['text'] = data['Power']
    CargoStat['text'] = data['Cargo']
    LatchStat['text'] = data['Latch']
    Timestamp['text'] = data['TimeStamp']

    ## Latches

    Latch1['text'] = "Latch 1: " + data['Latch 1']
    Latch2['text'] = "Latch 2: " + data['Latch 2']
    Latch3['text'] = "Latch 3: " + data['Latch 3']
    Latch4['text'] = "Latch 4: " + data['Latch 4']

    if data['Latch 1'] == "Full":
        Latch1['bg'] = latchFull
    elif data['Latch 1'] == "Door":
        Latch1['bg'] = latchDoor
    else:
        Latch1['bg'] = latchOpen

    if data['Latch 2'] == "Full":
        Latch2['bg'] = latchFull
    elif data['Latch 2'] == "Door":
        Latch2['bg'] = latchDoor
    else:
        Latch2['bg'] = latchOpen

    if data['Latch 3'] == "Full":
        Latch3['bg'] = latchFull
    elif data['Latch 3'] == "Door":
        Latch3['bg'] = latchDoor
    else:
        Latch3['bg'] = latchOpen

    if data['Latch 4'] == "Full":
        Latch4['bg'] = latchFull
    elif data['Latch 4'] == "Door":
        Latch4['bg'] = latchDoor
    else:
        Latch4['bg'] = latchOpen

    ## Battery Voltage Bar 
    bar = tk.Canvas(window, borderwidth = 3,
    relief="solid", bg=battBack)
    bar.pack()
    bar.place(bordermode = "outside", relwidth=1/2, relheight=2/6, 
    relx = 1/2, rely = 0) #Position voltage bar
    x = bar.winfo_reqwidth()*(data['Voltage']/battFull)
    y = bar.winfo_reqheight()
    bar.create_rectangle(0, 0, x, y,
        fill=battBar)

    window.after(1000, updateData)

def windowParameters():

    global winLength, winHeight, hexColor, geoString, startHeight, battFull, labelColorText
    global labelColorValue, buttonBackgroundA, buttonBackgroundP, battBar, battBack, latchFull
    global latchDoor, latchOpen
    ## Set screen size and color
    winLength = 1000
    winHeight = 600
    hexColor = '#15325B'

    ## Define Geometry and time
    geoString = str(winLength)+"x"+str(winHeight)
    startHeight = winHeight/6

    ## Battery full voltage
    battFull = 49.5

    ## Colors
    labelColorText = "#bad5f7" #Text label color hardcoded
    labelColorValue = "#9daec4" #Value label color hardcoded
    buttonBackgroundP =  "#c27272" #Passive background button color
    buttonBackgroundA = "#c72020" #Active background button color
    battBar = "#049138" #Battery bar fill color
    battBack = "#e4f0e8" #battery bar background color
    latchFull = "#89f594" # Latch is Full
    latchDoor = "#f7d26d" # Latch is door
    latchOpen =  "#f28d8d" # Latch is open

def createWidgets():
    #Battery label
    Batt = tk.Label(window, text = "Battery Voltage", font=('Lekton 14'), 
    borderwidth = 3, relief="solid", bg=labelColorText) #Create Voltage label
    Batt.pack()
    Batt.place(bordermode = "outside", relwidth=1/3, relheight=1/6, relx = 0, rely = 0) #Position voltage label

    #Power label
    Pow = tk.Label(window, text = "Power Passthrough", font=('Lekton 14'), 
    borderwidth = 3, relief="solid", bg=labelColorText)
    Pow.pack()
    Pow.place(bordermode = "outside", relwidth=1/3, relheight=1/6, relx = 0, rely = 1/6)

    #Cargo label
    Cargo = tk.Label(window, text = "Cargo Bay", font=('Lekton 14'), 
    borderwidth = 3, relief="solid", bg=labelColorText)
    Cargo.pack()
    Cargo.place(bordermode = "outside", relwidth=1/3, relheight=1/6, relx = 0, rely = 2/6)

    #Latch label
    Latch = tk.Label(window, text = "Latch Status", font=('Lekton 14'),
    borderwidth = 3, relief="solid", bg=labelColorText)
    Latch.pack()
    Latch.place(bordermode = "outside", relwidth=1/3, relheight=1/6, relx = 0, rely = 3/6)

    #Time label
    Time = tk.Label(window, text = "Timestamp", font=('Lekton 14'), 
    borderwidth = 3, relief="solid", bg=labelColorText)
    Time.pack()
    Time.place(bordermode = "outside", relwidth=1/3, relheight=1/6, relx = 0, rely = 4/6)

    ## Display input values

    #Battery Voltage
    BattVolt = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    BattVolt.pack()
    BattVolt.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 0)

    #Power status
    PowStat = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    PowStat.pack()
    PowStat.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 1/6)

    #Cargo Status
    CargoStat = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    CargoStat.pack()
    CargoStat.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 2/6)

    #Latch Status
    LatchStat = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    LatchStat.pack()
    LatchStat.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 3/6)

    #Timestamp
    Timestamp = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    Timestamp.pack()
    Timestamp.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 4/6)


    ## Button for latch/unlatch
    latch = tk.Button(window, text = "Fire Latch Command", font=('Lekton 20'),borderwidth = 3,
    command = latchCommand,
    relief="solid", bg=buttonBackgroundP, activebackground=buttonBackgroundA)
    latch.pack()
    latch.place(relwidth=(1), relheight=1/6, relx = 0, rely = 5/6)


    ## Latches

    #Latch 1
    Latch1 = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=latchOpen)
    Latch1.pack()
    Latch1.place(relwidth=(1/4), relheight=1/4, relx = 1/2, rely = 2/6)

    #Latch 2
    Latch2 = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=latchOpen)
    Latch2.pack()
    Latch2.place(relwidth=(1/4), relheight=1/4, relx = 3/4, rely = 2/6)

    #Latch 3
    Latch3 = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=latchOpen)
    Latch3.pack()
    Latch3.place(relwidth=(1/4), relheight=1/4, relx = 1/2, rely = 7/12)

    #Latch 4
    Latch4 = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=latchOpen)
    Latch4.pack()
    Latch4.place(relwidth=(1/4), relheight=1/4, relx = 3/4, rely = 7/12)


## CONNECT XBEE ## 
if __name__ == "__main__":
# Instatiate home Xbee and open
    comAddress = "COM5"
    baudRate = 9600
    homeXbee = XBeeDevice(comAddress, baudRate)
    homeXbee.open(force_settings=True)

    # Instatiate remote xbee and open
    remoteXbeeAddress = "0013A200419F1EF1"
    remoteXbee = RemoteXBeeDevice(homeXbee, XBee64BitAddress.from_hex_string(remoteXbeeAddress))

    window = tk.Tk() #Window instance
    ## Create window
    windowParameters()
    window.title("DROPS GUI V2.3") #Title the window after drops version
    window.geometry(geoString) #Set the window size
    window.configure(background=hexColor) #Set window background color in Hex


    ################ CREATE WIDGETS ###################
    
    #Battery label
    Batt = tk.Label(window, text = "Battery Voltage", font=('Lekton 14'), 
    borderwidth = 3, relief="solid", bg=labelColorText) #Create Voltage label
    Batt.pack()
    Batt.place(bordermode = "outside", relwidth=1/3, relheight=1/6, relx = 0, rely = 0) #Position voltage label

    #Power label
    Pow = tk.Label(window, text = "Power Passthrough", font=('Lekton 14'), 
    borderwidth = 3, relief="solid", bg=labelColorText)
    Pow.pack()
    Pow.place(bordermode = "outside", relwidth=1/3, relheight=1/6, relx = 0, rely = 1/6)

    #Cargo label
    Cargo = tk.Label(window, text = "Cargo Bay", font=('Lekton 14'), 
    borderwidth = 3, relief="solid", bg=labelColorText)
    Cargo.pack()
    Cargo.place(bordermode = "outside", relwidth=1/3, relheight=1/6, relx = 0, rely = 2/6)

    #Latch label
    Latch = tk.Label(window, text = "Latch Status", font=('Lekton 14'),
    borderwidth = 3, relief="solid", bg=labelColorText)
    Latch.pack()
    Latch.place(bordermode = "outside", relwidth=1/3, relheight=1/6, relx = 0, rely = 3/6)

    #Time label
    Time = tk.Label(window, text = "Timestamp", font=('Lekton 14'), 
    borderwidth = 3, relief="solid", bg=labelColorText)
    Time.pack()
    Time.place(bordermode = "outside", relwidth=1/3, relheight=1/6, relx = 0, rely = 4/6)

    ## Display input values

    #Battery Voltage
    BattVolt = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    BattVolt.pack()
    BattVolt.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 0)

    #Power status
    PowStat = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    PowStat.pack()
    PowStat.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 1/6)

    #Cargo Status
    CargoStat = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    CargoStat.pack()
    CargoStat.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 2/6)

    #Latch Status
    LatchStat = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    LatchStat.pack()
    LatchStat.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 3/6)

    #Timestamp
    Timestamp = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    Timestamp.pack()
    Timestamp.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 4/6)


    ## Button for latch/unlatch
    latch = tk.Button(window, text = "Fire Latch Command", font=('Lekton 20'),borderwidth = 3,
    command = latchCommand,
    relief="solid", bg=buttonBackgroundP, activebackground=buttonBackgroundA)
    latch.pack()
    latch.place(relwidth=(1), relheight=1/6, relx = 0, rely = 5/6)


    ## Latches

    #Latch 1
    Latch1 = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=latchOpen)
    Latch1.pack()
    Latch1.place(relwidth=(1/4), relheight=1/4, relx = 1/2, rely = 2/6)

    #Latch 2
    Latch2 = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=latchOpen)
    Latch2.pack()
    Latch2.place(relwidth=(1/4), relheight=1/4, relx = 3/4, rely = 2/6)

    #Latch 3
    Latch3 = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=latchOpen)
    Latch3.pack()
    Latch3.place(relwidth=(1/4), relheight=1/4, relx = 1/2, rely = 7/12)

    #Latch 4
    Latch4 = tk.Label(window, 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=latchOpen)
    Latch4.pack()
    Latch4.place(relwidth=(1/4), relheight=1/4, relx = 3/4, rely = 7/12)



    ## Main loop to keep the window open
    updateData()
    window.mainloop()
    homeXbee.close()
    print("Closed Connection \n")
