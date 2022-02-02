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

    data_in = {'Voltage': round(random.uniform(35, 49.5),2), 'Power': "yes", 'Cargo': "full", 'Latch': "door", \
        'Latitude': "40.0150° N", 'Longitude': "105.2705° W", 'TimeStamp': current_time}
    return data_in