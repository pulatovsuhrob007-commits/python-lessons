# KONSTRUKTOR, DESKTRUKTOR
# VORISDORLIK, POLIMORFIZM

# # # KONSTRUKTOR

# class Student:
#
#     # construktor
#     # initialize instance varible
#
#     def __init__(self, name):
#         print("Inside Construktor")
#         self.name = name
#         print("All variables initialized")
#
#     # instancce method
#     def show(self):
#         print("Hello, my name is", self.name)
#
#
# # create object using construktor
# s1 = Student("Emma")
# s1.show()

# # # default constructor
# class Employee:
#
#     def display(self):
#         print("Inside Display")
#
# emp = Employee()
# emp.display()

# # # non-parametrized constructor
# class Company:
#
#     # no-argument constructor
#     def __init__(self):
#         self.name = "PYnative"
#         self.address = "ABC Street"
#
#     # a method for printing data members
#     def show(self):
#         print('Name:', self.name, "Address:", self.address)
#
# # creating object of the class
# cmp = Company()
#
# # calling the instance method using the object
# cmp.show()

# # # parametrized constructor
# class Employee:
#
#     # parametrized constructor
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     # display object
#     def show(self):
#         print(self.name, self.age, self.salary)
#
# # creating object of the Employee class
# emma = Employee('Emma', 23, 7500)
# emma.show()
#
# kelly = Employee('Kelly', 25, 8500)
# kelly.show()

# # konstruktor yordamida class obyektlarini sanash
# class Employee:
#     count = 0
#     def __init__(self):
#         Employee.count = Employee.count + 1
#
# # creating objects
# e1 = Employee()
# e2 = Employee()
# e3 = Employee()
# print("The number of Employees:", Employee.count)

# # # DESTRUKTOR

# class Student:
#     # constructor
#     def __init__(self, name):
#         print('Inside Constructor')
#         self.name = name
#         print('Object initialized')
#
#     def show(self):
#         print('Hello, my name is', self.name)
#
#     # destructor
#     def __del__(self):
#         print('Inside destructor')
#         print('Object destroyed')
#
# # create object
# s1 = Student('Emma')
# s1.show()
#
# # delete object
# del s1


# # # VORISDORLIK
# class Odam:
#     qollar_soni = 2
#     oyoqlar_soni = 2
#
#
# class Jangchi(Odam):
#     energiya = 100
#     jang_qiyinligi = 30
#
#     def jang_qil(self):
#         if self.energiya >= self.jang_qiyinligi:
#             self.energiya -= self.jang_qiyinligi
#             print(f"Jangda {self.jang_qiyinligi} energiya yo'qotildi, {self.energiya} qoldi.")
#         else:
#             print("Jang uchun energiya yetarli emas!")
#
# Botir = Jangchi()
# # Botir.jang_qil()
# # Botir.jang_qil()
# # Botir.jang_qil()
# # Botir.jang_qil()
# class Shifokor(Odam):
#     dorilar = ['Trimol', 'Suv']
#
#     def davola(self):
#         if len(self.dorilar) > 0:
#             dori = self.dorilar.pop()
#             print(f"{dori} yordamida davolandi!")
#         else:
#             print("Dori qolmadi!")
#
# Doniyor = Shifokor()
# # Doniyor.davola()
# # Doniyor.davola()
# # Doniyor.davola()
# class JangchiShifokor(Jangchi, Shifokor):
#     pass
#
# Superman = JangchiShifokor()
# Superman.davola()

# class Person:
#     origin_country = "USA"
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def speak(self, words):
#         print(f"{self.name} speaks: {words}")
#
# class Employee(Person):
#     def __init__(self, name, age, gender, salary, job_title):
#         super().__init__(name, age, gender)
#         self.salary = salary
#         self.job_title = job_title
#
#     def display_info(self):
#         print(f"Employee {self.name} works as a {self.job_title}")
#
# akbar = Employee('Akbar', 18, 'M', 18_000, 'Menejer')
# akbar.display_info()

# # # Diamond Problem
# class Base:
#     def call(self):
#         print("Base Class")
#
# class Left(Base):
#     def call(self):
#         print("Left Class")
#
# class Right(Base):
#     def call(self):
#         print("Right Class")
#
# class Child(Left, Right):
#     pass
#
# obj = Child()
# obj.call()                # Child -> Left -> Right -> Base -> Object
# print(Child.mro())

# # # Polimorfizm
# # Polymorphism in Built-in function len()
# students = ['Emma', 'Jesse', 'Kelly']
# school = 'ABC School'
#
# # calculate count
# print(len(students))
# print(len(school))

# class Vehicle:
#
#     def __init__(self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price
#
#     def show(self):
#         print("Details:", self.name, self.color, self.price)
#
#     def max_speed(self):
#         print("Vehicle max speed is 150")
#
#     def change_gear(self):
#         print("Vehicle change 6 gear")
#
# # inherit from vehicle class
# class Car(Vehicle):
#     def max_speed(self):
#         print("Car max speed is 240")
#
#     def change_gear(self):
#         print('Car change 7 gear')
#
# # Car object
# car = Car('Car x1', 'Red', 200000)
# car.show()
# # calls methods from Car class
# car.max_speed()
# car.change_gear()
#
# # Vehicle Object
# vehicle = Vehicle('Truck x1', 'white', 75000)
# vehicle.show()
# # calls method from a Vehicle classs
# vehicle.max_speed()
# vehicle.change_gear()

# # # UYGA VAZIFA
# # 1)
# class Texnika:
#     def __init__(self, brand, model, type):
#         self.brand = brand
#         self.model = model
#         self.type = type
#
#     def info(self):
#         print(f"Brend: {self.brand}, Model: {self.model}, Turi: {self.type}")
#
#
# class Notebooks(Texnika):
#     def __init__(self, brand, model, type, video_card, ram, display):
#         super().__init__(brand, model, type)
#         self.video_card = video_card
#         self.ram = ram
#         self.display = display
#
#     def more_info(self):
#         print(f"Brend: {self.brand}\nModel: {self.model}\nTuri: {self.type}\nVideo karta: {self.video_card}\nRam:{self.ram}\nDisplay: {self.display} ")
#
# class Televisions(Texnika):
#     def __init__(self, brand, model, type, size, display):
#         super().__init__(brand, model, type)
#         self.size = size
#         self.display = display
#
#     def more_info(self):
#         print(f"Brend: {self.brand}\nModel: {self.model}\nTuri: {self.type}\nHajmi: {self.size}\nDisplay: {self.display}")
#
# class Smartphones(Texnika):
#     def __init__(self, brand, model, type, size, sim_count):
#         super().__init__(brand, model, type)
#         self.size = size
#         self.sim_count = sim_count
#
#     def more_info(self):
#         print(f"Brend: {self.brand}\nModel: {self.model}\nTuri: {self.type}\nHajmi: {self.size}\nSim karta: {self.sim_count}")
#
# technology = Smartphones('apple', 'iPhone13', 'green', 'x', '1 and "e-sim"')
# technology.more_info()

# # 2)
# class Transport:
#     def __init__(self, brand, model, type):
#         self.brand = brand
#         self.model = model
#         self.type = type
#
#     def info(self):
#         print(f"Brend: {self.brand}, Model: {self.model}, Turi: {self.type}")
#
# class ElectroCars(Transport):
#     def __init__(self, brand, model, type, battery_life, chargin_time):
#         super().__init__(brand, model, type)
#         self.battery_life = battery_life
#         self.chargin_time = chargin_time
#
#     def more_info(self):
#         print(f"Brand -> {self.brand}\nModel -> {self.model}\nTuri -> {self.type}\nBatareyasi -> {self.battery_life}\nZaryadka vaqti -> {self.chargin_time}")
#
# class SportCars(Transport):
#     def __init__(self, brand, model, type, motor, color):
#         super().__init__(brand, model, type)
#         self.motor = motor
#         self.color = color
#
#     def more_info(self):
#         print(f"Brand -> {self.brand}\nModel -> {self.model}\nTuri -> {self.type}\nMotori -> {self.motor}\nRangi -> {self.color}")
#
# class Truck(Transport):
#     def __init__(self, brand, model, type, height, long, weight):
#         super().__init__(brand, model, type)
#         self.height = height
#         self.long = long
#         self.weight = weight
#
#     def more_info(self):
#         print(f"Brand -> {self.brand}\nModel -> {self.model}\nTuri -> {self.type}\nBalandligi -> {self.height}\nUzunligi -> {self.long}\nOg'irligi -> {self.weight}")
#
# transport = Truck('Isuzu', 'X7 Pro', '10 TONNA', '3 metre', '10 metre', '10 tonna')
# transport.more_info()

# # 3.1)
# class University:
#     def __init__(self, university):
#         self.university = university
#
#     def info(self):
#         print(f'Universitet: {self.university}')
#
# class Staff(University):
#     def __init__(self, university, first_name, last_name, age):
#         super().__init__(university)
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def more_info(self):
#         print(f"XODIM HAQIDA MA'LUMOTNOMA"
#               f"\nUniversitet: {self.university},\nIsmi: {self.first_name},\nFamilyasi: {self.last_name},\nYoshi: {self.age}")
#
# class Student(Staff):
#     def __init__(self, university, first_name, last_name, age, group):
#         super().__init__(university, first_name, last_name, age)
#         self.group = group
#
#     def more_info(self):
#         print(f"TALABA HAQIDA MA'LUMOTNOMA:"
#               f"\nUniversitet: {self.university},\nIsmi: {self.first_name},\nFamilyasi: {self.last_name},\nYoshi: {self.age}, Guruhi: {self.group}")
#
# class Teacher(Staff):
#     def __init__(self, university, first_name, last_name, age, position, subject):
#         super().__init__(university, first_name, last_name, age)
#         self.position = position
#         self.subject = subject
#
#     def more_info(self):
#         print(f"O'QITUVCHI HAQIDA MA'LUMOTNOMA"
#               f"\nUniversitet: {self.university},\nIsmi: {self.first_name},\nFamilyasi: {self.last_name},\nLavozimi: {self.position},\nMutaxasisligi (fan bo'yicha): {self.subject}")
#
# class OtherStaff(Staff):
#     def __init__(self, university, first_name, last_name, age, position):
#         super().__init__( university, first_name, last_name, age)
#         self.position = position
#
#     def more_info(self):
#         print(f"BOSHQA XODIMLAR HAQIDA MA'LUMOTNOMA:"
#               f"\nUniversitet: {self.university},\nIsmi: {self.first_name},\nFamilyasi: {self.last_name},\nLavozimi: {self.position}")
#
#
#
# # # 3.2)
# class Object(University):
#     def __init__(self, university, name):
#         super().__init__(university)
#         self.name = name
#     def object_info(self):
#         print(f"UNIVERSITETDAGI OBYEKTLAR"
#               f"\nUniversitet: {self.university}, Obyekt nomi: {self.name}")
# class Computer(Object):
#     def __init__(self, university, name, soni, tizimi, holati):
#         super().__init__(university, name)
#         self.soni = soni
#         self.tizimi = tizimi
#         self.holati = holati
#
#     def object_more_info(self):
#         print(f"KOMPYUTER (OBYEKT) HAQIDA MA'LUMOT"
#               f"Universitet: {self.university},\nObyekt nomi: {self.name}\nMiqdori: {self.soni}\nOperatsion tizimi: {self.tizimi}\nHolati: {self.holati}")
# class Mebel(Object):
#     def __init__(self, university, name, soni, turi, holati):
#         super().__init__(university, name)
#         self.soni = soni
#         self.turi = turi
#         self.holati = holati
#
#     def object_more_info(self):
#         print(f"Universitet: {self.university},\nObyekt nomi: {self.name}\nMiqdori: {self.soni}\nTuri: {self.turi}\nHolati: {self.holati}")
#