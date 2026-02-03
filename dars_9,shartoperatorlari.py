# # String and List Slicing - String va Listlarni Kesish
# matn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# matn2 = matn[0:11:3] 0=begin, 11=end, 3=step.
# print(matn2) [0, 3, 6, 9]
# sonlar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# matn = "123456789"
# matn2 = matn[8:2:-2]
# print(matn2) 975

# Shart operatorlari - Conditionals: if elif else
# # IF, ELSE, ELIF - shart operatorlari va "INPUT" funksiyasi
# print("Saylovga Xush keilbsiz!")
# user = input("Ismingiz: ")
# age = int(input("Yoshingiz: "))
# print(f"Xush keilibsiz {user}bek, sizning yoshingiz - {age}da")
# if age == 18:
#     print("Amallab qatnashsez bo'larkan, Saylovga")
# else:
#     print("Saylovga Xush kelibsiz")

# # "ELIF" - shart operatori
# yosh = int(input("Yoshingiz: "))
# if yosh < 18:
#     print("Voyaga yetmagan")
# elif yosh >= 18 and yosh < 30:
#     print("Yoshlar toifasi")
# elif yosh >= 30 and yosh < 60:
#     print("O'rta yosh")
# else:
#     print("Qariya")

# # "OR"- shart operatori
# user_parol = input("Parolni kiriting: ")
# parol = "qwerty"
# parol2 = "1234"
# parol3 = "asdf"
# if user_parol == parol or user_parol == parol2 or user_parol == parol3:
#     print("Xush kelibsiz")
# else:
#     print("Login yoki parol xato!")


sonA = int(input("'A' sonni kiriting: "))
sonB = int(input("'B' sonni kiriting; "))
if sonA > 3 and sonB <= 6:
    print("TO'G'RI")
else:
    print("XATO")

# a = int(input("Son kiriting: "))
# if str(a)[0] == str(a)[1] == str(a)[2]:
#     print("XATO")
# else:
#     print("TO'G'RI")

# son = int(input("son: "))
# if son == 1:
#     print("Dushanba")
# elif son ==2:
#     print("Seshanba")
# elif son ==3:
#     print("Chorshanba")
# elif son ==4:
#     print("Payshanba")
# elif son ==5:
#     print("Juma")
# elif son ==6:
#     print("Shanba")
# elif son ==7:
#     print("Yakshanba")
# else:
#     print("Bunday hafta kunlari yo'q!")

# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
#
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))
#
# if abs(x1-x2) == abs(y1-y2):
#     print("Yursa bo'ladi")
# else:
#     print("Yurib bo'maydi")