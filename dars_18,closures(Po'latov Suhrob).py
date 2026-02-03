"""
02.01.2026
18-dars: Closures
A1 guruh: Po'latov Suhrob
"""
# # # Scope of variable - o'zgaruvchining qamrovi

# # 1) Global Scope
# a = 4 #global
#
# def f1():
#     print(a+1)
#
# # f1()           # output = 5
# # print(a)       # output = 4
#
# def f2():
#     global a                  ##>>>>Global variableni o'zgartirishda,
#     a+=1                         #>>>"global"dan foydalanamiz
#     print(a)
#
# f2()           # output = 5
# print(a)       # output = 5

# # 2) Local Scope
# def f1():
#     a = 4#local
#     a += 1        # output = 5
#     print(a)
# # f1()

# # 3) Nonlocal Scope
# def f1():
#     a = 4
#     def f2(): #inner function      # ichkma-ich ketgan funkisyada
#       print(a)  #nonlocal        # f2() uchun 'a' nonlocal hisoblanadi


# # Global o'zgaruvchi funksiya ichida qayta yaratilsa,
## u o'sha funksiya uchun local bo'ladi.

# a = 4
# def f1():
#     global a
#     a = 5
#    print(a) # local -> 5

# print(a) #global -> 4


# def d1():
#     a = 4
#     def d2(): #inner function
#         nonlocal a          ##>>> ichki funksiya o'zgaruvchini o'zgartirish
#         a += 2                    # uchun nonlocal so'zidan foydalanadi
#     print(a)    # -> 6
# d1()
# d2() # -> ishlamaydi!




# def f1():
#     a = 4
#     return a
# x = f1() #1
# f2(f1()) #2

# def f(x):
#     def g(y):
#         return y
#     return g
# a = 5
# b = 1
#
# h = f(a)
# natija = h(b)
# print(natija)   # Output is `1
## yoki
# natija = f(a)(b)
# print(natija)     # Output is 1

# # 3-qavatli funksiya
# def f(x):
#     def g(y):
#         def h(z):
#             return z
#         return h
#     return g
# a = 5
# b = 2
# c= 1
# f(a)(b)(c)  # Output is 1

def f(x):
    z = 2
    def g(y):
        return z*x + y










