budget = float(input())
countStatist = int(input())
priceClothing = float(input())

decorPrice = budget * 0.10
allClothes = countStatist * priceClothing

if countStatist > 150:
    allClothes = allClothes * 0.90
totalExpenses = allClothes + decorPrice

diff = abs(totalExpenses - budget)
if budget >= totalExpenses:
    print(f'Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print(f'Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')