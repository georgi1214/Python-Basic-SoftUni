percent_fat = int(input())
percent_protein = int(input())
percent_carb = int(input())
calories = int(input())
percent_water = int(input())

percent_fat1 = ((percent_fat / 100) * calories) / 9
percent_protein1 = ((percent_protein / 100) * calories) / 4
percent_carb1 = ((percent_carb / 100) * calories) / 4

weight = percent_fat1 + percent_protein1 + percent_carb1
calories2 = calories / weight

weight_per_gr = calories / weight
one_gr = weight_per_gr * (1 - percent_water / 100)
print(f'{one_gr:.4f}')
