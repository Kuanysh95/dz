numbers = []
for number in range(1, 1000):
    if number % 2:
        numbers.append(number ** 3)
print(numbers)


sum = 0
for i in range(len(numbers)):
    digit = numbers[i] % 10
    sum += digit
    numbers[i] //= 10
    if sum % 7 == 0:
        print(sum)

sum = 0
for i in range(len(numbers)):
    digit = numbers[i] % 10
    sum += digit
    numbers[i] //= 10
    sum += 17
    if sum % 7 == 0:
        print(sum)




