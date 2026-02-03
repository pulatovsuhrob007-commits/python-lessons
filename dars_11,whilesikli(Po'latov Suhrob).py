# WHILE sikli mavzusi 11-dars
# Sana: 22.11.2025


# a = [1, 2, 3, 4,]
# for i in a:
#     print(i, end = " ")

# sanoq = 0
# while sanoq < 5:
#     print("Hello World!")
#     sanoq += 2

# while True:
#     ism = input("Ismni kiriting: ")
#     print(f"Hello {ism}")
#     if ism == "Zoe":
#         print("O'zbekcha ism emas!")
#         break

# son = 1
# while son <10:
#     print(son)
#     son += 1

# users = {"Doe":"123root", "John":"root2", "Joey":"root3", "Anna":"root4"}
#
#
# while True:
#     ism = input("Ism: ")
#     parol = input("Parol kirting: ")
#
#     if ism in users.keys() and parol in users.values():
#
#      print("Ruxsat etildi, Xush kelibsiz!")
#      break
#     else:
#         print("Xato, Iltimos qayta urining")


# X VA O O'YINI
# g=[1,2,3,4,5,6,7,8,9]
#
#
# print(f"""
#              {g[0]} | {g[1]} | {g[2]}
#             -----------
#              {g[3]} | {g[4]} | {g[5]}
#             -----------
#              {g[6]} | {g[7]} | {g[8]}
# """
#       )
#
# while True:
#
#     x = int(input('x='))
#     g[x - 1] = 'X'
#     print(f"""
#                  {g[0]} | {g[1]} | {g[2]}
#                 -----------
#                  {g[3]} | {g[4]} | {g[5]}
#                 -----------
#                  {g[6]} | {g[7]} | {g[8]}
#     """
#           )
#     if g[0]==g[1] and g[1]==g[2] or g[3]==g[4] and g[4]==g[5] or g[6]==g[7] and g[7]==g[8] or g[0]==g[3] and g[3]==g[6] or g[1]==g[4] and g[4]==g[7] or g[2]==g[5] and g[5]==g[8] or g[0]==g[4] and g[4]==g[8] or g[2]==g[4] and g[4]==g[6]:
#         print('X yutdi! tamom')
#         break
#     o = int(input('o='))
#     g[o - 1] = 'O'
#     print(f"""
#                  {g[0]} | {g[1]} | {g[2]}
#                 -----------
#                  {g[3]} | {g[4]} | {g[5]}
#                 -----------
#                  {g[6]} | {g[7]} | {g[8]}
#     """
#           )
#     if g[0]==g[1] and g[1]==g[2] or g[3]==g[4] and g[4]==g[5] or g[6]==g[7] and g[7]==g[8] or g[0]==g[3] and g[3]==g[6] or g[1]==g[4] and g[4]==g[7] or g[2]==g[5] and g[5]==g[8] or g[0]==g[4] and g[4]==g[8] or g[2]==g[4] and g[4]==g[6]:
#         print('0 yutdi! tamom')
#         break


# import random
#
# word_list = ["olma", "banan", "nok", "behi", "gilos", "uzum", "malina"]
#
# word = random.choice(word_list)
#
# guesses = set()
#
# while True:
#     display = ""
#     for letter in word:
#         if letter in guesses:
#             display += letter
#         else:
#             display += ("_")
#     print(display)
#
#     if "_" not in display:
#         print("Siz yutdingiz!")
#         break
#
#
#     guess = input("taxminingiz: ")
#     guesses.add(guess)
#     if guess not in word:
#         print('Mavjud emas!')
#     else:
#         print("To'g'ri harf topdingiz!")
#
#     if len(guesses) == 10:
#         print("Urinishlar tugadi, afsus")


# # # UYGA VAZIFA

# # # PDFdagi MASALALAR
# while True:
#     svetafor = input("Svetafor qaysi rangda: ")
#     ranglar = ("qizil","yashil","sariq")
#     if svetafor in ranglar:
#         print("rahmat, to'g'ri rang")
#         break


# import random
# sonlar = [1,2,3,4,5,6,7,8,9]
# son = random.choice(sonlar)
#
# while True:
#     taxmin = input("Taxmin qiling: ")
#     if taxmin == son:
#         print("Tabriklaymiz, siz topdingiz!")
#         break
#     else:
#         print("Noto'g'ri, qayta urinib ko'ring")


# dostlar = [ ]
# while True:
#     ism = (input("Do'stingizning ismini kiriting: "))
#     dostlar.append(ism)
#     if "stop" in ism:
#         break
# print(f"Sizning do'stlaringiz ro'yxati-{dostlar})


# print("Valyuta ayirboshlash Kalkulyatori")
# print("\n1 USD = 12,600 so'm")
# print("\nChiqish uchun 'exit' deb yozing!!!")
# while True:
#     summa = (input("Summani kirting: "))
#     if summa.lower() == "exit":
#         print("Operatsiya to'xtatildi")
#         break
#     elif summa.isdigit():
#         som = float(summa)
#         som = som / 12_600
#         print(f"{summa} so'm- teng - {som} dollarga")
#     else:
#         print("Iltimos, faqat son yoki 'exit' deb yozing.\n")

"""
1. While siklidan foydalanib print qiling:
1
22
333
4444
55555
"""
# sonlar = 0
# while sonlar < 10:
#     sonlar += 1
#     print(str(sonlar)*sonlar)

"""2. While dan foydalanib sondagi raqamlar yig'indisini topadigan dastur tuzing.
input: 555   output: 15
input: 8125   output: 16"""

# son = int(input("Son kiriting: "))
# yigindi = 0
# while son > 0:
#     yigindi += son%10 # num = num + son % 10
#     son //= 10 # son = son //10
#
# print(yigindi)


""" 3. While orqali 1 dan 100 gacha bo'lgan toq solar yig'indisini topuvchi dastur tuzing"""
# son = 1
# yigindi = 0
# while son <= 100:
#     yigindi += son
#     son = son +2
# print(f"Javob: {yigindi}")


"""3. While orrqali Ro'yxatdagi 2-eng katta sonni topuvchi dastur yozing"""
# savol = "Son kiriting: "
# savol += "(sonni topish uchun 'stop' deb yozng): "
# sonlar = []
# while True:
#     son = (input(savol))
#     if son == "stop":
#         break
#     sonlar.append(int(son))
# sonlar.sort(reverse=True)
# num2 = sonlar[1]
# print(f"Ro'yxatdagi eng katta 2-son = {num2}")


#
""" 4. Taxmin qilish o'yinini simulyatsiya qiladigan dastur yarating.
Dastur 1 dan 100 gacha bo'lgan tasodifiy sonni yaratishi va
foydalanuvchidan raqamni taxmin qilishni so'rashi kerak.
Agar foydalanuvchi taxmini haqiqiy raqamdan yuqori bo'lsa, dastur "Juda baland!" va
foydalanuvchidan yana taxmin qilishni so'rang. Xuddi shunday, agar foydalanuvchining
taxmini haqiqiy raqamdan past bo'lsa, dastur "Juda past!" va foydalanuvchidan yana taxmin
qilishni so'rang. Dastur foydalanuvchidan to'g'ri raqamni topmaguncha taxmin qilishni so'rashi kerak."""

# import random
#
# sonlar = list(range(1, 101))
# son = random.choice(sonlar)
# urinishlar = []
#
# while True:
#     guess = int(input("Taxmin qiling: "))
#     urinishlar.append(guess)
#     taxminlar_soni = len(urinishlar)
#     if guess == son:
#         print("Qoyil siz to'g'ri topdingiz")
#         break
#
#     elif guess < son:
#         print("Juda past")
#     elif guess > son:
#         print("Juda baland")
# print(f"Siz {taxminlar_soni} urinishda topdingiz! Urinishlaringiz {urinishlar}")

