
## length = len("Hello")      # Длина строки
## data_type = type(123)      # Тип переменной
## is_instance = isinstance(123, int)  # Проверка типа

# print(length, data_type, is_instance)

# ↓ len()
# print("Frontend")
# # Длина строки
# my_string = "Hello, World!"
# length_of_string = len(my_string)
# print(length_of_string)  # Вывод: 13

# # Длина списка
# my_list = [1, 2, 3, 4, 5]
# length_of_list = len(my_list)
# print(length_of_list)  # Вывод: 5

# # Длина кортежа
# my_tuple = (10, 20, 30)
# length_of_tuple = len(my_tuple)
# print(length_of_tuple)  # Вывод: 3

# # Длина множества
# my_set = {1, 2, 3, 4, 5}
# length_of_set = len(my_set)
# print(length_of_set)  # Вывод: 5

# # Длина словаря
# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# length_of_dict = len(my_dict)
# print(length_of_dict)  # Вывод: 3 (количество ключей)

# # Длина пустых коллекций
# empty_list = []
# empty_string = ""
# empty_dict = {}

# print(len(empty_list))   # Вывод: 0
# print(len(empty_string))  # Вывод: 0
# print(len(empty_dict))    # Вывод: 0

# # Длина вложенных структур
# nested_list = [[1, 2], [3, 4, 5], [6]]
# length_of_nested_list = len(nested_list)
# print(length_of_nested_list)  # Вывод: 3 (количество подсписков)

# # Применение len() в условиях
# if len(my_list) > 3:
#     print("Список содержит больше трех элементов.")  # Вывод: Список содержит больше трех элементов.

# ↑ len()

# ↓ type()
# Определение типа переменной
# my_string = "Hello, World!"
# print(type(my_string))  # Вывод: <class 'str'>

# my_integer = 42
# print(type(my_integer))  # Вывод: <class 'int'>

# my_float = 3.14
# print(type(my_float))    # Вывод: <class 'float'>

# my_list = [1, 2, 3]
# print(type(my_list))     # Вывод: <class 'list'>

# my_dict = {"key": "value"}
# print(type(my_dict))     # Вывод: <class 'dict'>

# # Определение типа кортежа и множества
# my_tuple = (1, 2, 3)
# print(type(my_tuple))    # Вывод: <class 'tuple'>

# my_set = {1, 2, 3}
# print(type(my_set))      # Вывод: <class 'set'>

# # Определение типа пользовательского класса
# class MyClass:
#     pass

# my_object = MyClass()
# print(type(my_object))    # Вывод: <class '__main__.MyClass'>

# # Проверка типа с помощью isinstance()
# if isinstance(my_integer, int):
#     print("Это целое число.")  # Вывод: Это целое число.

# # Использование type() в условиях
# if type(my_list) == list:
#     print("Это список.")  # Вывод: Это список.

# # Определение типа аргумента в функции
# def check_type(var):
#     return type(var)

# print(check_type(100))       # Вывод: <class 'int'>
# print(check_type("Python"))  # Вывод: <class 'str'>

# # Получение типа через аннотации
# def add(a: int, b: int) -> int:
#     return a + b

# print(type(add))  # Вывод: <class 'function'>

# ↑ type()

# ↓ isinstance()
# Проверка типа переменной
# my_integer = 42
# print(isinstance(my_integer, int))  # Вывод: True

# my_string = "Hello"
# print(isinstance(my_string, str))    # Вывод: True

# my_list = [1, 2, 3]
# print(isinstance(my_list, list))     # Вывод: True

# # Проверка с несколькими типами
# my_value = 3.14
# print(isinstance(my_value, (int, float)))  # Вывод: True

# # Определение пользовательского класса
# class Animal:
#     pass

# class Dog(Animal):
#     pass

# my_dog = Dog()
# print(isinstance(my_dog, Dog))       # Вывод: True
# print(isinstance(my_dog, Animal))    # Вывод: True
# print(isinstance(my_dog, object))    # Вывод: True

# # Проверка с использованием встроенных типов
# my_set = {1, 2, 3}
# print(isinstance(my_set, set))       # Вывод: True
# print(isinstance(my_set, (list, dict)))  # Вывод: False

# # Проверка на None
# my_value = None
# print(isinstance(my_value, type(None)))  # Вывод: True

# # Использование isinstance() в условиях
# def process_value(value):
#     if isinstance(value, list):
#         print("Это список.")
#     elif isinstance(value, dict):
#         print("Это словарь.")
#     else:
#         print("Это другой тип.")

# process_value([1, 2, 3])  # Вывод: Это список.
# process_value({"key": "value"})  # Вывод: Это словарь.

# # Проверка с пользовательскими типами и наследованием
# class Vehicle:
#     pass

# class Car(Vehicle):
#     pass

# my_car = Car()
# print(isinstance(my_car, Car))      # Вывод: True
# print(isinstance(my_car, Vehicle))   # Вывод: True

# ↑ isinstance()
