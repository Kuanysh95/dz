src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def get_unique_numbers(src):
    unique = []

    for number in src:
        if number in unique:
            continue
        else:
            unique.append(number)
    yield unique

print(next(get_unique_numbers(src)))
