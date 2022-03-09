##### This some jank code to collect data for dom ##########


def writeTime(io, timestamp):

    dataFile = open("data_output.txt", "a")
    dataFile.write(io+timestamp+"\n")
    dataFile.close()