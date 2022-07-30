tape_fuel = str(input())
tank_fuel = int(input())

lower_case = tape_fuel.lower()

if tape_fuel == 'Diesel' or tape_fuel == 'Gasoline' or tape_fuel == 'Gas':
    if tank_fuel < 25:
        print(f'Fill your tank with {lower_case}!')
    elif tank_fuel >= 25:
        print(f'You have enough {lower_case}.')
else:
    print('Invalid fuel!')

