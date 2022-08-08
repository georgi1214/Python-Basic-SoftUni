degrees = int(input())
timeOfDay = input()

if timeOfDay == 'Morning':
    if degrees <= 10 or degrees <= 18:
        print(f"It's {degrees} degrees, get your {'Sweatshirt'} and {'Sneakers'}.")
    elif degrees < 18 or degrees <= 24:
        print(f"It's {degrees} degrees, get your {'Shirt'} and {'Moccasins'}.")
    else:
        print(f"It's {degrees} degrees, get your {'T-Shirt'} and {'Sandals'}.")
elif timeOfDay == 'Afternoon':
    if degrees <= 10 or degrees <= 18:
        print(f"It's {degrees} degrees, get your {'Shirt'} and {'Moccasins'}.")
    elif degrees < 18 or degrees <= 24:
        print(f"It's {degrees} degrees, get your {'T-Shirt'} and {'Sandals'}.")
    else:
        print(f"It's {degrees} degrees, get your {'Swim Suit'} and {'Barefoot'}.")
elif timeOfDay == 'Evening':
    if degrees <= 10 or degrees <= 18:
        print(f"It's {degrees} degrees, get your {'Shirt'} and {'Moccasins'}.")
    elif degrees < 18 or degrees <= 24:
        print(f"It's {degrees} degrees, get your {'Shirt'} and {'Moccasins'}.")
    else:
        print(f"It's {degrees} degrees, get your {'Shirt'} and {'Moccasins'}.")