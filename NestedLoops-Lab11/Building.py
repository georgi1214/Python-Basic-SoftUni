number_of_floors = int(input())
numbers_of_rooms = int(input())

floor_letter = ' '

for floor in range(number_of_floors, 0 , -1):
    for room in range(0, numbers_of_rooms):
        if floor == number_of_floors:
            floor_letter = 'L'
        elif floor % 2 != 0:
            floor_letter = 'A'
        else:
            floor_letter = 'O'
        print(f'{floor_letter}{floor}{room}', end=' ')
    print()

