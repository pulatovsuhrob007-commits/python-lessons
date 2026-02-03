"""
01.01.2026
17-dars: Iterator va Generator
A1 guruh: Po'latov Suhrob
"""
# # # ITERATOR
# my_list = [1,2,3]
# my_list_iter = iter(my_list)

# # after iter funksiya
# print(type(my_list))
# print(type(my_list_iter))   # type

# # Oddiy list vs Iterator nima o'zgaradi ?
# l = [1, 2, 3, 4, 5]
# l_iter = iter(l)
# # print(l_iter)
# print(next(l_iter))         # next() funksiyasi
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))

# # for() sikliga nazar
# my_list = [1, 2, 3]
# my_list_iter = iter(my_list)
#
# while True:
#     try:
#         print(next(my_list_iter))
#     except StopIteration:
#         break

# # # GENERATOR
# # Generator yordamida Iterator yaratish
# def try_generator(y):
#     n = y
#     n += 1
#     print("Performed additon")
#     yield n                     # yield dan keyin keyingi qatorga o'tiladi
#                                   # return esa funksiyadan chiqazvoradi
#     n *= 2
#     print("Performed multiplication")
#     yield n
#
# result = try_generator(5)
#
# print(next(result))
# print(next(result))

# # Generator va for sikli
# def return_squared(min, max):
#     for i in range(min, max):
#         yield i**2
#
# result = return_squared(1,5)
#
# for item in result:
#     print(item)

# # # UYGA VAZIFA
# ##1.
# def tubson_generator():
#     def tubson(son):
#         if son < 2:
#             return False
#         for i in range(2, int(son**0.5) + 1):
#             if son % i == 0:
#                 return False
#         return True
#
#     son = 2
#     while True:
#         if tubson(son):
#             yield son
#         son += 1
#
# soonlar = tubson_generator()
# for _ in range(6):
#     print(next(soonlar))

##2.
# import itertools
#
# def password_generator(inputparol):
#     for pwd in itertools.permutations(inputparol):
#         yield ''.join(pwd)
#
# inputparol = "abs"
# parollar = password_generator(inputparol)
# for _ in range(6):
#     print(next(parollar))


