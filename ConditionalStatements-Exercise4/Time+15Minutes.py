import math

hour = int(input())
minutes = int(input())

totalMinutes = (hour * 60) + minutes + 15
hour = totalMinutes // 60
minutes = totalMinutes % 60

if hour > 23:
    hour = 0

if minutes <= 9:
    print(f'{hour}:0{minutes}')
else:
    print(f'{hour}:{minutes}')
