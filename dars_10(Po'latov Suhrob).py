#A1 guruh
# Po'latov Suhrob

#1-masala
# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for pochta in pochtalar:
#
#     if "@" in pochta:
#         print(f"To'g'ri: {pochta}")
#     else:
#         print(f"Noto'g'ri email: {pochta}")

#2-masala
# parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]
# for i in parollar:
#     if len(i) < 8:
#         print("Juda qisqa")
#     elif i.isalnum():
#         print("Kuchsiz parol")
#     else:
#         print("Kuchli parol")

#3-masala
# harorat = [20, 22, 19, 24, 25, 23, 21]
# ortacha = int(sum(harorat)/len(harorat))
# print(f"{ortacha} C-o'rtacha harorat")
# for x in harorat:
#     if x > 22:
#         print(f"{x}-Iliq kun")
#     else:
#         print((f"{x}-Salqin kun"))

#4-masala
# taomlar = ["osh", 'shashlik', 'manti', 'lag\'mon']
# print(taomlar)
# buyurtma = input('Buyurtmani kriting: ')
# for taom in taomlar:
#     if buyurtma.lower() in taomlar:
#         print("Buyurtma qabul qilindi")
#         break
#     else:
#         print("Kechirasiz, bunday taom yo'q")
#         break

#2-USUL
# if buyurtma.lower() in taomlar:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Buyurtma yo'q")
#5-masala
# yosh = [16, 21, 17, 30, 25]
# for i in yosh:
#     if i < 18:
#         print('Yosh chegarasiga yetmagan')
#     else:
#         print('xush kelibsiz')

#6-masala
# xabarlar = ["Yang xabar", "Batareya past", "Yangilanish mavjud"]
# for i in xabarlar:
#     if i == "Batareya past":
#         print("Telefoningiznni quvvatlang")
#     else:
#         print("bildirishnoma")

#7-masala
# fayllar= ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
# musiqalar = [ ]
# rasmlar = [ ]
# for f in fayllar:
#     if ".jpg" in f:
#         rasmlar.append(f)
#     elif ".mp3" in f:
#         musiqalar.append(f)
# print(f"Musiqa - {musiqalar}")
# print(f"Rasm - {rasmlar}")