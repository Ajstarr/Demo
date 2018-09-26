# # # import Demo
# # #
# # # print(Demo.b)
# a = 1
#
#
# def test():
#     # a = [8]
#     print(a)
#
#     def test1(a=3):
#         # nonlocal a
#         # a = [3]
#         # b = a + 1
#         # a = 2
#
#         print(a)
#
#         def test2():
#             # global a
#             # a = a + 1
#             # a[0] += 1
#             # a = 3
#             print(a)
#
#         test2()
#         print(a)
#
#     test1()
#     # print(a)
#     print(a)
#
#
# test()
# print(a)
#
#
#
#
#
# #
# # def test(a=[1]):
# #     # a = [8]
# #     a[0] += 1
# #     print(a)
# #
# #
# # test()
# # test()
# # test()
# # test()


# t = [[], []]
# li = [[]]
# Li = [[1, 2, 3, [4]]]
# Li = Li + Li
# li = [[] for _ in range(3)]
# # Li[0].append(1)
#
# print(Li)
#
# print(li)
# # li[0].append(1)
# print([id(inner_list) for inner_list in li])
#
# # print(li)
#
# i = 0
# a = [i for i in range(3)]
# print(i)
# print(a)
#
# b = (0, 1, 2, 3, 4, 5)[:4]
# print(b)
# for i in li:
#     print(i)
# li = [[] for _ in range(3)]

# li=[1,[2]]
# li = [1,2]
# li[2].append(2)

# print(li)

# def f(x):
#     return x * x
#
#
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(r)
from functools import reduce

# def count():
#     fs = []
#     print(fs)
#     for i in range(1, 4):
#         def f():
#             return i * i
#
#         fs.append(f)
#     print(fs)
#     return fs


# print(count())
# count()

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#
#         return wrapper
#
#     return decorator
#
#
#
# @log('execute')
# def now():
#     print('2015-3-25')
#
#
# now()
# print(now.__name__)


# def decorator_a(func):
#     print('Get in decorator_a')
#
#     def inner_a(*args, **kwargs):
#         print('Get in inner_a')
#         return func(*args, **kwargs)
#
#     return inner_a
#
#
# def decorator_b(func):
#     print('decorator_b')
#
#     def inner_b(*args, **kwargs):
#         print('Get in inner_b')
#         return func(*args, **kwargs)
#
#     return inner_b
#
#
# @decorator_b
# @decorator_a
# def f(x):
#     print
#     'Get in f'
'123'

# print(int.mro())
from collections.abc import Iterable
from collections.abc import Iterator


# _______________________________________
class A(object):
    def go(self):
        print("go A go!")

    def stop(self):
        print("stop A stop!")

    def pause(self):
        raise Exception("Not Implemented")


class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")


class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")

    def stop(self):
        super(C, self).stop()
        print("stop C stop!")


class D(C, B):
    def go(self):
        super(D, self).go()
        print("go D go!")

    def stop(self):
        super(D, self).stop()
        print("stop D stop!")

    def pause(self):
        print("wait D wait!")


class E(B, C): pass


print(D.mro())
print(C.mro())

a = A()
print('-------------------')
b = B()
print('-------------------')
c = C()
print('-------------------')
d = D()
print('-------------------')
e = E()
print('-----a.go-----')

a.go()
print('-----b.go----------')
b.go()
print('----c.go----------')
c.go()
print('----d.go-----------')
d.go()
print('--------e.go-----------')
e.go()
print('--------a.stop-----------')

a.stop()
print('--------b.stop-----------')
b.stop()
print('--------c.stop-----------')
c.stop()
print('--------d.stop-----------')
d.stop()
print('--------e.stop-----------')
e.stop()
print('-------------------')
print('-------------------')
print('-------------------')
print('-------------------')


#
# a.pause()
# print('-------------------')
# b.pause()
# print('-------------------')
# c.pause()
# print('-------------------')
# d.pause()
# print('-------------------')
# e.pause()

class CCC(object):
    auth = "hello"  # 类变量

    def __init__(self):
        self.person = "jzm123"  # 实例变量

    def instance_printauth(self):  # 实例方法
        print("成员方法:" + self.auth)

    @classmethod
    def class_printauth(cls):  # 类方法
        print("类方法:" + cls.auth)

    @staticmethod
    def static_printauth():  # 静态方法
        print("静态方法:" + CCC.auth)

    def use_membervariable(self):
        print("成员变量" + self.person)


# if __name__ == "__main__":
ccc = CCC()
print("---静态方法，对参数无要求---")
ccc.static_printauth()
CCC.static_printauth()
print("---类方法，第一个参数为类，可由类或者对象调用---")
ccc.class_printauth()
CCC.class_printauth()
print("---成员方法，只能由对象调用---")
ccc.instance_printauth()
print("---类变量---")
print("类变量:CCC.auth=" + CCC.auth)  # 类变量
print("---实例变量---")
print("实例变量:ccc.person=" + ccc.person)  # 实例变量
ccc.person = "xxx"
ccc.auth = "1222er"
print("实例变量:ccc.person=" + ccc.person)  # 实例变量
print("类变量:CCC.auth=" + CCC.auth)  # 类变量
CCC.auth = "ggg"
print("类变量:CCC.auth=" + CCC.auth)  # 类变量

ppp = CCC()
print("实例变量:ppp.person=" + ppp.person)  # 实例变量
print("类变量:CCC.auth=" + CCC.auth)  # 类变量

del CCC.auth
# del CCC.auth
#
# print(ccc.auth)
# print(CCC.auth)
print(CCC.auth)
CCC.class_printauth()

print('11')
print('11')
print('11')
print('11')
print('11')

zip()
zip()

zip()
zip()