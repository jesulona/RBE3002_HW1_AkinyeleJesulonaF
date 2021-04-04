import math

wB = 0.156 #wheel base
wD = 0.065 #wheel diameter

traj = raw_input("Enter the vel, dir and ICC separated by space: ")
info = traj.split(" ") # Split string into words

#if 3 inputs found

if len(info) == 3 :        
    vel = float(info[0])
    dir = str(info[1])
    ICC = float(info[2])
    if ICC != 0 :                              #if real ICC
        w = vel/ICC
        vR = w*(ICC + wB/2)
        vL = w*(ICC - wB/2)
        wR = vR/0.5*wD
        wL = vL/0.5*wD
        rRPM = round((wR/2*(math.pi))*60,2)
        lRPM = round((wL/2*(math.pi))*60,2)
        if dir in ('F','f') and ICC < 0 :
            rRPM = rRPM
            lRPM = rRPM
        elif dir in ('F','f') and ICC > 0 :
            swap = lRPM
            lRPM = rRPM
            rRPM = swap
        elif dir in ('R','r') and ICC < 0 :
            rRPM = -rRPM
            lRPM = -lRPM
        elif dir in ('R','r') and ICC > 0 :
            swap = lRPM
            lRPM = -rRPM
            rRPM = -swap
    else :                                      #else ICC is point turn
        d1Rev = (math.pi)*wD 
        revS = vel/d1Rev #rps at desired speed
        lRPM = round(revS*60,2)
        rRPM = round(revS*60,2)
        if dir in ('F','f') :
            rRPM = -rRPM
        else :
            lRPM = -lRPM      

#only 2 inputs given  

else:   
    vel = float(info[0])
    dir = str(info[1])

    d1Rev = (math.pi)*wD 
    revS = vel/d1Rev #rps at desired speed
    lRPM = round(revS*60,2)
    rRPM = round(revS*60,2)
    if dir in ('R','r'):
        lRPM = -lRPM
        rRPM = -rRPM

wVel = [lRPM,rRPM] #final lRPM and rRPM based off variable input

if vel > 0.22: #speed limit check
    print('Invalid Velocity Request!')
else:
    print(wVel)

    
