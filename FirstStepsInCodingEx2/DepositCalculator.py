depositSum = float(input())
months = int(input())
interest = float(input())


perYear = depositSum * (interest/100)
perMonth = perYear / 12
totalSum = depositSum + (months * perMonth)


print(totalSum)