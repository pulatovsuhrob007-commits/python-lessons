# # # Instance va class methodlar

# class Student:
#     school_name = "ABC School"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def change_school(cls, school_name):
#         # class_name.class_variable
#         cls.school_name = school_name
#
#     # instance method
#     def show(self):
#         print(self.name, self.age, 'school:', Student.school_name)
#
# jessa = Student('Jessa', 20)
# jessa.show()
#
# # change school_name
# Student.change_school('XYZ School')
# jessa.show()

# # # USING CLASS METHOD TO CREATING 'FACTORY METHOD'.

# from datetime import date
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def calculate_age(cls, name, birth_year):
#         # calculate age an set it as a age
#         # return new object
#         return cls(name, date.today().year - birth_year)
#
#     def show(self):
#         print(self.name + "'s age is: " + str(self.age))
#
# jessa = Student('Jessa', 20)
# jessa.show()
#
# # create new object using the factory method
# joy = Student.calculate_age("Joy", 1995)
# joy.show()

# # # Static methods

# # ODDIY static method
# class Employee:
#     @staticmethod
#     def sample(x):
#         print('Inside static method', x)
#
# # call static method
# Employee.sample(10)
#
# # can be called using object
# emp = Employee()
# emp.sample(10)

# # Ba'zan biz class ga tegishli bo'lgan kod yoamiz lekin u obyektga bog'liq bo'lmaydi
# class Employee(object):
#
#     def __init__(self, name, salary, project_name):
#         self.name = name
#         self.salary = salary
#         self.project_name = project_name
#
#     @staticmethod
#     def gather_requirement(project_name):
#         if project_name == 'ABC PRoject':
#             requirement = ['task_1', 'task_2', 'task_3']
#         else:
#             requirement = ['task_1']
#         return requirement
#
#     # instance method
#     def work(self):
#         # call static method form instance method
#         requirement = self.gather_requirement(self.project_name)
#         for task in requirement:
#             print('Completed', task)
#
# emp = Employee('Kelly', 12000, 'ABC Project')
# emp.work()

# # Static metodni boshqa metoddan turib ham chaqirish mumkin
# class Test:
#     @staticmethod
#     def static_method_1():
#         print('static method 1')
#
#     @staticmethod
#     def static_method_2():
#         Test.static_method_1()
#
#     @classmethod
#     def class_method_1(cls):
#         cls.static_method_2()
#
# # call class method
# Test.class_method_1()

# # # ENCAPSULATION
# class Employee:
#     def __init__(self, name, project):
#         self.name = name
#         self.project = project  # Data members
#
#     def work(self):
#         print(self.name, 'is working on', self.project) # Method
#
# class Employee:
#     # constructor
#     def __init__(self, name, salary, project):
#         # data members
#         self.name = name
#         self.salary = salary
#         self.project = project
#
#     # method
#     # to display employee's details
#     def show(self):
#         # accessing public data member
#         print("Name: ", self.name, 'Salary:', self.salary)
#
#     # method
#     def work(self):
#         print(self.name, 'is working on', self.project)
#
# # creating object of a class
# emp = Employee('Jessa', 8000, 'NLP' )
#
# # calling public method of the class
# emp.show()
# emp.work()
# # # DATA HIDING

# # Public member
# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data members
#         self.name = name
#         self.salary = salary
#
#     # public instance methods
#     def show(self):
#         # accessing public data member
#         print('Name: ', self.name, 'Salary:', self.salary)
#
# # creating object of a class
# emp = Employee('Jessa', 10000)
#
# # accessing public data members
# print('Name: ', emp.name, 'Salary:', emp.salary)
#
# # calling public method of the class
# emp.show()

# # Private member
# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary
#
# # creating object of a class
# emp = Employee("Jessa", 10000)

# accessing private data members
# print("Salary:", emp.__salary)   # ->>> Error 404

# # 1. public metod yaratish orqali private ga murojaat qilish
# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary

#     # public instance methods
#     def show(self):
#         # private members are accessible from a class
#         print("Name: ", self.name, "Salary:", self.__salary)
#
# # creating object of a class
# emp = Employee('Jessa', 10000)
#
# # calling public method of the class
# emp.show()

# 2. name mangling orqali public va protected memberlarga murojaat qilish
# # ---------ObyektNomi._ClassNomi._PrivateMemberNomi---------
# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary
#
# # creating object of a class
# emp = Employee('Jessa', 10000)
#
# print('Name:', emp.name)
# # direct access to private member using name mangling
# print('Salary:', emp._Employee__salary)

# # Protected Member
# # base class
# class Company:
#     def __init__(self):
#         # Protected member
#         self._project = "NLP"
#
# # child class
# class Employee(Company):
#     def __init__(self, name):
#         self.name = name
#         Company.__init__(self)
#
#     def show(self):
#         print("Employee name:", self.name)
#         # Accessing protected member in child class
#         print("Working on project:", self._project)
#
# c = Employee("Jessa")
# c.show()
#
# # Direct access protected data member
# print('Project:', c._project)

# # # GETTER va SETTER metodlar
# # private variable larga to’g’ridan-to’g’ri murojaat qilishdan qochish uchun
# class Student:
#     def __init__(self, name, age):
#         self.name = name  # public member
#         self.__age = age  # private member
#
#     # getter method
#     def get_age(self):
#         return self.__age
#
#     # setter method
#     def set_age(self, age):
#         self.__age = age
#
#
# stud = Student('Jessa', 14)
#
# # retrieving age using getter
# print('Name:', stud.name, stud.get_age())
#
# # changing age using setter
# stud.set_age(16)
#
# # retrieving age using getter
# print('Name:', stud.name, stud.get_age())







###########################################################################################################
# # # UYGA VAZIFA

#1)
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def deposit(self, miqdor):
#         if miqdor > 0:
#             self.balance += miqdor
#             print(f"Bank hisobingizga {miqdor} miqdorda mablag' Omonat qo'yildi,"
#                   f"\nJoriy hisobingiz: {float(self.balance)}")
#
#         else:
#             print("Noto'g'ri buyruq!")
#     def withdraw(self, withdraw):
#         if withdraw < self.balance:
#             self.balance -= withdraw
#             print(f"Bank hisobingizdan {float(withdraw)} miqdorda pul yechib olindi!\nQoldiq:{float(self.balance)}")
#
#         elif withdraw > self.balance:
#             print("Balansingizda yetarli mablag' mavjud emas")
#
#         else:
#             print("Noto'g'ri buyruq!")
#     def check_balance(self):
#         return f"Siznig balansingiz {float(self.balance)}"
#
# mijoz = BankAccount(100)
# mijoz.deposit(50)
# mijoz.withdraw(99)
# print(mijoz.check_balance())

#2)
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         area = self.length*self.width
#         return f"Area: {area}"
#     def perimetre(self):
#         perimetre = 2*(self.length*self.width)
#         return f'Perimetre: {perimetre}'
#     def is_square(self):
#         if self.length == self.width:
#             print("The Rectangle is Square")
#         else:
#             print("The Rectangle isn't Square")
#
# shakl = Rectangle(4, 5)
# print(shakl.area())
# print(shakl.perimetre())
# shakl.is_square()

#3)
# class Student:
#     def __init__(self, name, age):
#         self.name  = name
#         self.age = age
#         self.grades = []
#     def add_grade(self, grade):
#         if 2 <= grade <= 5:
#             self.grades.append(grade)
#             print(f"'{grade}' appended into {self.grades} (grades list)")
#         elif grade < 2 or grade > 5:
#             print('Grade must be between 2 and 5')
#         else:
#             print("❌ Invalid input. Please enter numbers between 2 and 5!")
#     def calculate_average(self):
#         return sum(self.grades) / len(self.grades)
#     def print_summary(self):
#         gpa = float(self.calculate_average())
#         print("===== STUDENT SUMMARY =====")
#         print(f"Name   : {self.name}")
#         print(f"Age    : {self.age}")
#         print(f"Grade  : {str(self.grades)}")
#         print(f"GPA    : {gpa:.2f}")
#         print("===========================")
# student = Student("John", 18)
# student.add_grade(5)
# student.add_grade(5)
# student.add_grade(3)
# print(student.calculate_average())
# student.print_summary()

#4)
# class Circle:
#     def __init__(self, radious):
#         self.radious = radious
#     def area(self):
#         return 3.14*(self.radious**2)
#     def circumference(self):
#         return 2*3.14*self.radious
#     def diameter(self):
#         return 2*self.radious
# circle1 = Circle(7)
# print(circle1.area())
# print(circle1.circumference())
# print(circle1.diameter())

#5)
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.current_page = 1
#
#     def open(self, page):
#         if page >= 1:
#             self.current_page = page
#             return self.current_page
#         else:
#             return f'Page number must be grater than 1!'
#     def turn_page(self):
#         self.current_page += 1
#         print(self.current_page)
#
#     def restart(self):
#         self.current_page = 1
#         print(self.current_page)
# book = Book("Dasturlash asoslari", "Anvar Narzullayev")
# print(book.open(51))
# book.turn_page()
# book.restart()

#6)
# class Dog:
#     total_dogs = 10
#     @classmethod
#     def get_total_dogs(cls):
#         return cls.total_dogs
#
# dogs = Dog.get_total_dogs()
# print(dogs)

#7)
# class Computer:
#     total_computers = 2
#     computers_list = ['Acer Aspire 3', 'Asus Expertbook']
#     @classmethod
#     def add_computer(cls, comp):
#         cls.computers_list.append(comp)
#         cls.total_computers += 1
#         return cls.computers_list
# comps = Computer.add_computer("Tuff Gaming Edition")
# comps = Computer.add_computer("HP Victus 15")
# print(comps)
# print(Computer.total_computers)

#8)
# class Employee:
#     total_employees = 2
#     employees_list = ['John', 'Jessa']
#     @classmethod
#     def hire_employee(cls, name):
#         cls.employees_list.append(name)
#         cls.total_employees += 1
#         return cls.employees_list
# emps  = Employee.hire_employee('Doe')
# emps = Employee.hire_employee('Anna')
# print(emps)
# print(Employee.total_employees)

#9)
# class Television:
#     average_screen_size = 45
#     @classmethod
#     def update_average_screen_size(cls, new):
#         cls.average_screen_size = new
#         return cls.average_screen_size
# new = Television.update_average_screen_size(720)
# print(new)

#10)
# class Course:
#     total_courses = 3
#     courses_list = ['AI-Learning', 'Python Backend', 'English']
#     @classmethod
#     def add_course(cls, new_course):
#         cls.courses_list.append(new_course)
#         cls.total_courses += 1
#         return cls.courses_list
# new = Course.add_course('Machine Learning')
# new = Course.add_course('Frontend Programming')
# print(new)
# print(Course.total_courses)

#11)
# class Math:
#     @staticmethod
#     def multiple(x, y):
#         return x*y
# print(Math.multiple(4,5))

#12)
# class Temperature:
#     @staticmethod
#     def celsius_to_fahrenheit(x):
#         return (x*(9/5))+32
# print(Temperature.celsius_to_fahrenheit(25))

#13)
# class Distance:
#     @staticmethod
#     def miles_to_kilometers(x):
#         return x * 1.60934
# mile = Distance.miles_to_kilometers(10)
# print(mile)

#14)
# class Utility:
#     @staticmethod
#     def is_even(x):
#         if x%2 == 0:
#             return "Number is Even"
#         else:
#             return 'Number is Odd'
# check = Utility.is_even(9)
# print(check)

#15)
# class Time:
#     @staticmethod
#     def seconds_to_minutes(x):
#         return x/60
# seconds = Time.seconds_to_minutes(250)
# print(seconds)












