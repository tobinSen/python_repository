name_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in name_list:
    for name in list:
        if name == 7:
            print(name)
            break
        print(name)

print(name_list[0][1])

teacher = ['Tom', 'Lily', 'Rose']
classRoom = [1, 2, 3]
t1 = (1, 2, 3, 4)
print(t1)
t2 = (1, 'Tom')
t3 = (1,)
print(type(t2))  # int
print(type(t3))  # tuple
