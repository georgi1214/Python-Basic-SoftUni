import math

recordInSec = float(input())
distance = float(input())
timeInSecForOne = float(input())

totalTime = distance * timeInSecForOne

resistTime = math.floor(distance / 15) * 12.5
totalTime = totalTime + resistTime

if totalTime < recordInSec:
    print(f'Yes, he succeeded! The new world record is {totalTime:.2f} seconds.')
else:
    diff = totalTime - recordInSec
    print(f'No, he failed! He was {diff:.2f} seconds slower.')
