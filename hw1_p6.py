import os

IIGGAtextFile = open("IIGAAmessages.txt", "w+") #creating file for processed data storage

direc = os.path.dirname(os.path.abspath(__file__)) #appending directory to open data File

with open (direc+'/NMEA0183_Data.txt','rt') as dataFile:
    for line in dataFile:
        if '$IIGGA' in line:
            IIGGAtextFile.write(line)