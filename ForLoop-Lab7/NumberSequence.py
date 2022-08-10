import sys

n = int(input())

maxNum = -sys.maxsize
minNum = sys.maxsize

for i in range(n):
    num = int(input())
    if num > maxNum:
        maxNum = num
    if num < minNum:
        minNum = num
print(f'Max number: {maxNum}')
print(f'Min number: {minNum}')
