# # # Rekursiv funksiya - funksiya ichida funksiya yaratish

# # Teskari sanoq
# def countdown(n):
#     print(n)
#     if n == 0: # Base condition_1-qism
#         return
#     else:
#         countdown(n-1) # Recursive call_2-qism
#
# countdown(5)


# # Factorialni hisoblash
def factorial(n):
    if n == 1:  # Base Case
        return 1
    else:
        return n * factorial(n - 1)  # Call stack


print(factorial(300))  # Output: 120
#
# # !5 = 5*4*3*2*1


# # Fibonacci sonlarni topish
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n ==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(4))

# def fibonacci(n, cache={}):   #cache = {2:1, 4:3}
#     if n in cache:
#         return cache[n]
#     if n == 0:
#         result = 0
#     elif n == 1:
#         result = 1
#     else:
#         result = fibonacci(n-1) + fibonacci(n-2)
#     cache[n] = result
#     return result
#
# print(fibonacci(20))

# def quick_sort(lst):
#     if len(lst) <= 1:
#         return lst
#     else:
#         pivot = lst[0]
#         left = [x for x in lst[1:] if x<= pivot]
#         right = [x for x in lst[1:] if x > pivot]
#         return quick_sort(left) + [pivot] + quick_sort(right)
#
# print(quick_sort([4, 7, 1, 2, 5, 6, 3]))


