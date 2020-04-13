list = []
list.append('a')
list.append('b')

list1 = []
list1.append('c')


list.extend(list1)

print(list)
str = ''
for i in list:
    str = str + i + ','

print(str[:-1])