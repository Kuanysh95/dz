list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = []
for i in list_1:
    if(i.isdigit() == True):
        list_2.extend(['"', i.zfill(2), '"'])
    elif(i.startswith('+')):
        list_2.extend(['"', i.zfill(3), '"'])
    else:
        list_2.append(i)
print(list_2)

list_2 = " ".join(list_2).strip()
print(list_2)