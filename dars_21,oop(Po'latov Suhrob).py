# # # OOP - Obyektga yo'naltirilgan dasturlash

# class Mashina:
#     def __init__(self, narxi, tezligi, rangi):
#         self.narxi = narxi
#         self.rangi = rangi
#         self.tezligi = tezligi
#
#     def signal(selfself, tovush="Beep!"):
#         print(tovush)
#
#
# m = Mashina(narxi=30000, tezligi=220, rangi="oq")
# m.nomi = "Tesla"

# class Person:
#     def __init__(self, name, age, gender): #konstruktor
#         self.name = name # attribute
#         self.age = age # attribute
#         self.gender = gender # attribute
#
#
# Doe = Person(name="Doe", age=20, gender="male") # Instantiate object
# Anna = Person(name="Anna", age=18, gender="female") # Instantiate object
#
# print(Doe.name, Doe.age)
# print(Anna.name, Anna.age)
# # Output
# # Doe 20
# # Anna 18

# # Endi unga method qo'shamiz:
# class Person:
#     arms = 2                # class ni o'ziga o'zgaruvchi yaratish
#     legs = 2
#
#
#     def __init__(self, name, age, gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#
#     def update_age(self,val):
#         if val > 0:
#             self.age = val
#         else:
#             raise "Bunday yosh mavjud emas"
#
#     def create(self, new_var):
#         self.new_var = new_var
#
#     def delete(self, val):
#         del val
#
#
#     def read(self):
#         self.all = {'name':self.name, 'age':self.age, 'gender':self.gender}
#         return self.all
#
# Doe = Person(name="Doe", age=20, gender="male")
# Anna = Person(name="Anna", age=18, gender="female")
# Doe.kurs = 2
# Doe.update_age(15)
#
# print(Doe.kurs)


# Doe.speak("Salom Anna")
# Anna.speak("Salom Doe, yaxshimisz")
# Doe.kurs = 2
# Doe.change_country("USA")
# print(Doe.country)

# # # UYGA VAZIFA
# # 1)
# class Oson1:
#     a = 4
#
#     def output_a(cls):
#         print(cls.a)
#
# # Oson1.output_a(Oson1)

# # 2)
# class Oson2:
#     a = 4
#     b = 3
#
#     def summa(cls):
#         print(cls.a + cls.b)
#
# # Oson2.summa(Oson2)

# # # 3)
# class Oson3:
#     a = -1
#
#     def plus_minus(cls):
#         if cls.a < 0:
#             print("Manfiy son")
#         elif cls.a >= 0:
#             print("Musbat son")
#
# Oson3.plus_minus(Oson3)


# # # 4)
# class Oson4:
#     a = 1
#     def odd_even(cls):
#         if cls.a % 2 == 0:
#             print("Juft son")
#         elif cls.a == 1:
#             print("1 Toq son ham emas, juft son ham emas")
#         else:
#             print("Toq son")
#
# Oson4.odd_even(Oson4)


# # 5)
# class Oson5:
#     a = 4
#     b = 3
#
#     def daraja(cls):
#         print(cls.a**cls.b)
#
# Oson5.daraja(Oson5)

# # # 6)
# class MyClass6:
#     words = []
#
#     def add_word(self, word):
#         self.words.append(word)
#         print(word)
#     def remove(self, word):
#         self.words.remove(word)
#         print(word)
#
# obj = MyClass6()
# obj.add_word("olma")
# obj.add_word("shaftoli")
# obj.remove("olma")
# print(obj.words)

# # # 7)
# class MyClass7:
#     myDict = {}
#
#     @classmethod
#     def add_elem(cls, key, val):
#         if key not in cls.myDict:
#             cls.myDict[key] = val
#     @classmethod
#     def update_elem(cls, key, val):
#         if key in cls.myDict:
#             cls.myDict[key] = val
#
# MyClass7.add_elem('a', 10)
# MyClass7.add_elem('b', 20)
# MyClass7.add_elem('a', 99)
#
# print(MyClass7.myDict)
#
# MyClass7.update_elem("a", 100)
# MyClass7.update_elem('c', 30)
#
# print(MyClass7.myDict)


# # # 8)
# class MyClass8:
#     def __init__(self, numbers):
#         self.numbers = numbers
#
#     def compare_lists(self, new_list):
#         sum_numbers = sum(self.numbers)
#         sum_new_list = sum(new_list)
#
#         if sum_numbers > sum_new_list:
#             print(self.numbers)
#         else:
#             print(new_list)
#
#
# obj = MyClass8([1, 2, 3, 4])
#
# obj.compare_lists([1, 2, 3])
# obj.compare_lists([5, 6])


#
# # # 9)
# class MyClass9:
#     def __init__(self, list1, list2):
#         self.list1 = list1
#         self.list2 = list2
#
#     def list1_max(self):
#         return max(self.list1)
#
#     def list2_max(self):
#         return max(self.list2)
#
#     def sum_of_two_max(self):
#         jami = self.list1_max() + self.list2_max()
#         print(jami)
#
#
# obj = MyClass9([1, 5, 3], [2, 8, 4])
# print(obj.list1_max())  # 5
# print(obj.list2_max())  # 8
# obj.sum_of_two_max()  # 13

# # # 10)
# class MyClass10:
#     def __init__(self, numbers):
#         self.numbers = numbers
#
#     def divide(self, d):
#         if d == 0:
#             raise ValueError("Bo'luvchi '0' ga teng bo'la olmaydi!")
#         natija = []
#         for num in self.numbers:
#             if num % d == 0:
#                 natija.append(num)
#         return natija
#
# obj = MyClass10([12,15,18,20])
# print(obj.divide(5))      # 15, 20
# print(obj.divide(3))      # 12, 15, 18