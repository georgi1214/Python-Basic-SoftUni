square_m = float(input())

square_meters = 7.61

price = square_m * square_meters
all_price = price * 0.82


diss = price - all_price


print(f'The final price is: {all_price:.2f} lv.')
print(f'The discount is: {diss:.2f} lv.')
