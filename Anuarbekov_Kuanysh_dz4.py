src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = []
a = [int(i) for i in src]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        result.append(a[i])

print(result)





