import sys

n = int(input())

maxNum = -sys.maxsize
sumNumbers = 0

for i in range(0, n):
    num = int(input())
    if num > maxNum:
        maxNum = num
        sumNumbers += num
if maxNum == sumNumbers - maxNum:
    print('Yes')
    print(f'Sum= {sumNumbers}')
else:
    print('No')
    sumOthers = sumNumbers - maxNum
    print(f'Diff= {abs(maxNum - sumNumbers)}')


