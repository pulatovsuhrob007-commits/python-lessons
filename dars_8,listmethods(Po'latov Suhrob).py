# A1 - Po'latov Suhrob
# 8-dars "List methods"
# 1.append() - listning oxiriga element qo'shadi(biriktiradi)
# fruits = ["apple", "banana", "peach"]
# fruits.append("watermelon")
# print(fruits)
# 2.extend() - kengaytirish ya'ni listga yana list yoki tuple qo'shib beradi
# fruits = ["apple", "banana", "peach",]
# fruits.extend(["watermelon", "melon", "orange"])
# print(fruits)
# 3.insert() - listni orasiga 1 ta element qo'shadi
# fruits = ["apple", "cherry", "orange"]
# fruits.insert(2, "watermelon")
# print(fruits)
# 4.pop() - index bo'yicha xohlagan elementdi o'chiradi(yulvoladi).
# pop() ning 3 ta qiziq tomoni: 1) () ichi bo'sh bo'lsa oxirgi elementdi o'chiradi
#                               2) index yozsak o'sha elementni o'chiradi
#                               3) agar yangi "o'zgaruvchi"ga tenglasak o'sha elementni chiqarib beradi
# 1 mevalar = ["olma","anor", "nok"]
# mevalar.pop()
# print(mevalar)
# 2 mevalar = ["olma", "anor", "nok"]
# mevalar.pop(0)
# print(mevalar)
# 3 mevalar = ["olma", "anor", "nok"]
# meva = mevalar.pop(0)
# print(meva)
# 5.remove() - element o'chirib tashedi qiymat bo'yicha
# mevalar = ["olma", "anor", "banan", "nok"]
# mevalar.remove("banan")
# print(mevalar)
# 6.clear() - hamma elementni o'chirib tashedi
# mevalar = ["olma", 'anor', 'nok','banan']
# mevalar.clear()
# print(mevalar)
# 7.copy() - kopy oladi
# fruits = ["apple","banana","cherrish"]
# f = fruits.copy()
# print(f)
# 8.count() - listdagi elementni sanab beradi
# fruits = ["apple","cherrish", "banana", "cherrish"]
# x = fruits.count("cherrish")
# print(x)
# 9.index() - elementni indexini chiqarib beradi
# fruits = ["apple", "cherrish", "banana"]
# x = fruits.index("cherrish")
# print(x)
# 10.sort() - elementni taxlab beradi (Alfabet yoki tartib raqam bo'yicha
# raqamlar = [1, 7, 4, 5]
# p = raqamlar.sort()
# print(raqamlar)
# 11.reverse - elementlarni teskari qilib beradi
# raqamlar = [3, 2, 7, 4]
# teskari = raqamlar.reverse()
# print(raqamlar)