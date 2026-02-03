# funksiyalar
# Qiymat Qaytarmaydigan Funksiya
# def print_5_greetings():
#     for _ in range(5):
#         print("Hello World!")
#
# print_5_greetings()
# print("__ _ __ _ __ ")
# print_5_greetings()

# print(print_5_greetings()) # = "None" - chunki bu funksiya Qiymat Qaytarmaydigan funksiya

# def sanoq():
#     sonlar = list(range(1, 41))
#     for son in sonlar:
#         if son % 6 == 0:
#             print(son)
#
# sanoq()

#                              # Qiymat qaytaradigan Funksiya
# def bir():
#     return 1
# def ikki():
#     return 2
# def uch():
#     return 3
# def tort():
#     return 4
#
# print(bir())  # = 1, chunki bu funksiya qiymat qaytaradigan
#
# son = uch()
# print(son)    # = 3

# def add(a, b): # a,b => parametrlar
#     return a + b
#
#
# yigindi = add(2, 3) # 2,3 => argument
# print(yigindi)

### MASHQLAR ###
# # 1-MASHQ
# login = "admin1"
# parol = 12345
# def login_print(l, p):
#     print(f"""
#     ********************
#     *  login: {l}   *
#     *  parol: {p}    *
#     *                  *
#     ********************
# """)
#
# login_print(login, parol)

# # WORD and LETTER MASHQ
# def find_letter_count(word, letter):
#     return word.count(letter)
#
# natija = find_letter_count("wordwordandanotherwordw", "w")
# print(natija)
## 11-topshiriq

# 1- usul
# def find_max(d):
#     return max(d, key=d.get)
#
# print(find_max({
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }))
# 2- usul
# def find_max(d):
#     max_key = d[list(d.keys())[0]]
#     max_value = list(d.values())[0]
#     for key,value in d.items():
#         if value > max_value:
#             max_value = value
#             max_key = key
#
#     return max_key
#
#
# print(find_max({
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }))

### UYGA VAZIFA:
##1.
# #a option
# def user_data():
#     first_name = input("name>>>")
#     last_name = input("last name>>>")
#     age = int(input("age>>>"))
#     print(f"Ism: {first_name}")
#     print(f"Familiya: {last_name}")
#     print(f"Yosh: {age}")
# user_data()
# #b option
# def user_data(first_name, last_name, age):
#     print(f"Ism: {first_name}")
#     print(f"Familiya: {last_name}")
#     print(f"Yosh: {age}")
#
# # Foydalanuvchidan ma'lumotlarni olish
# ism = input("Ismingizni kiriting: ")
# familiya = input("Familiyangizni kiriting: ")
# yosh = input("Yoshingizni kiriting: ")
#
# # Funksiyani chaqirish
# user_data(ism, familiya, yosh)

##2.
def find_max(a, b, c):
    maks = max(a, b, c)

    natija = []

    if a == maks:
        natija.append("A")
    if b == maks:
        natija.append("B")
    if c == maks:
        natija.append("C")
    print(f"Eng katta son - {' va '.join(natija)}")


a = int(input("A sonini kiriting: "))
b = int(input("B sonini kiriting: "))
c = int(input("C sonini kiriting: "))

find_max(a, b, c)

##3.
# def find_letter_count(word, letter):
#     count = word.count(letter)
#     print(f'"{word}" so\'zida "{letter}" dan {count} ta.')
#
# soz = str(input("Soz kiriting: "))
# harf = input("Harf kiriting: ")
#
# find_letter_count(soz, harf)
#

##4.
# def list_sum(mylist):
#     s = 0
#     for i in mylist:
#         s += i
#     return print(f"Listning elementlar yigindisi = {s}")
#
# list_sum([1,2,3,4])

##5.
# def daraja(a,b):
#     print(a**b)
# daraja(2,3) # natija 8

##6.
# def daraja4(a, b, c, d):
#     print(a**b, a**c, a**d)
# daraja4(2,3,4,5)

##7. digit_count_and_sum(word) - bu funksiya "word" ni ichidagi
##raqamni aniqlab ularni yig'indisini va nechtaligini print qilsin.
# def digit_count_and_sum(a1="abc123de45"):
#     count = 0
#     yigindi = 0
#     for son in a1:
#         if son.isdigit():
#             count += 1
#             yigindi += int(son)
#     return print(f"'Word'dagi raqamlar nechtaligi- {count} \n 'Word'dagi raqamlar yigindisi- {yigindi}")
#
#
# digit_count_and_sum()

##8.
# def add_right(a,b):
#     birga = str(a) + str(b)
#     print(f"Birlashmasi - {birga}")
# add_right(3,4)

##9.
# def add_left(a,b):
#     birga = str(b) + str(a)
#     print(f"Birlashmasi - {birga}")
# add_left(3,4)

##10.
# def work_with_list(a):
#     m = min(a)
#     a1 = []
#     for i in a:
#         a1.append(i*m)
#     return a1
# print(work_with_list([2,3,4]))

##11.
# def big_sales():
#         sales= {
#           "yanvar": 12000,
#           "mart": 6000,
#           "aprel": 15000,
#           "sentabr": 9000,
#           "dekabr": 10000,
#          }
#         eng_katta_oy = max(sales, key=sales.get,)
#         return eng_katta_oy
# natija = big_sales()
# print(natija)
#
# big_sales()

##12.
# def min_max(numbers, max_num, min_num):
#     if max_num == max(numbers):
#         print(f"To'g'ri, eng katta son - {max_num}")
#     else:
#         print(f"{max_num} - Xato, eng katta son emas")
#     if min_num == min(numbers):
#         print(f"Tog'ri, eng kichik son - {min_num}")
#     else:
#         print(f"{min_num} - Xato, eng kichik son emas")
# min_max([1,2,3,4,5,6], 6, 1)

##13.
# def expensiveproduct(products):
#     max_price = 0
#     max_product = {}
#     for product in products:
#         if product["price"] > max_price:
#             max_price = product["price"]
#             max_product = product
#     return max_product["name"]
# arr =  [
#   {
#     "name": "Iphone X",
#     "price": 600
#   },
#   {
#     "name": "Iphone 12",
#     "price": 1500
#   },
#   {
#     "name": "Samsung Note 9",
#     "price": 800
#   },
#   {
#     "name": "Samsung S10",
#     "price": 1100
#   },
# ]
# print(expensiveproduct(arr))

####################################################################################
# d = {
#     "name": "Iphone X",
#     "price": 600,
#     "color": "black"
#   }
#                                  # Hech narsa yozmasak, keys
# for i in d.items():  # d.keys()                      # d.values()
#     print(i)         # Javob: name, clor, price      # Javob: Iphone X, 600, black
####################################################################################