first = int(input())
second = int(input())
magik = int(input())

result = 0
count_magik = False

for first_num in range(first, second + 1):
    for second_num in range(first, second + 1):
        result += 1
        if first_num + second_num == magik:
            count_magik = True
            break
    if count_magik:
        break
if count_magik:
    print(f'Combination N:{result} ({first_num} + {second_num} = {magik})')
else:
    print(f'{result} combinations - neither equals {magik}')
