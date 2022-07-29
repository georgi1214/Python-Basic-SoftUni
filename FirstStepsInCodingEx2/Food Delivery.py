chicken = int(input())
fish = int(input())
vegan = int(input())

chicenMenu = chicken * 10.35
fishMenu = fish * 12.40
veganMenu = vegan * 8.15

menuPrice = chicenMenu + fishMenu + veganMenu
desert = menuPrice * 0.2

allPrice = menuPrice + desert + 2.5
print(allPrice)


