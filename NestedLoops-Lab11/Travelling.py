destination = input()

while destination != 'End':
    needed_money = float(input())
    count_money = 0
    while count_money < needed_money:
        current_save_money = float(input())
        count_money += current_save_money
    print(f'Going to {destination}!')
    destination = input()
