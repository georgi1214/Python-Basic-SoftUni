easter_bread = int(input())
count_eggs = int(input())
kilograms_cookies = int(input())

bread = 3.20
egg = 4.35
cookie = 5.40
egg_paint = 0.15
egg_paint1 = count_eggs * 12
final_price = 0

easter_bread = easter_bread * bread
count_eggs = count_eggs * egg
kilograms_cookies = kilograms_cookies * cookie
egg_paint1 = egg_paint1 * egg_paint

final_price = easter_bread + count_eggs + kilograms_cookies + egg_paint1
print(f'{final_price:.2f}')