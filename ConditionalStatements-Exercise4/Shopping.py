import math

budget = float(input())
videoCard = int(input())
processor = int(input())
ram = int(input())

videoCardPrice = videoCard * 250
processorPrice = (videoCardPrice * 0.35) * processor
ramPrice = (videoCardPrice * 0.1) * ram

allPrice = videoCardPrice + processorPrice + ramPrice

if videoCard > processor:
    allPrice = allPrice * 0.85

diff = abs(allPrice - budget)

if budget >= allPrice:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')









