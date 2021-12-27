some_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']

i = 0
for el in some_list:
    some_str = some_list[i]
    str_i = some_str.split(' ')
    name = str_i[-1]
    print('Привет,', name.capitalize(), '!')
    i += 1