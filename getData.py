######################### getData.PY ###############################

# Description: get data from radio
#
# Inputs: 
#
# Author: Ben Capeloto
#Original use: ASEN 4018 Senior Projects DROPS team GUI Display
# Last edited by: Ben Capeloto
#Last edited date: 1/22/2022

                ###### Version History ##########
# V1.1 - 1/22/2022 - getData.py created, very basic functionality. test function

###################################################################

import datetime as datetime
import random


def getData():

    ## Get current date and time for testing
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    data_in = {'Voltage': round(random.uniform(35, 49.5),2), 'Power': "yes", 'Cargo': "full", 'Latch': "1/4", \
        'Latitude': "40.0150° N", 'Longitude': "105.2705° W", 'Latch 1': "Full", 'Latch 2': "Open",
        'Latch 3': "Open", 'Latch 4': "Door", 'TimeStamp': current_time}
    return data_in