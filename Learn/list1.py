
# x = int("10")      # Преобразует строку в целое число
# y = float("3.14")  # Преобразует строку в число с плавающей точкой
# z = str(100)       # Преобразует число в строку
# my_list = list((1, 2, 3))  # Преобразует кортеж в список
# my_tuple = tuple([1, 2, 3]) # Преобразует список в кортеж
# my_set = set([1, 2, 2, 3])  # Преобразует список в множество
# my_dict = dict(a=1, b=2)    # Создает словарь
# is_true = bool(1)            # Преобразует 1 в True

# print(x, y, z, my_list, my_tuple, my_set, my_dict, is_true)

# ↓ int()
# # Преобразование float в int
# float_num = 3.99
# int_num = int(float_num)
# print(int_num)  # Вывод: 3 (округление вниз)

# # Преобразование строки в целое число с указанием основания
# binary_str = "1010"
# decimal_num = int(binary_str, 2)  # Преобразует двоичное число в десятичное
# print(decimal_num)  # Вывод: 10

# hex_str = "1A"
# decimal_num_from_hex = int(hex_str, 16)  # Преобразует шестнадцатеричное число в десятичное
# print(decimal_num_from_hex)  # Вывод: 26

# # Обработка ошибок при преобразовании
# try:
#     invalid_str = "abc"
#     invalid_num = int(invalid_str)  # Это вызовет ValueError
# except ValueError:
#     print("Doesn't work.")  # Вывод: Не удалось преобразовать строку в целое число.

# # Преобразование пустой строки с проверкой
# empty_str = ""
# if empty_str.strip():  # Проверяем, не является ли строка пустой или состоящей только из пробелов
#     result = int(empty_str)
# else:
#     result = 0  # Или любое другое значение по умолчанию
# print(result)  # Вывод: 0

# # Использование базового значения
# num_with_base = int("5", base=10)  # Десятичное число
# print(num_with_base)  # Вывод: 5

# num_with_base_hex = int("A", base=16)  # Шестнадцатеричное число
# print(num_with_base_hex)  # Вывод: 10
# ↑ int()

# ↓ float()
# Преобразование строки в float
# num_str = "3.14"
# num_float = float(num_str)
# print(num_float)  # Вывод: 3.14

# # Преобразование целого числа в float
# int_num = 5
# float_num = float(int_num)
# print(float_num)  # Вывод: 5.0

# # Преобразование float в float (без изменений)
# original_float = 2.718
# new_float = float(original_float)
# print(new_float)  # Вывод: 2.718

# # Обработка ошибок при преобразовании
# try:
#     invalid_str = "abc"
#     invalid_float = float(invalid_str)  # Это вызовет ValueError
# except ValueError:
#     print("Не удалось преобразовать строку в число с плавающей точкой.")  # Вывод: Не удалось преобразовать строку в число с плавающей точкой.

# # Преобразование пустой строки // если преобразовать пустую строку в float, будет ошибка
# empty_str = "9"
# result = float(empty_str)  # Преобразует в 9.0
# print(result)  # Вывод: 9.0

# # Преобразование строки с пробелами
# space_str = "   42.5   "
# result = float(space_str)  # Игнорирует пробелы
# print(result)  # Вывод: 42.5

# # Преобразование строки в научной нотации
# scientific_str = "1e-3"  # Это 0.001
# result = float(scientific_str)
# print(result)  # Вывод: 0.001
# ↑ float()

# ↓ str()
# Преобразование целого числа в строку
# num = 42
# num_str = str(num)
# print(num_str)  # Вывод: '42'

# # Преобразование float в строку
# float_num = 3.14
# float_str = str(float_num)
# print(float_str)  # Вывод: '3.14'

# # Преобразование булевого значения в строку
# bool_value = True
# bool_str = str(bool_value)
# print(bool_str)  # Вывод: 'True'

# # Преобразование списка в строку
# my_list = [1, 2, 3]
# list_str = str(my_list)
# print(list_str)  # Вывод: '[1, 2, 3]'

# # Преобразование кортежа в строку
# my_tuple = (1, 2, 3)
# tuple_str = str(my_tuple)
# print(tuple_str)  # Вывод: '(1, 2, 3)'

# # Преобразование словаря в строку
# my_dict = {'a': 1, 'b': 2}
# dict_str = str(my_dict)
# print(dict_str)  # Вывод: "{'a': 1, 'b': 2}"

# # Преобразование множества в строку
# my_set = {1, 2, 3}
# set_str = str(my_set)
# print(set_str)  # Вывод: '{1, 2, 3}'

# # Преобразование пользовательского объекта в строку
# class MyClass:
#     def __str__(self):
#         return "Это мой класс"

# obj = MyClass()
# obj_str = str(obj)
# print(obj_str)  # Вывод: 'Это мой класс'

# ↑ str()

# ↓ list()
# Создание списка
# my_list = [1, 2, 3, 4, 5]
# print(my_list)  # Вывод: [1, 2, 3, 4, 5]

# # Доступ к элементам списка
# first_element = my_list[0]  # Индексация начинается с 0
# print(first_element)  # Вывод: 1

# last_element = my_list[-1]  # Отрицательные индексы
# print(last_element)  # Вывод: 5

# # Изменение элемента списка
# my_list[1] = 20
# print(my_list)  # Вывод: [1, 20, 3, 4, 5]

# # Добавление элемента в конец списка
# my_list.append(6)
# print(my_list)  # Вывод: [1, 20, 3, 4, 5, 6]

# # Вставка элемента по индексу
# my_list.insert(1, 15)
# print(my_list)  # Вывод: [1, 15, 20, 3, 4, 5, 6]

# # Удаление элемента по значению
# my_list.remove(20)
# print(my_list)  # Вывод: [1, 15, 3, 4, 5, 6]

# # Удаление элемента по индексу
# del my_list[0]
# print(my_list)  # Вывод: [15, 3, 4, 5, 6]

# # Слияние списков
# another_list = [7, 8, 9]
# combined_list = my_list + another_list
# print(combined_list)  # Вывод: [15, 3, 4, 5, 6, 7, 8, 9]

# # Перебор элементов списка
# for item in my_list:
#     print(item)
# # Вывод:
# # 1
# # 2
# # 5
# # 5
# # 6
# # 9

# # Создание двумерного списка
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[1][1])  # Вывод: 5 (второй ряд, второй элемент)

# # Список с различными типами данных
# mixed_list = [1, "two", 3.0, True]
# print(mixed_list)  # Вывод: [1, 'two', 3.0, True]

# ↑ list()

# ↓ tuple()
# # Создание кортежа
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)  # Вывод: (1, 2, 3, 4, 5)

# # Доступ к элементам кортежа
# first_element = my_tuple[0]
# print(first_element)  # Вывод: 1

# last_element = my_tuple[-1]
# print(last_element)  # Вывод: 5

# # Попытка изменить элемент кортежа вызовет ошибку
# try:
#     my_tuple[1] = 20  # Это вызовет TypeError
# except TypeError as e:
#     print(e)  # Вывод: 'tuple' object does not support item assignment

# # Создание кортежа с одним элементом
# single_element_tuple = (42,)
# print(single_element_tuple)  # Вывод: (42,)

# # Объединение кортежей
# another_tuple = (6, 7, 8)
# combined_tuple = my_tuple + another_tuple
# print(combined_tuple)  # Вывод: (1, 2, 3, 4, 5, 6, 7, 8)

# # Перебор элементов кортежа
# for item in my_tuple:
#     print(item)
# # Вывод:
# # 1
# # 2
# # 3
# # 4
# # 5

# # Использование кортежей для хранения нескольких значений
# coordinates = (10.0, 20.0)
# print(f"X: {coordinates[0]}, Y: {coordinates[1]}")  # Вывод: X: 10.0, Y: 20.0

# # Кортежи можно использовать как ключи в словарях
# my_dict = {}
# my_dict[(1, 2)] = "point A"
# my_dict[(3, 4)] = "point B"
# print(my_dict)  # Вывод: {(1, 2): 'point A', (3, 4): 'point B'}

# # Распаковка кортежей
# a, b, c = (1, 2, 3)
# print(a)  # Вывод: 1
# print(b)  # Вывод: 2
# print(c)  # Вывод: 3

# # Кортежи с различными типами данных
# mixed_tuple = (1, "two", 3.0, True)
# print(mixed_tuple)  # Вывод: (1, 'two', 3.0, True)

# ↑ tuple()

# ↓ set()
# Создание множества
# my_set = {1, 2, 3, 4, 5}
# print(my_set)  # Вывод: {1, 2, 3, 4, 5}

# # Создание множества из списка (удаление дубликатов)
# my_list = [1, 2, 2, 3, 4]
# my_set_from_list = set(my_list)
# print(my_set_from_list)  # Вывод: {1, 2, 3, 4}

# # Добавление элемента в множество
# my_set.add(6)
# print(my_set)  # Вывод: {1, 2, 3, 4, 5, 6}

# # Удаление элемента из множества
# my_set.remove(3)  # Если элемента нет, вызовет KeyError
# print(my_set)  # Вывод: {1, 2, 4, 5, 6}

# # Удаление элемента с безопасной проверкой
# my_set.discard(10)  # Не вызовет ошибку, если элемента нет
# print(my_set)  # Вывод: {1, 2, 4, 5, 6}

# # Удаление элемента из множества
# my_set.remove(3)  # Если элемента нет, вызовет KeyError
# print(my_set)  # Вывод: {1, 2, 4, 5, 6}

# # Удаление элемента с безопасной проверкой
# my_set.discard(10)  # Не вызовет ошибку, если элемента нет
# print(my_set)  # Вывод: {1, 2, 4, 5, 6}

# # Проверка, есть ли элемент в множестве
# if 2 in my_set:
#     print("2 присутствует в множестве.")  # Вывод: 2 присутствует в множестве.

# # Создание других множеств
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}

# # Объединение множеств
# union_set = set_a | set_b
# print(union_set)  # Вывод: {1, 2, 3, 4, 5}

# # Пересечение множеств
# intersection_set = set_a & set_b
# print(intersection_set)  # Вывод: {3}

# # Разность множеств
# difference_set = set_a - set_b
# print(difference_set)  # Вывод: {1, 2}

# # Симметрическая разность
# symmetric_difference_set = set_a ^ set_b
# print(symmetric_difference_set)  # Вывод: {1, 2, 4, 5}

# # Перебор элементов множества
# for item in my_set:
#     print(item)
# # Вывод (порядок может варьироваться):
# # 1
# # 2
# # 4
# # 5
# # 6

# # Множества с различными типами данных
# mixed_set = {1, "two", 3.0, True}
# print(mixed_set)  # Вывод: {1, 'two', 3.0}

# # Создание пустого множества
# empty_set = set()
# print(empty_set)  # Вывод: set()

# # Множества нельзя использовать как ключи в словарях, так как они изменяемы
# try:
#     my_dict = {}
#     my_dict[{1, 2}] = "value"  # Это вызовет TypeError
# except TypeError as e:
#     print(e)  # Вывод: unhashable type: 'set'

# ↑ set()

# ↓ dict()
# Создание словаря
# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# print(my_dict)  # Вывод: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# # Доступ к элементам словаря по ключу
# name = my_dict["name"]
# print(name)  # Вывод: Alice

# age = my_dict.get("age")
# print(age)  # Вывод: 30

# # Изменение значения по ключу
# my_dict["age"] = 31
# print(my_dict)  # Вывод: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# # Добавление нового элемента в словарь
# my_dict["email"] = "alice@example.com"
# print(my_dict)  # Вывод: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}

# # Удаление элемента по ключу
# del my_dict["city"]
# print(my_dict)  # Вывод: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

# # Удаление элемента с безопасной проверкой
# value = my_dict.pop("age", "Not Found")
# print(value)  # Вывод: 31
# print(my_dict)  # Вывод: {'name': 'Alice'}

# # Проверка, есть ли ключ в словаре
# if "name" in my_dict:
#     print("Ключ 'name' присутствует в словаре.")  # Вывод: Ключ 'name' присутствует в словаре.

# # Словари с различными типами данных
# mixed_dict = {
#     1: "one",
#     "two": 2,
#     (3, 4): [3, 4]
# }
# print(mixed_dict)  # Вывод: {1: 'one', 'two': 2, (3, 4): [3, 4]}

# # Создание пустого словаря
# empty_dict = {}
# print(empty_dict)  # Вывод: {}

# # Создание пустого словаря
# empty_dict = {}
# print(empty_dict)  # Вывод: {}

# # Создание словаря из списка
# dev_dict = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "error": None,
#     "dev_info": {
#         "role": "Frontend",
#         "skills": ["HTML", "CSS", "JavaScript"],
#         "last_year": 2023,
#         "current_year": 2025
#     }
# }

# city = "city"

# dev_dict["name"] = "Alice"

# dev_dict["age"] = 31

# dev_dict["dev"] = "Backend"

# del dev_dict["error"]

# dev_dict[city] = "Kayakent"

# print(dev_dict["dev_info"]["skills"])

# print(dev_dict.get('model'))
# print(dev_dict.get('script', 'Not found'))

# dev_dict['model'] = "Mercedes"
# dev_dict['script'] = "Python"
# dev_dict['Not found'] = 404

# print(dev_dict)

# ↑ dict()

# ↓ bool()
# Создание логических переменных
# is_true = True
# is_false = False

# print(is_true)   # Вывод: True
# print(is_false)  # Вывод: False

# # Логические операции
# a = True
# b = False

# # И (and)
# print(a and b)  # Вывод: False

# # Или (or)
# print(a or b)   # Вывод: True

# # Не (not)
# print(not a)    # Вывод: False

# # Преобразование в логический тип
# print(bool(0))        # Вывод: False
# print(bool(1))        # Вывод: True
# print(bool(""))       # Вывод: False
# print(bool("Hello"))  # Вывод: True
# print(bool([]))       # Вывод: False
# print(bool([1, 2]))   # Вывод: True

# # Использование в условных операторах
# if is_true:
#     print("Это истинно!")  # Вывод: Это истинно!
# else:
#     print("Это ложно.")

# # Логические выражения
# x = 10
# y = 20

# # Проверка условий
# result = (x < y) and (y > 15)
# print(result)  # Вывод: True

# # Использование логического типа в списковых включениях
# numbers = [1, 2, 3, 4, 5]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)  # Вывод: [2, 4]

# # Функция, возвращающая логическое значение
# def is_even(n):
#     return n % 2 == 0

# print(is_even(4))  # Вывод: True
# print(is_even(5))  # Вывод: False

# # Логические значения в словарях
# status_dict = {
#     "is_active": True,
#     "is_deleted": False
# }
# print(status_dict)  # Вывод: {'is_active': True, 'is_deleted': False}

# # Использование логических значений в циклах
# count = 0
# while count < 5:
#     print(count)
#     count += 1  # Цикл продолжается, пока count < 5

# # Логические значения в списках
# bool_list = [True, False, True, False]
# print(bool_list)  # Вывод: [True, False, True, False]

# ↑ bool()
