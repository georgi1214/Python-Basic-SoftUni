import math

tournament = int(input())
start_points = int(input())

win_points = 0
win_count = 0
for i in range(1, tournament + 1):
    points = str(input())

    if points == 'W':
        win_count += 1
        win_points += 2000
    elif points == 'F':
        win_points += 1200
    elif points == 'SF':
        win_points += 720

points_after_game = start_points + win_points
diff = math.floor(win_points / tournament)
percent_win = win_count / tournament * 100

print(f'Final points: {points_after_game}')
print(f'Average points: {diff}')
print(f'{percent_win:.2f}%')


