dayOfWeak = str(input())

if (dayOfWeak == 'Monday' or dayOfWeak == 'Tuesday' or dayOfWeak =='Wednesday' or dayOfWeak == 'Thursday' or dayOfWeak == 'Friday'):
    print('Working day')
elif (dayOfWeak =='Saturday' or dayOfWeak == 'Sunday'):
    print('Weekend')
else:
    print('Error')