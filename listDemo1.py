# list = []
# i = 0
# while i < 10:
#     list.append(i)
#     i += 1
# print(list)

# for i in range(10):
#     list.append(i)
#
# list = [i for i in range(10) if i % 2 == 0]
# set = {i for i in range(10)}
# print(set)
# print(list)

# list = [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
#
# newList = [(i, j) for i in range(1, 3) for j in range(3)]  # 相当于for循环嵌套逻辑
# # print(newList)
# dict = {i: i * 2 for i in range(3)}
# print(dict)

# propertyList = ['name', 'age', 'gender']
# valueList = ['Tom', 20]
# dict = {p: valueList[index] for index, p in enumerate(propertyList)}
# dict1 = {propertyList[i]: valueList[i] for i in range(len(propertyList))}
# print(dict)
# # print(dict1)
# counts = {'HP': 1000, 'MBP': 2000, 'Deli': 3000, 'acer': 200}
# dict = {k: v for k, v in counts.items() if v >= 2000}
# print(dict)

set = {i ** 2 for i in range(3)}
print(set)
