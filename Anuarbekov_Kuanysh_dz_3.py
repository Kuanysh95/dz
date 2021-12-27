for number in range(1, 101):
    if number % 10 == 1 and number != 11:
       print(number, 'процент')
    elif number % 10 == 2 and number != 12:
       print(number, 'процента')
    elif number % 10 == 3 and number != 13:
       print(number, 'процента')
    elif number % 10 == 4 and number != 14:
       print(number, 'процента')
    else:
       print(number, 'процентов')