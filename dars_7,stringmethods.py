# 1.capitalize()-birinchi harfni katta harfga aylantiradi
tekst = "bu mening birinchi topshirig'im."
x = tekst.capitalize()
print(x)
# 2.casefold()- har bitta harfni kichraytiradi
# tekst = "I lovE Banana!"
# y = tekst.casefold()
# print(y)
# 3.center()- matnni markazlashtiradi
# tekst = "Lets go"
# u = tekst.center(200)
# print(u)
# 4.count()- matnni ichidagi belgini sanab beradi
# tekst = "Mening vatanim O'zbekiston.Men O'zbekistonga qaytdim"
# x = tekst.count('O\'zbekiston')
# print(x)
# 5.endswith- matn nima bilan tugaganini tekshirsa boladi
# tekst = "Hello123"#
# x = tekst.endswith("3")
# print(x)
# 6.startswith-matnni nima bilan boshlanganini bilsa boladi
# teskt = "Hello123"
# x = teskt.startswith("g")
# print(x) natija False
# 7.expandtabs() - matnni orasiga probel qoyib beradi
# text = "Men\tu\ty\tg\ta\tketdim"
# x = text.expandtabs(2)
# print(x)
# 8.find() - matnni ichidan topib beradi
# txt = "Mening Vatanim O'zbekiston"
# x = txt.find("Vatanim")
# print(x)
# 9.index() - matnni ichidan topib beradi = "find". Farqi find da yo'q narsani qidirsak -1 chiqarib beradi bunda kodni xato hisoblaydi
# txt = "Toshkent O'zbekistonning poytaxti"
# x = txt.find("poytaxt")
# print(x)
# 10.isalnum() - matnni ichida harf yoki son bor
# txt = "12357"
# x = txt.isalnum()
# print(x)
# 11.isalpha() - matn harflardan tashkil topgan
# txt = "matnni ichida harf bor - false"
# y = txt.isalpha()
# print(y)
# 12.isascii() - matn ascii jadvaldagi ishoralardan tashkil topgan
# txt = "Matn ascii ishoralardan tashkil topgan TRUE"
# x = txt.isascii()
# print(x)
# 13.isdecimal - desimal ya'ni 0 dan 9 gacha sonlar shu jumladan kasr sonlar ham
# txt = "1234"
# x = txt.isdecimal()
# print(x)
# 14.isdigit - hamma ishora raqam bob kegan, decimaldan farqi bunda raqam,lar boladi
# txt = "45678"
# x = txt.isdigit()
# print(x)
# 15. isidentifier - matnda ism bor
# txt = "Dilmurod"
# x = txt.isidentifier()
# print(x)
# 16. islower - hamma harflar kichkina
# txt = "hamma harfalar kichkina"
# x = txt.islower()
# print(x)
# 17.isnumeric - sonlardan tashkil topgan. (bunda masalan 100 sonlari ham kirib ketadi)
# txt = "10020001000"
# x = txt.isnumeric()
# print(x)
# 18.inspace - matn bo'shliqdan tashkil topgan
# txt = "         "
# x = txt.isspace()
# print(x)
# 19.isprintable - hamma ishoralar yoziladigan
# txt = "Hello! are you #1?"
# k = txt.isprintable()
# print(k)
# 20.istitle - sarlavhani qoidalariga bo'ysunadi ya'ni bosh harf katta qoganlari kichik bolishi kerak
# kol = "Hello String"
# k = kol.istitle()
# print(k)
# 21.isupper() - matndagi hamma ishora katta
# kol = "MATNDAGI HAMMA ISHORA KATTA"
# k = kol.isupper()
# print(k)
# 22.join() - ro'yxatlarni ya'ni tuple yoki list ni string ga yig'ib beradi
# kol = ["1", "2", "3"]
# k = "#######".join(kol)
# print(k)
# 23.ljust - matnning chap tarafani to'ldirib beradi
# kol = "banana"
# k = kol.ljust(20, "o")
# print(k)
# 24.lower() - matnni kichkina harfalrda ifodalaydi
# kol = "MATN KICHKINA HARFLARGA AYLANTIRILDI"
# k = kol.lower()
# print(k)
# 25.strip - matnndagi (faqat boshi va oxiridagi) "пробелъ"ni ob tashaydi
# kol = "     Orasi ochiq matn      "
# k = kol.strip()
# print(k)
# 26.lstrip - matnnning faqat chap tarafidagi oraliqni ob tashaydi
# kol = "      Chap tarafi ochilgan matn"
# k = kol.lstrip()
# print(k)
# 27.rstrip - matnning faqat o'ng tarafidagi oraliqni ob tashaydi
# kol = "O'ng tarafiga bo'sh joy tashab ketilgan      "
# k = kol.rstrip()
# print(k)
# 28.maketrans - ascii jadvalidagi ishoralarni almashtirish
# kol = "Hello Sam!"
# almashtirish = str.maketrans("S", "P")
# print(kol.translate(almashtirish))
# 29 translate - ascii jadvalidagi ishoralarni almshtirish
# mydict ={83: 115}
# kol = "HEllo SamS!"
# print(kol.translate(mydict))
# 30.replace - matnni ichidagi qiymatni almashtirish
# kol = "Men bananlarni yoqtiraman"
# k = kol.replace("bananlarni", "Olmalarni")
# print(k)
# 31.rindex - topib beradi lekin kop bolsa oxirgisini oladi
# kol = "Hello, welcome to my World."
# k = kol.rindex("e")
# print(k)
# 32.title - sarlavha qoidasiga kora birinchi harfni katta harf bilan boshlaydi
# kol = "hello, welcome  to my 2nd world!"
# k = kol.title()
# print(k)
# 33.split() - matnni listga o'girib beradi joinni teskarisi
# kol = ("welcometothejungle")
# k = kol.split("t")
# print(k)
# 34.upper() - matnni katta harfga o'tkazadi
# kol = "welcome to the jungle"
# k = kol.upper()
# print(k)
# 35.zfill() - matnni boshidan "0" bilan to'ldirib ketadi
# kol = "NOl"
# k = kol.zfill(20)
# print(k)
