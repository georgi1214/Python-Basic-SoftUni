count_guests = int(input())
price_envelope = float(input())
budget = float(input())

cake = (budget / 100) * 10
diss = 0
all_price = 0

if count_guests < 10:
    diss = price_envelope
elif count_guests >= 10 and count_guests <= 15:
    diss = (price_envelope * 0.85) * 1
elif count_guests >= 15 and count_guests <= 20:
    diss = (price_envelope * 0.80) * 1
elif count_guests > 20:
    diss = (price_envelope * 0.75) * 1

all_price = count_guests * diss + cake

if budget < all_price:
    print(f'No party! {all_price - budget:.2f} leva needed.')
else:
    print(f'It is party time! {budget - all_price:.2f} leva left.')
