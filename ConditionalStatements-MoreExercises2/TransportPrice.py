import math

n_kilometers = int(input())
day_night = input()

daily_night_rate = 0

if n_kilometers < 20:
    if day_night == 'day':
        daily_night_rate = 0.79 * n_kilometers + 0.70
    elif day_night == 'night':
        daily_night_rate = 0.90 * n_kilometers + 0.70
elif n_kilometers >= 20 and n_kilometers < 100:
    daily_night_rate = n_kilometers * 0.09
elif n_kilometers >= 100:
    daily_night_rate = n_kilometers * 0.06
print(f'{daily_night_rate:.2f}')




