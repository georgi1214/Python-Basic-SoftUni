import math

name = input()
episodeDuration = int(input())
breakDuration = int(input())

lunchTime = breakDuration / 8
relaxTime = breakDuration / 4

timeForEpisode = breakDuration - lunchTime - relaxTime

diff = abs(timeForEpisode - episodeDuration)

if timeForEpisode >= episodeDuration:
    print(f'You have enough time to watch {name} and left with {math.ceil(diff)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(diff)} more minutes.")