count_groups = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
all_people = 0

for i in range(1, count_groups + 1):
    count_people = int(input())
    all_people += count_people

    if count_people <= 5:
        musala += count_people
    elif count_people <= 12:
        montblanc += count_people
    elif count_people <= 25:
        kilimanjaro += count_people
    elif count_people <= 40:
        k2 += count_people
    else:
        everest += count_people

musala_percent = musala / all_people * 100
montblanc_percent = montblanc / all_people * 100
kilimanjaro_percent = kilimanjaro / all_people * 100
k2_percent = k2 / all_people * 100
everest_percent = everest / all_people * 100

print(f'{musala_percent:.2f}%')
print(f'{montblanc_percent:.2f}%')
print(f'{kilimanjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')
