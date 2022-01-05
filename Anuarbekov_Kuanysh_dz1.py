n = 15

def odd_to_n():
    for num in range(1, n + 1):
        if num % 2 != 0:
            yield num

nums = odd_to_n()
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

