yearTax = int(input())

shoes = yearTax - (yearTax * 0.40)
suit = shoes - (shoes * 0.20)
ball = suit / 4
acc = ball / 5

totalSum = shoes + suit + ball + acc + yearTax

print(totalSum)