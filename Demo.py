# def add(a,*b,*c):
#     print('a=%s' %a)
#     print('b=%s' %a)
#     print('c=%s' %a)
#
#
# add(1)
#

b = 100


# a = [1, 2, 3, '1']

#
# print(list(map(lambda x: x, a)))
# cnt = 3


#
# def counter():
#     cnt = 0
#     def add():
#         # nonlocal cnt
#         cnt += 1
#         # cnt += 1
#         return cnt[0]
#     return add
#
#
#
# # counter()
# # print(cnt)
#
# number =  counter()
#
# print(number())
# print(number())
# print(number())
# print(number())
# print(number())


#
# count = 10
# def outer():
#     print(count)
#     global count
#     # count = 100
#     print(count)
# outer()
# count=30

# count = 100
#
#
# def outoutout():
#     count = 40
#
#     def outer():
#         count = 10
#
#         def inner():
#             # nonlocal count
#             global count
#             count = 20
#             print(count)
#
#         inner()
#         print(count)
#
#     outer()
#
#
# outoutout()
# print(count)


# ---------------------------------------------------------------
# a = [0, 1, 2, 3]
# d = 0
#
# c = 2 * d + 3
#
#
# def test():
#     a[0] = 3
#     d = 10
#     print(a, d)
#
#
# test()
# print(d, a)


def test(num):
    in_num = num

    def nested(label):
        nonlocal in_num
        in_num += 1
        print(label, in_num)

    return nested


F = test(0)
F('a')
F('b')
F('c')
G = test(100)
G('mm')

F('d')

# a = [0, 1, 2, 3]
# b = 0
#
# def test():
#     a[0] = 3
#     # c = 10
#     print(a)
#
#
# test()
# print(a)

# def outer_fun():
#     a = 1
#
#     def fun():
#         global a  # a为全局变量，与上面等于1的 a 没有关系
#         a = 3  # 定义全局变量
#         print(a)  # 输出3
#         a = 2
#
#     fun()
#     print(a)  # 输出1，局部变量
#
#
# outer_fun()
# print(a)  # 输出2，全局变量
