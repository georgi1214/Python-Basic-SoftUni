change = float(input())
change_coins = round(change * 100)

coins_count = 0
# 1.23 = 123
while change_coins > 0:
    if change_coins >= 200:
        change_coins = change_coins - 200
        coins_count += 1
    elif change_coins >= 100:
        change_coins = change_coins - 100
        coins_count += 1
    elif change_coins >= 50:
        change_coins = change_coins - 50
        coins_count += 1
    elif change_coins >= 20:
        change_coins = change_coins - 20
        coins_count += 1
    elif change_coins >= 10:
        change_coins = change_coins - 10
        coins_count += 1
    elif change_coins >= 5:
        change_coins = change_coins - 5
        coins_count += 1
    elif change_coins >= 2:
        change_coins = change_coins - 2
        coins_count += 1
    elif change_coins >= 1:
        change_coins = change_coins - 1
        coins_count += 1

print(coins_count)