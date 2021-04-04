import os

Lat = []     #empty list to store Lat info
Long = []    #empty list to store Long info

direc = os.path.dirname(os.path.abspath(__file__)) #appending directory to open data File

with open (direc+'/IIGAAmessages.txt','rt') as dataFile:

    firstLine = dataFile.readline().strip() #read first line 
    firstLineList = firstLine.split(",")    #determine heading based on first line
    NS = firstLineList[3]
    EW = firstLineList[5]

    for line in dataFile:
        info = line.split(",") #Split data into individual parts
        Lat.append(info[2])    #add to list of Lat
        Long.append(info[4])   #add to list og Long

Llat = [float(n) for n in Lat if n]                   #ensure data is clean 
avgLat = sum(Llat)/len(Llat) if Llat else '-'         #take average 

Llong = [float(n) for n in Long if n]                 #ensure data is clean 
avgLong = sum(Llong)/len(Llong) if Llong else '-'     #take average   

dataAvg = [round(avgLat,2), NS, round(avgLong,2), EW] #rounded final data output

print(dataAvg)