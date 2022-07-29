nylon = int(input())
paint = int(input())
razor = int(input())
hoursWorkers = int(input())

priceNylon = (nylon + 2) * 1.5
pricePaint = (paint * 1.10) * 14.5
priceRazor = razor * 5

sumMaterials = priceNylon + pricePaint + priceRazor + 0.40
sumWorkers = (sumMaterials * 0.30) * hoursWorkers

totalSum = sumWorkers + sumMaterials

print(totalSum)