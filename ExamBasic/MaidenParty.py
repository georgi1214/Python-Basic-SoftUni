price_party = float(input())
love_message = int(input())
flowers = int(input())
keychain = int(input())
cartoon = int(input())
surprise = int(input())

love_message1 = 0.60
flowers1 = 7.20
keychain1 = 3.60
cartoon1 = 18.20
surprises = 22

count_products = love_message + flowers + keychain + cartoon + surprise
all_price = (love_message * love_message1) + (flowers * flowers1) + \
            (keychain * keychain1) + (cartoon * cartoon1) + (surprise * surprises)

if count_products >= 25:
    all_price = all_price - (all_price * 0.35)
hosting = all_price * 0.1

hosting1 = all_price - hosting

diff = abs(hosting1 - price_party)

if diff > price_party:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')

