"""
Этот скрипт демонстрирует различные функции Python, включая преобразование типов, 
базовые операции, работу с файлами, атрибуты функций, обработку исключений, ввод пользователя, 
и работу со списками и словарями.
Преобразование типов:
- x: Преобразует строку в целое число.
- y: Преобразует строку в число с плавающей точкой.
- z: Преобразует целое число в строку.
- my_list: Преобразует кортеж в список.
- my_tuple: Преобразует список в кортеж.
- my_set: Преобразует список в множество, удаляя дубликаты.
- my_dict: Создает словарь.
- is_true: Преобразует 1 в логическое значение True.
Базовые операции:
- length: Получает длину строки.
- data_type: Получает тип переменной.
- is_instance: Проверяет, является ли переменная экземпляром указанного типа.
- absolute: Получает абсолютное значение числа.
- rounded: Округляет число до ближайшего целого.
- minimum: Находит минимальное значение в наборе чисел.
- maximum: Находит максимальное значение в наборе чисел.
- total: Суммирует элементы списка.
- div_result: Выполняет деление и возвращает частное и остаток.
- power: Возводит число в указанную степень.
Итерация и перечисление:
- for loop: Генерирует числа от 0 до 4.
- enumerated: Перечисляет список, связывая каждый элемент с его индексом.
- zipped: Объединяет два списка, связывая элементы из каждого списка.
- mapped: Применяет функцию к каждому элементу списка.
- filtered: Фильтрует элементы списка на основе условия.
Операции со списками:
- sorted_list: Сортирует список.
- reversed_list: Переворачивает список.
- all_true: Проверяет, являются ли все элементы списка True.
- any_true: Проверяет, является ли хотя бы один элемент списка True.
Работа с файлами:
- Запись в файл: Записывает "Hello, World!" в файл с именем 'example.txt'.
- Чтение из файла: Читает содержимое файла 'example.txt'.
Атрибуты функций:
- is_callable: Проверяет, является ли объект вызываемым.
- get_attr: Получает атрибут имени функции.
- set_attr: Устанавливает новый атрибут для функции.
- del_attr: Удаляет атрибут из функции.
- has_attr: Проверяет, имеет ли функция указанный атрибут.
Обработка исключений:
- try-except-finally: Обрабатывает деление на ноль и гарантирует выполнение блока finally.
Ввод пользователя:
- user_input: Запрашивает ввод от пользователя и выводит введенное значение.
- help: Отображает справочную информацию о функции print.
- directory: Перечисляет методы и атрибуты объекта.
- variables: Возвращает словарь локальных переменных.
"""

# !!!!!!!!!!!!!!!!!!!!
# пример использования нескольких переменных

# name, dev, age = 'Ivan', 'Backend', 30
# print(f'Hello, {name} {dev} {age}')

# name, surname = input(), input()
# print('Имя:', name, 'Фамилия:', surname)

# name1 = 'Timur'
# name2 = 'Gvido'

# name1, name2 = name2, name1

# print(name1, name2)
# !!!!!!!!!!!!!!!!!!!!

# Преобразование типов
# x = int("10")      # Преобразует строку в целое число
# y = float("3.14")  # Преобразует строку в число с плавающей точкой
# z = str(100)       # Преобразует число в строку
# my_list = list((1, 2, 3))  # Преобразует кортеж в список
# my_tuple = tuple([1, 2, 3]) # Преобразует список в кортеж
# my_set = set([1, 2, 2, 3])  # Преобразует список в множество
# my_dict = dict(a=1, b=2)    # Создает словарь
# is_true = bool(1)            # Преобразует 1 в True

# print(x, y, z, my_list, my_tuple, my_set, my_dict, is_true)

# length = len("Hello")      # Длина строки
# data_type = type(123)      # Тип переменной
# is_instance = isinstance(123, int)  # Проверка типа

# print(length, data_type, is_instance)

# absolute = abs(-5)         # Модуль числа
# rounded = round(3.6)       # Округление
# minimum = min(1, 2, 3)     # Минимальное значение
# maximum = max(1, 2, 3)     # Максимальное значение
# total = sum([1, 2, 3])     # Сумма элементов
# div_result = divmod(10, 3) # Деление с остатком
# power = pow(2, 3)          # Возведение в степень

# print(absolute, rounded, minimum, maximum, total, div_result, power)

# for i in range(5):         # Генерация чисел от 0 до 4
#     print(i)

# enumerated = list(enumerate(['a', 'b', 'c']))  # [(0, 'a'), (1, 'b'), (2, 'c')]
# zipped = list(zip([1, 2, 3], ['a', 'b', 'c'])) # [(1, 'a'), (2, 'b'), (3, 'c')]
# mapped = list(map(lambda x: x * 2, [1, 2, 3])) # [2, 4, 6]
# filtered = list(filter(lambda x: x > 1, [1, 2, 3])) # [2, 3]

# print(enumerated, zipped, mapped, filtered)

# sorted_list = sorted([3, 1, 2])  # [1, 2, 3]
# reversed_list = list(reversed([1, 2, 3]))  # [3, 2, 1]
# all_true = all([True, True, False])  # False
# any_true = any([False, False, True])  # True

# print(sorted_list, reversed_list, all_true, any_true)

# # Запись в файл
# with open('example.txt', 'w') as f:
#     f.write('Hello, World!')

# # Чтение из файла
# with open('example.txt', 'r') as f:
#     content = f.read()

# print(content)

# def example_func():
#     return "Hello"

# is_callable = callable(example_func)  # True
# get_attr = getattr(example_func, '__name__')  # 'example_func'
# set_attr = setattr(example_func, 'new_attr', 42)  # Добавляет атрибут
# del_attr = delattr(example_func, 'new_attr')  # Удаляет атрибут
# has_attr = hasattr(example_func, '__name__')  # True

# print(is_callable, get_attr, set_attr, del_attr, has_attr)

# # obj_id = id(123)  # Получает уникальный идентификатор объекта
# # del_var = del   # Удаляет переменную

# # print(obj_id, del_var)

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Деление на ноль!")
# finally:
#     print("Этот блок выполнится в любом случае.")

# # raise ZeroDivisionError("Деление на ноль!")

# user_input = input("Введите что-нибудь: ")  # Ввод от пользователя
# print("Вы ввели:", user_input)                # Вывод информации
# help(print)                                   # Вывод справки о функции
# directory = dir([1, 2, 3])                   # Список методов и атрибутов объекта
# variables = vars()                            # Возвращает словарь локальных переменных

# print(user_input, directory, variables)
