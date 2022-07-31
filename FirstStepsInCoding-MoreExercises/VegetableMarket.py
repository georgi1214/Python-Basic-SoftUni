vedji = float(input())
fruit = float(input())
allVedji = int(input())
allFruit = int(input())

priceVedji = vedji * allVedji
priceFruit = fruit * allFruit

allPrice = priceFruit + priceVedji
price = allPrice / 1.94


print('\n %.2f'%price)