num = int(input())

count_num = 0

for x1 in range(0, num + 1):
    for x2 in range(0, num + 1):
        for x3 in range(0, num + 1):
            if x1 + x2 + x3 == num:
                count_num += 1
print(count_num)

