budget = float(input())
season = input()

price = 0
destination = ''
hotelCamp = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'Summer':
        price = budget * 0.3
        hotelCamp = 'Camp'
    else:
        price = budget * 0.7
        hotelCamp = 'Hotel'

elif budget <= 1000:
    destination = 'Balkans'
    if season == 'Summer':
        price = budget * 0.4
        hotelCamp = 'Camp'
    else:
        price = budget * 0.8
        hotelCamp = 'Hotel'

else:
    destination = 'Europe'
    price = budget * 0.9
    hotelCamp = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{hotelCamp} - {price:.2f}')


