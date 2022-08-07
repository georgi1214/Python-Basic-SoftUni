projectionType = str(input())
r = int(input())
c = int(input())

price = 0

if projectionType == 'Premiere':
    price = (r * c) * 12
elif projectionType == 'Normal':
    price = (r * c) * 7.5
elif projectionType == 'Discount':
    price = (r * c) * 5
print(f'{price:.2f}')
