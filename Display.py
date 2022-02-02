######################### DISPLAY.PY ###############################

# Description: Program displays data sent from TBD to GUI 
#             using tkinter library
#
# Inputs: NONE
#
# Author: Ben Capeloto
#Original use: ASEN 4018 Senior Projects DROPS team GUI Display
# Last edited by: Ben Capeloto
#Last edited date: 1/22/2022

                ###### Version History ##########
# V1.1 - 10/30/2021 - Display.py created, very basic functionality
#V2.1 = 1/22/2022 - Full overhaul. Layout change, buttons added, battery
#                   bar added, refresh added, data input added

###################################################################


##Import libraries
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

def updateData():
    data = getData()
    print("data recieved \n")
    return data

def display(winLength, winHeight, hexColor):


    data = updateData()
    ## Define Geometry and time
    geoString = str(winLength)+"x"+str(winHeight)
    startHeight = winHeight/6

    ## Battery full voltage
    battFull = 49.5

    ## Create window
    window.title("DROPS GUI V1.1") #Title the window after drops version
    window.geometry(geoString) #Set the window size
    window.configure(background=hexColor) #Set window background color in Hex

    ## Colors
    labelColorText = "#bad5f7" #Text label color hardcoded
    labelColorValue = "#9daec4" #Value label color hardcoded
    buttonBackgroundP = "#c27272" #Passive background button color
    buttonBackgroundA = "#c72020" #Active background button color
    battBar = "#049138" #Battery bar fill color
    battBack = "#e4f0e8" #battery bar background color

    ## Labels

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
    BattVolt = tk.Label(window, text = str(data['Voltage']), 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    BattVolt.pack()
    BattVolt.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 0)

    #Power status
    PowStat = tk.Label(window, text = data['Power'], 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    PowStat.pack()
    PowStat.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 1/6)

    #Cargo Status
    CargoStat = tk.Label(window, text = data['Cargo'], 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    CargoStat.pack()
    CargoStat.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 2/6)

    #Latch Status
    LatchStat = tk.Label(window, text = data['Latch'], 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    LatchStat.pack()
    LatchStat.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 3/6)

    #Timestamp
    Timestamp = tk.Label(window, text = data['TimeStamp'], 
    font=('Lekton 20'),borderwidth = 3, relief="solid", bg=labelColorValue)
    Timestamp.pack()
    Timestamp.place(relwidth=(1/2-1/3), relheight=1/6, relx = 1/3, rely = 4/6)


    ## Button for latch/unlatch
    latch = tk.Button(window, text = "Fire Latch Command", font=('Lekton 20'),borderwidth = 3,
    command = latchCommand,
    relief="solid", bg=buttonBackgroundP, activebackground=buttonBackgroundA)
    latch.pack()
    latch.place(relwidth=(1/2), relheight=1/6, relx = 0, rely = 5/6)

    
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

     ## Image or Map
    GUIimg = tk.PhotoImage(file="GUIPHOTO.ppm")
    imagePlace = tk.Label(window, borderwidth = 3,
    relief="solid", image=GUIimg)
    imagePlace.pack()
    imagePlace.place(bordermode = "outside", relwidth=1/2, relheight=4/6, 
    relx = 1/2, rely = 2/6) #Position image/map

    # ## Map and Geo Location
    # latlabel =tk.Label(window, text = "Latitude", font=('Lekton 8'), width=18, height=2)
    # latlabel.place(x=winLength/2, y=2*winHeight/6)
    # lat = tk.Label(window, text = data['Latitude'], font=('Lekton 8'), width=18, height=2)
    # lat.place(x = winLength/2+200, y=2*winHeight/6) 

    # longlabel =tk.Label(window, text = "Longitude", font=('Lekton 8'), width=18, height=2)
    # longlabel.place(x=winLength/2, y=4*winHeight/6)
    # long = tk.Label(window, text = data['Longitude'], font=('Lekton 8'), width=18, height=2)
    # long.place(x = winLength/2+200, y=4*winHeight/6) 

    ## Main loop to keep the window open
    window.mainloop()