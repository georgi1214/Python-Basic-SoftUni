kindOfFlowers = input()
countFlowers = int(input())
budget = int(input())

price = 0


if kindOfFlowers == 'Roses':
    if countFlowers > 80:
        price = (countFlowers * 5) * 0.9
    else:
        price = countFlowers * 5
if kindOfFlowers == 'Dahlias':
    if countFlowers > 90:
        price = (countFlowers * 3.8) * 0.85
    else:
        price = countFlowers * 3.8
if kindOfFlowers == 'Tulips':
    if countFlowers > 80:
        price = (countFlowers * 2.80) * 0.85
    else:
        price = countFlowers * 2.80
if kindOfFlowers == 'Narcissus':
    if countFlowers < 120:
        price = countFlowers * 3 + (countFlowers * 3) * 0.15
    else:
        price = countFlowers * 3
if kindOfFlowers == 'Gladiolus':
    if countFlowers < 80:
        price = countFlowers * 2.50 + (countFlowers * 2.5) * 0.2
    else:
        price = countFlowers * 2.50

diff = abs(budget - price)

if budget >= price:
    print(f'Hey, you have a great garden with {countFlowers} {kindOfFlowers} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
