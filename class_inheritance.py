# class Base:
#     height = 175
#     eye_color = 'green'
#     hair_color = 'brown'
#     age = 20
#
#     def trade_in_ninja(self):
#         print("Ninja trading")
#
#
# class Base2:
#     height = 180
#     eye_color = 'green'
#     hair_color = 'dark brown'
#     age = 20
#
#
# Employee1 = Base()
# Employee2 = Base2()
#
# print(Employee1.age)
# print(Employee1.trade_in_ninja())
# Employee2 = Base2('Ivan', 'Ivanov')
# print(Employee2.name, Employee2.surname)


# class Interior_items:
#
#     def __init__(self, name, material, size, color):
#         self.name = name
#         self.material = material
#         self.size = size
#         self.color = color
#
#     def characteristics(self):
#         print(f'name: {self.name}; material: {self.material}; size: {self.size}; color: {self.color}')
#
#
# class Chair(Interior_items):
#
#     def change_of_size(self):
#         print('do you know the exact size? YES/NO')
#         answer = input()
#         if answer == 'YES':
#             print('do you want to change info about size?')
#             new_size = input()
#             self.size = new_size
#
#
# class Table(Interior_items):
#     ...
#
#
# class Lamp(Interior_items):
#
#     def status(self):
#         # self.status = status
#         print('is the lamp on? YES/NO')
#         answer = input()
#         if answer == 'YES':
#             self.status = 'the lamp is turned on'
#         elif answer == 'NO':
#             self.status = 'the lamp is turned off'
#         return self.status
#
#
# chandelier = Lamp('Chandelier', 'Metal, Plastic, Glass', 'Standard', 'Black')
# office_chair = Chair('Office Chair', 'Metal, Plastic, Leather', 'Standard', 'Black, Silver')
# writing_desk = Table('Writing Desk', 'Wood', '120x65', 'Dark brown')
# writing_desk.characteristics()
# office_chair.characteristics()
# chandelier.characteristics()
# print(chandelier.status())
# office_chair.change_of_size()
# office_chair.characteristics()



# класс школа +
# список всех учеников (переменная) +
# метод, добавляющий нового обучающегося в список +
# название школы +
# изменение названия +
# получение адреса
# изменение адреса +
#
# класс ученик +
# имя, класс, рост, вес, возраст +
# магический метод __str__, должен возвращать имя ученика
#
# 3 учеников, наследующиеся от класса ученик
# название : имя ученика, student
#
#
# создание школы, задаю название и адрес +
# создание 3х учеников
# добавляю этих учеников в школу
# вывести список всех учеников школы +


# class School:
#
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#         self.students_list = []
#
#     def add_student(self, student_name):
#         self.students_list.append(student_name)
#
#     def change_address(self):
#         print('give the school a new address')
#         new_address = input()
#         self.address = new_address
#
#     def change_name(self):
#         print('give the school a new name')
#         new_name = input()
#         self.name = new_name
#
#
# class Student:
#
#     def __init__(self, student_name, student_class, height, weight, age):
#         self.student_name = student_name
#         self.student_class = student_class
#         self.height = height
#         self.weight = weight
#         self.age = age
#
#     def __call__(self):
#         return self.student_name
#
#
# school = School('Gymnasium', 'Dolgoprudny')
# student1 = Student('Sergey', 10, 183, 71, 16)
# student2 = Student('Andrew', 5, 160, 43, 11)
# student3 = Student('John', 12, 203, 65, 18)
# school.add_student(student1())
# school.add_student(student2())
# school.add_student(student3())
# print(school.students_list)



# создать класс здание
# метод, устанавливающий число этажей
# метод, устанавливающий адрес здания
# (применить декоратор abstractmethod)
#
#
# создать класс, наследующийся от первого
# метод, устанавливающий число этажей
# метод, устанавливающий адрес здания
# метод, возвращающий имя здания (применить декоратор staticmethod)

# from abc import ABC, abstractmethod
#
# class Building(ABC):
#
#     def __init__(self, floors, address):
#         self.floors = floors
#         self.address = address
#
#     @abstractmethod
#     def set_floors(self):
#         pass
#
#     @abstractmethod
#     def set_address(self):
#         pass
#
#
# class Project(Building):
#
#     def set_floors(self):
#         print('set the number of floors')
#         new_floors = input()
#         self.floors = new_floors
#
#     def set_address(self):
#         print('set the address')
#         new_address = input()
#         self.address = new_address
#
#     @staticmethod
#     def return_name():
#         return "NMkdskfds"


# Прочитать файл (pickle python)
# Разбить текст на массив (каждая строчка - один элемент в массиве) (file readlines python)
# Разбить первую строчку на массив по словам (split python)
# Заменить пробелы в строчке на нули (replace python)
# Сохранить строчку в новый файл с названием format.txt (pickle save)

# import pickle
# import pandas as pd
#
# with open('text.txt', encoding="utf-8") as reader:
#     data = reader.readlines()
#     string = data[0].replace(' ', '0')
# print(string)
#
# with open('format.txt', 'w+') as writer:
#     writer.write(string)




