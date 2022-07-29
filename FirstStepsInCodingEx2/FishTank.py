length = int(input())
width = int(input())
heigth = int(input())
percent = float(input())

volume = length * width * heigth

totalLiters = volume / 1000

percent = totalLiters * (percent / 100)


neededLiters = totalLiters - percent

print(neededLiters)