######################### DISPLAY.PY ###############################

# Description: Program displays data sent from TBD to GUI 
#             using tkinter library
#
# Inputs:
#
# Author: Ben Capeloto
#Original use: ASEN 4018 Senior Projects DROPS team GUI Display
# Last edited by: Ben Capeloto
#Last edited date: 1/22/2022

                ###### Version History ##########
# V1.1 - 10/30/2021 - Display.py created, very basic functionality
# V2.1 - 1/22/2022 - This is what I am running now instead of GUI.py

###################################################################


##Import libraries
import tkinter as tk
import os
import datetime as datetime
import numpy as np
import pandas as pd
import matplotlib as plt
plt.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from latchCommand import latchCommand
from getData import getData
#Set system display
#os.system("Xvfb :1 -screen 0 720x720x16 &")
#os.environ['Display'] = ":0.0"


window = tk.Tk() #Window instance

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

## Colors
labelColorText = "#bad5f7" #Text label color hardcoded
labelColorValue = "#9daec4" #Value label color hardcoded
buttonBackgroundP = "#c27272" #Passive background button color
buttonBackgroundA = "#c72020" #Active background button color
battBar = "#049138" #Battery bar fill color
battBack = "#e4f0e8" #battery bar background color

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
latch.place(relwidth=(1/2), relheight=1/6, relx = 0, rely = 5/6)

## Image or Map
GUIimg = tk.PhotoImage(file="Images\GUIPHOTO.PPM")
imagePlace = tk.Label(window, borderwidth = 3,
relief="solid", image=GUIimg)
imagePlace.pack()
imagePlace.place(bordermode = "outside", relwidth=1/2, relheight=4/6, 
relx = 1/2, rely = 2/6) #Position image/map

def updateData():
    data = getData()
    print("data recieved \n")

    BattVolt['text'] = str(data['Voltage'])
    PowStat['text'] = data['Power']
    CargoStat['text'] = data['Cargo']
    LatchStat['text'] = data['Latch']
    Timestamp['text'] = data['TimeStamp']
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


## Main loop to keep the window open
updateData()
window.mainloop()