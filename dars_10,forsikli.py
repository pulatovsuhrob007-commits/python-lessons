# ism = str(input("Ismingizni kiriting: "))
# qiziqishlar = str(input(f"{ism} nimaga qiziqasiz: "))
#
# if qiziqishlar.find("kitob") >= 0  or qiziqishlar.find("kutubxonaga") >=0:
#     kitob = str(input("Qanday kitoblar yoqadi: "))
#
#     if kitob.find("detektiv") >= 0:
#         fikr = str(input("Shaytanat kitobi haqida fikringiz: "))
#         print("Fikringiz uchun rahmat!")
#
#     elif kitob.find("diniy") >= 0:
#         print("Sizga Hadis va Hayot kitobini sovg'a qilamiz! ")
#
# elif qiziqishlar.find("sport") >= 0:
#     sport_turi = str(input("Qaysi sport turiga qiziqasiz: "))
#
#     if sport_turi.find("futbol") >= 0:
#         komanda = str(input("Qaysi komandaga muhlislik qilasiz: "))
#
#         if komanda.find("real") >= 0 or komanda.find("barsa") >= 0:
#             print("El-Classicoga chipta sovg'a qilamiz! ")
# else:
#     print("Ajoyib!!!!!")

# a = 5.4
# b = 4.8
# a1 = abs(a) - int(abs(a))
# b1 = abs(b) - int(abs(b))
# if a1 > b1:
#     print("A ning qoldig'i katta")
# else:
#     print("B ning qoldig'i katta")

# mevalar = ["olma", "anor", "uzum", "banan"]
#
# for meva in mevalar:
#     if meva== "uzum":
#         continue
#     print(meva, "mevasi")
#     print(meva, "ni olamiz ")

# m = ["a", "b", "c", "d", "e"]
# n = ["A", "B", "C", "D", "E"]
# for i in range(0,5,2):
#     print(f"{m[i]} ning indeksi {n[i]}"

# harflar = ['a', 'b', 'c', 'd', 'e','a', 'b', 'c', 'd', 'e']
# natija = []
# for i in harflar:
#     if i not in natija:
#         natija.append(i)
# print(natija)

# son = int(input("Sonni kiriting: "))
# natija = 1
# for i in range(1,son+1):
#     natija = natija * i
# print(natija)

# import math
#
# son = int(input("son: "))
#
# chegara = int(math.sqrt(son))
#
# for i in range(2, chegara + 1):
#     if i % 2 == 0 and i != 2:
#         continue
#     if son % i == 0:
#         print("tub son emas")
#         break
# else:
#     print("tub son!")

# s = 'abc'
# for i in range(10):
#     s = tuple(s)
# print(s)

t = [1, 2, 3, 4]
x = t.pop()>t.pop()>t.pop()
print(x)