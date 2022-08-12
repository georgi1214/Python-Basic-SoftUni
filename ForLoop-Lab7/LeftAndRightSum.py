n = int(input())

leftSum = 0
rightSum = 0

for i in range(n):
    currentNum = int(input())
    leftSum = leftSum + currentNum
    
for i in range(n):
    currentNum = int(input())
    rightSum = rightSum + currentNum

if leftSum == rightSum:
    print(f'Yes, sum = {leftSum}')
else:
    diff = abs(leftSum - rightSum)
    print(f'No, diff = {diff}')