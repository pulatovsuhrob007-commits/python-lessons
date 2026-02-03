# hash table -> dict
# CRUD - Create, Read, Update, Delete

# d = {"ism":"Nodir", "yoshi":23}    # -> sinteks orqali yaratalishi
# d2 = dict(ism="Nodir", yoshi=23)   # -> Funksiya orqali yaratilishi
# d3 = dict([("ism", "Nodir"), ("yoshi", 23)]) # -> List of tuples orqali yaratilishi
# d["ball"] = [5,4,3]        # yangi key-value yaratildi
# print(d["ball"])
# print(d2)
# print(d3)

# duplicated_keys = {"key1": "value1", "key1": "value2", "key1": "value3"}
#
# # Access key1
# print(duplicated_keys["key1"])

### Update qilish
# harry_potter_dict = {
#     "Harry Potter": "Gryffindor",
#     "Ron Weasley": "Gryffindor",
#     "Hermione Granger": "Gryffindor"
# }
#
# add_characters_1 = {
#     "Albus Dumbledore":"Gryffindor",
#     "Luna Lovegood":"Ravenclaw"
# }                                           # =====>>>> dict qo'shish
# harry_potter_dict.update(add_characters_1)
# print(harry_potter_dict)
#
# add_characters_2 = [
#     ["Draco Malfoy", "Slytherin"],
#     ["Cedric Diggory", "Hufflepuf"]
# ]                                           # =====>>>> list qo'shsak = key-value
# harry_potter_dict.update(add_characters_2)
#
# print(harry_potter_dict)
#
# add_characters_3 = [
#     ("Rubeus Hagrid", "Gryffindor"),
#     ("Minerva McGonagall", "Gryffindor")
# ]                                           # =====>>>> tuple qo'shsak = key-value
# harry_potter_dict.update(add_characters_3)
# print(harry_potter_dict)

#### dict methods ###

### .popitem() metodi
# harry_potter_dict["Voldemort"] = "Slytherin"
#
# print("Dictionary with Voldemort:")
# print(harry_potter_dict)
# print()

# # Remove the last inserted item (Voldemort)
# harry_potter_dict.popitem()
#
# print("Dictionary after popping the last inserted item (Voldemort):")
# print(harry_potter_dict)

### .get(key) metodi
# new = harry_potter_dict.get("RonWeasley", "None")
# print(new)

# from collections import Counter
#
# counter = Counter(harry_potter_dict.values())
# print(counter)

# # # UYGA VAZIFA # # #
##1.
# def str_counter(strs):
#     lugat = {}
#     for s in strs:
#         keys = len(s)
#         if keys not in lugat:
#             lugat[keys] = s
#     return lugat
#
# print(str_counter(['shaftoli', 'olma', 'nok']))

##2.
# def merge_list(l1, l2):
#     lugat = {}
#     for i in range(len(l1)):
#         lugat[l1[i]]=l2[i]
#     return lugat
# list_1 = ["a", "b", "c"]
# list_2 = [1, 2, 3]
# print(merge_list(list_1 ,list_2))

##3.
# contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"}
# def show_menu():
#     print("\n******* Telefon kontaktlar ro'yxati *******")
#     print("1.Mavjud kontaktlarni ko'rish; ")
#     print("2. Kontakt qo'shish;")
#     print("3.Kontaktlarni yangilash;")
#     print("4.Kontaktlarni o'chirish;")
#     print("5.Kontaktlarni qidirish")
#     print("6. Dasturdan chiqish")
# def view_contacts():
#     print("\nMavjud kontaktlar:")
#     for ism, raqam in contacts.items():
#             print(f"{ism}: {raqam}")
#
# def add_contact():
#     name = input("Qo'shmoqchi bo'lgan kontakt Ismi: ")
#     phone = input("Raqamini kiriting: ")
#     if name in contacts:
#         print("Bu kontakt mavjud !")
#     else:
#         contacts[name] = phone
#         print(f"'{name}' muvaffaqiyatli qo'shildi.")
# def update_contact():
#     name= input("Yangilanadigan ismni kiriting: ")
#     if name in contacts:
#         new_phone = input("Yangilanadigan raqamni kiriting: ")
#         contacts[name]=new_phone
#         print(f"'{name}' muvaffaqiyatli yangilandi.")
#     else:
#         print('Kontakt topilmadi.')
# def del_contact():
#     name = input("O'chirmoqchi bo'lgan kontakt Ismi: ")
#     if name in contacts:
#         del contacts[name]
#         print(f"'{name}' kontaktdan muvaffaqiyatli o'chirildi.")
#     else:
#         print(f"'{name}' kontakt topilmadi")
# def find_contact():
#     name = input("Qidirmoqchi bo'lgan kontakt Ismi: ")
#     if name in contacts:
#         print(f"{name}: {contacts[name]}")
#     else:
#         print("Hech narsa topilmadi ):")
#
# def main():
#     while True:
#         show_menu()
#         tanlov = (input(">>>>>>>Kerakli operatsiyani tanlang(1-6)>>>>>"))
#
#         if tanlov == '1':
#             view_contacts()
#         elif tanlov == '2':
#             add_contact()
#         elif tanlov == '3':
#             update_contact()
#         elif tanlov == '4':
#             del_contact()
#         elif tanlov == '5':
#             find_contact()
#         elif tanlov == '6':
#             print("Dasturdan muvaffaqiyatli chiqildi. Xayr!")
#             break
#         else:
#             print("Noto'g'ri tanlov qilyabsiz. Iltimos boshqa tanlov qiling!!!")
# main()

# #4. def counter_dict(nums):
# def counter_dict(nums):
#     from collections import Counter
#
#     counts = Counter(nums)
#     result_dict = dict(counts)
#
#     print(result_dict)
# counter_dict([2,1,1,2, 3,1])

#5.
# def max_ball_students(students):
#     ballar = sorted(students.values(), reverse=True)
#     top1, top2 = ballar[0], ballar[1]
#     lugat = {}
#     for ism, ball in students.items():
#         if ball == top1:
#             lugat[ism] = ball
#             print(f"Eng yaxshi 1-o'quvchi {ism} - {ball}.")
#             break
#     for ism, ball in students.items():
#         if ball == top2:
#             lugat[ism]= ball
#             print(f"Eng yaxshi 2-o'quvchi {ism} - {ball}.")
#             break
#
#
#
# max_ball_students({"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80 })













