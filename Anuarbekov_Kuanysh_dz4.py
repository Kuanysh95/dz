'''Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5


Примечание: сможете ли вы замаскировать работу декоратора?'''

def val_checker(callback):
    def _val_checker(func):
        def wrapper(*args):
            try:
                if len(list(filter(callback, args))):
                    return func(*filter(callback, args))
                else:
                    raise ValueError(f"wrong val {''.join(str(*args))}")
            except ValueError as e:
                print(f'ValueError: {e}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
