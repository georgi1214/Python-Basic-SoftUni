import math

type = input()

if type == 'square':
    width = float(input())
    result = width * width

elif type == 'rectangle':
    width = float(input())
    height = float(input())
    result = width * height

elif type == 'circle':
    square = float(input())
    result = math.pi * square * square

elif type == 'triangle':
    wight = float(input())
    height = float(input())
    result = wight * height / 2

print('%.3f'%result)


