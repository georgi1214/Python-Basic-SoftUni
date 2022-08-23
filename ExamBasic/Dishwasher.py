bottles = int(input())
soap = bottles * 750
plates = 0
pots = 0
counter = 0

while soap >= 0:
    command = input()

    if command == 'End':
        break
    dishes = int(command)
    counter += 1

    if counter % 3 == 0:
        pots += dishes
        soap -= abs(dishes * 15)
    else:
        plates += dishes
        soap -= abs(dishes * 5)
if soap < 0:
    print(f'Not enough detergent, {abs(soap)} ml. more necessary!')
else:
    print('Detergent was enough!')
    print(f'{plates} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {soap} ml.')



