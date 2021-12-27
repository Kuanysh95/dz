
prices = [45.89, 23.76, 87, 95.74, 33, 80.34, 18.23, 27.98, 56, 75.37]
new_list = []

for price in prices:
    ruble = int(price)
    penny = int((price - ruble) * 100)
    new_list.append(f'{ruble} руб {penny:02d} коп')
print(', '.join(new_list))
print(id(new_list))
new_list.sort()
print(new_list)
print(id(new_list))
new_list_2 = sorted((new_list), reverse=True)
print(new_list_2)
