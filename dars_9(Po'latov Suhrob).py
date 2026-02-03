# harorat = int(input("Ob havo haroratini kiriting: "))
# if harorat < 0:
#     print("Sovuq")
#
# elif 0 <= harorat <= 20:
#     print("Salqin")
#
# elif 21<= harorat <= 30:
#     print("Iliq")
#
# else:
#     print("Issiq")


# summa = int(input("Xarid summasini kiriting: "))
# if summa < 50_000:
#     print("Chegirma yo'q")
#     print(f'Narx - {summa}')
#
# elif 50_000 <= summa <=100_000:
#     print("5% chegirma")
#     chegirma = (5/100) * summa
#     yakuniy = summa - chegirma
#     print(f'Yakuniy narx {yakuniy} so\'m')
# elif 100_000 < summa:
#     print("10% chegirma")
#     chegirma = (10/100) * summa
#     yakuniy = summa - chegirma
#     print(f'Yakuniy narx {yakuniy} so\'m')


# login = input("Login kiriting: ")
# parol = input("Parol kiriting: ")
#
# if login == "admin" and parol == "12345":
#     print("Xush kelibsiz, admin!")
# else:
#     print("Login yoki parol xato")

# age = int(input("Yoshingizni kiriting: "))
# if age < 13:
#     print("Sizga ushbu film tavsiya etilmaydi")
# elif 13 <= age <= 17:
#     print("Siz filmni ota-onangiz bilan ko'rishiz mumkin")
# else:
#     print("Siz filmni tomosha qilishingiz mumkin")



# menu = (input("Taom tanlang:\n"
#                  "1. Osh\n"
#                  "2. Shashlik\n"
#                  "3. Mastava\n"
#                  ">>> "))
# if menu == "1" or menu.lower() == "osh":
#     print("Narxi: 45.000 so'm,"
#           "Tayyorlanish vaqti: 20 minut")
# elif menu == "2" or menu.lower() == "shashlik":
#     print("Narxi: 14.000 so'm donasi,"
#           "Tayyorlanish vaqti: 30 minut")
# elif menu == "3" or menu.lower() == "mastava":
#     print("Narxi: 30.000 so'm,"
#           "Tayyorlanish vaqti: 15 minut")
# else:
#     print("Bunday taom mavjud emas!")




# email = input("Email kiriting: ")
# if email.find("@") ==0 and email.find("."):
#     print("Email qabul qilindi")
# else:
#     print("Noto'g'ri email manzil")


# ball = int(input("Yig'gan balingizni kiriting: "))
# if 86 <= ball <= 100:
#     print("5 baho")
# elif 70 <= ball <= 85:
#     print("4 baho")
# elif 55 <= ball <= 69:
#     print("3 baho")
# else:
#     print("2 baho")


# k_summa = int(input("Kartadagi summani kiriting: "))
# y_summa = int(input("Yechmoqchi bo'lgan summani kiriting:" ))
# if k_summa < y_summa:
#     print("Hisobda mablag' yetarli emas")
# elif y_summa < 5_000:
#     print("Minimal yechish summasi 5_000 so'm")
# else:
#     print("Pul muvaffaqiyatli yechildi")
#     karta = k_summa - y_summa
#     print(f"Kartada qolgan mablag'-{karta} so'm")


# kun = input("Bugun qaysi kun>>> ")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni")


# gb = int(input("Oyiga qancha GB ishlatasiz? "))
# if gb < 1:
#     print("Sizga Mini ta'rif mos keladi")
# elif 1 <= gb <= 5:
#     print("Sizga Standard ta'rif mos keladi. ")
# else:
#     print("Sizga Unlimited ta'rif mos keladi.")
