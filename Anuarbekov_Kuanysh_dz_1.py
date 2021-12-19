dur = int(input('Enter duration: '))

if dur < 60:
    second = dur % 60
    print('duration =', dur)
    print(second, 'сек')
elif dur < 3600:
    minute = dur // 60
    second = dur % 60
    print('duration =', dur)
    print(minute, 'мин', second, 'сек')
elif dur < 86400:
    hour = dur // 3600
    minute = dur % 3600 // 60
    second = dur % 60
    print('duration =', dur)
    print(hour, 'час', minute, 'мин', second, 'сек')
else:
    day = dur // 86400
    hour = dur % 86400 // 3600
    minute = dur % 3600 // 60
    second = dur % 60
    print('duration =', dur)
    print(day, 'дн', hour, 'час', minute, 'мин', second, 'сек')

