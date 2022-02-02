######################### latchCommand.PY ###############################

# Description: sends latch/unlatch command to radio
#
# Inputs: 
#
# Author: Ben Capeloto
#Original use: ASEN 4018 Senior Projects DROPS team GUI Display
# Last edited by: Ben Capeloto
#Last edited date: 1/22/2022

                ###### Version History ##########
# V1.1 - 1/22/2022 - latchCommand.py created, very basic functionality

###################################################################

def latchCommand():
    # Send Data Asynchronously
    #homeXbee.send_data_async(remoteXbee, "Bing Bong")
    print("Latch/Unlatch Command Sent \n")