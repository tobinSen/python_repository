# a = 100
#
#
# def test1(a, b):
#     return a, b, {}, {'key': 'value'}, [], (), set()
#
#
# def test2(a):
#     print(a)
#
#
# print(test1(1, 2))
# print(type(test1(1, 2)))
#
# print(a)


def sum_numbers(num):
    if num == 1:
        return 1
    return num + sum_numbers(num - 1)


print(sum_numbers(3))
