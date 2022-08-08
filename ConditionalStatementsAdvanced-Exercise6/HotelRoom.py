month = input()
nights = int(input())

price_apartment = 0
price_studio = 0
if month in ('May', 'October'):
    price_studio = 50.00
    price_apartment = 65.00
elif month in ('June', 'September'):
    price_studio = 75.20
    price_apartment = 68.70
elif month in ('July', 'August'):
    price_studio = 76.00
    price_apartment = 77.00

discount_apartment = 0
discount_studio = 0
if nights > 14:
    discount_apartment = 0.1
    if month in ('May', 'October'):
        discount_studio = 0.3
    elif month in ('June', 'September'):
        discount_studio = 0.2
elif nights > 7:
    if month in ('May', 'October'):
        discount_studio = 0.05

total_price_studio = price_studio * (1 - discount_studio) * nights
total_price_apartment = price_apartment * (1 - discount_apartment) * nights

print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')






