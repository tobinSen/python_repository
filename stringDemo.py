str1 = 'I wonder to Hello world'

index = str1.find('wonder')
index1 = str1.index('wonder')
count = str1.count('wond')

newStr = str1.replace('I', 'I am Tom', 2)
print(newStr)
list = [1, 2, 3, 4, 5, 6]
index = list.index(1)
print(index)
print(list.count(1))
print(len(list))

name_list = [1, 2, 3, 4, 5, 6]
print(1 in name_list)  # True

name_list.append(['tom', 32, 322])
name_list.extend([1, 2, 34, 5])
name_list.insert(3, ['yyy', 123])
# del name_list
# print(name_list)

for n in name_list:
    print(n)
