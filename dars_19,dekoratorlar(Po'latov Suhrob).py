
#
# def group_generator(lst, n):
#     stack = [(0, [])]
#     while stack:
#         idx, current_group = stack.pop()
#         if len(current_group) == n:
#             yield tuple(current_group)
#         else:
#             for i in range(idx, len(lst)):
#                 new_group = current_group + [lst[i]]
#                 stack.append((i + 1, new_group))
#                 # print(f"stack={stack}")
#     else:
#         print("end")
#
#
# my_list = [1, 2, 3, 4]
# group_size = 2
# groups = group_generator(my_list, group_size)
# for group in groups:
#     print(group)

# def deco(f):
#         def g(*args, **kwargs):
#             return f(*args, **kwargs)
#         return g
#
# def func(x):
#       return 2*x
#
# func = deco(func)
# func(2)  # Output is 4

# def deco(f):
#     def g(*args, **kwargs):
#         print("Calling ", f.__name__)
#         return f(*args, **kwargs)
#     return g
# @deco
# def func(x):
#     return 2*x
#
# func = deco(func)
# func(2)


# def suhrobbek(f):
#     def g(*args, **kwargs):
#
#
#         f(*args, **kwargs)
#         print("by Suhrobbek", f.__name__)
#     return
#
#
# @suhrobbek
# def kv(x):
#     print(f"x ning kvadrati: {x*x}")
#
# kv(2)

# # # UYGA VAZIFA

##1
# def uppermethod(f):
#
#     def ichki():
#         natija = f()
#         return natija.upper()
#
#     return ichki
#
# @uppermethod
# def string():
#     return 'Katta harflarda'
# print(string())

# def uppercase_deco(func):
#     def wrapper(*args):
#         result = func(*args)
#         return result.upper()
#     return wrapper
#
# @uppercase_deco
# def greet(name):
#
#     return name
#
# result = greet('John')
# print(result)

##2.
# def teskariga(function):
#     def ichki():
#         natija = function()
#         return natija[::-1]
#     return ichki
# @teskariga
# def matn():
#     return 'idlitaray irakseT'
# print(matn())

# def reversed_version(function):
#     def wrapper(*args, **kwargs):
#         result=function(*args, **kwargs)
#         return result[::-1]
#     return wrapper
#
# @reversed_version
# def string(x):
#     return x
#
# result = string("Salom")
# print(result)


##3.
# import time
#
# def vaqt_hisobla(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         natija = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} took: {end - start:.2f} seconds to execute")
#         return natija
#     return wrapper
#
# @vaqt_hisobla
# def test():
#     def fibonacci(n):
#         if n == 0:
#             return 0
#         elif n ==1:
#             return 1
#         else:
#             return fibonacci(n-1) + fibonacci(n-2)
#     print(fibonacci(37))
#
# test()

##4.
# def chaqiruv_counter(func):
#     sanoq = 0
#
#     def ichki():
#         nonlocal sanoq
#         sanoq += 1
#         print(f"Funksiya {sanoq} marta chaqirildi")
#         return func()
#     return ichki
#
# @chaqiruv_counter
# def salom():
#     print("Salom !")
#
# salom()
# salom()

def count_calls_decorator(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls_decorator
def some_function():
    a = 0
    for i in range(3):
        a += 5

f = some_function()
g = some_function()
print(some_function.calls)

