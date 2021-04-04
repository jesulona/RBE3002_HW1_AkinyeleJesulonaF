import math

velMs = float(raw_input("Enter desired Velocity: "))

wB = 0.156 #wheel base
wD = 0.065 #wheel diameter

d1Rev = (math.pi)*wD #distace covered w. one wheel rev

revS = velMs/d1Rev #rps at desired speed

rpmL = round(revS*60,2)
rpmR = round(revS*60,2)

wVel = [rpmL,rpmR]

print(wVel)