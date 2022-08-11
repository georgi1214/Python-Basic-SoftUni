countOfNumbers = int(input())

oddSum = 0
evenSum = 0

for position in range(1,countOfNumbers + 1):
    currentNumber = int(input())
    if position % 2 == 0:
        evenSum += currentNumber
    else:
        oddSum += currentNumber
if oddSum == evenSum:
    print('Yes')
    print(f'Sum = {evenSum}')
else:
    print('No')
    print(f'Diff = {abs(evenSum - oddSum)}')







