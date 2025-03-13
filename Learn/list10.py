
## user_input = input("Введите что-нибудь: ")  # Ввод от пользователя
## print("Вы ввели:", user_input)                # Вывод информации
## help(print)                                   # Вывод справки о функции
## directory = dir([1, 2, 3])                   # Список методов и атрибутов объекта
## variables = vars()                            # Возвращает словарь локальных переменных

# print(user_input, directory, variables)

# ↓ input
# name = input("Введите ваше имя: ")
# print("Привет, " + name + "!")

# age = input("Введите ваш возраст: ")
# age = int(age)  # Преобразование строки в целое число
# print("Вам " + str(age) + " лет.")

# try:
#     number = input("Введите число: ")
#     number = float(number)  # Преобразование строки в число с плавающей точкой
#     print("Вы ввели число:", number)
# except ValueError:
#     print("Ошибка: введено не число!")

# values = input("Введите три числа, разделенные пробелами: ")
# numbers = values.split()  # Разделение строки на список
# numbers = [int(num) for num in numbers]  # Преобразование каждого элемента в целое число
# print("Вы ввели числа:", numbers)

# while True:
#     user_input = input("Введите 'exit' для выхода: ")
#     if user_input.lower() == 'exit':
#         print("Выход из программы.")
#         break
#     else:
#         print("Вы ввели:", user_input)

# ↑ input

# ↓ print
# print("Привет, мир!")

# name = "Алексей"
# age = 25
# print("Имя:", name, "Возраст:", age)  # Вывод: Имя: Алексей Возраст: 25

# print("Я", "люблю", "Python", sep="-")  # Вывод: Я-люблю-Python

# print("Это первая строка", end=", ")
# print("а это вторая строка.")  # Вывод: Это первая строка, а это вторая строка.

# name = "Ольга"
# age = 30
# print(f"Имя: {name}, Возраст: {age}")  # Использование f-строк

# with open("output.txt", "w") as file:
#     print("Это будет записано в файл.", file=file)

# import sys
# print("Это сообщение будет немедленно сброшено.", flush=True)

# ↑ print

# ↓ help
# help(print)

# import math
# help(math)

# class MyClass:
#     """Это мой класс."""
    
#     def my_method(self):
#         """Это метод класса."""
#         pass

# help(MyClass)

# help(Exception)

# help()

# ↑ help

# ↓ dir
# print(dir(str))  # Список методов и атрибутов для строк

# class MyClass:
#     def my_method(self):
#         pass

# obj = MyClass()
# print(dir(obj))  # Выводит атрибуты и методы объекта obj

# print(dir())  # Выводит список имен в текущей области видимости

# import math
# print(dir(math))  # Список функций и констант в модуле math

# print(dir([]))  # Выводит методы и атрибуты для списка

# ↑ dir

# ↓ vars
# class MyClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# obj = MyClass("Алексей", 30)
# print(vars(obj))  # Вывод: {'name': 'Алексей', 'age': 30}

# x = 10
# y = 20
# print(vars())  # Вывод: {'x': 10, 'y': 20}

# my_list = [1, 2, 3]
# print(vars(my_list))  # Вывод: {'0': 1, '1': 2, '2': 3, ...} (может не работать для встроенных типов)

# ↑ vars
