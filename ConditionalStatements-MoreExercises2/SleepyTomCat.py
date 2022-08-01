import math

x = int(input())
y = float(input())
z = int(input())
workers = int(input())

wine = 0
sum1 = 0
sum2 = 0
sum3 = 0

needed_wine = x * y
wine = math.ceil(0.40 * needed_wine / 2.5)

if wine > z:
    sum1 = math.ceil(wine - z)
    sum2 = math.ceil(sum1 / workers)
    print(f'Good harvest this year! Total wine: {wine} liters.')
    print(f'{sum1} liters left -> {sum2} liters per person.')
elif wine < z:
    sum3 = math.ceil(z - wine)
    print(f'It will be a tough winter! More {sum3} liters wine needed.')

