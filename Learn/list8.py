
# # obj_id = id(123)  # Получает уникальный идентификатор объекта
# # del_var = del   # Удаляет переменную

# # print(obj_id, del_var)

# ↓ id()
# a = [1, 2, 3]
# print(id(a))  # Вывод: Уникальный идентификатор для списка a

# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(id(a) == id(b))  # Вывод: True (a и b указывают на один и тот же объект)
# print(id(a) == id(c))  # Вывод: False (a и c - разные объекты, хотя и имеют одинаковое содержимое)

# x = 42
# y = 42

# print(id(x))  # Вывод: Уникальный идентификатор для целого числа x
# print(id(y))  # Вывод: Уникальный идентификатор для целого числа y (может совпадать с id(x) из-за оптимизации)

# # Поскольку небольшие целые числа кэшируются, id(x) и id(y) могут совпадать

# ↑ id

# ↓ del
# x = 10
# print(x)  # Вывод: 10

# del x

# # Попытка доступа к x после удаления вызовет ошибку
# try:
#     print(x)
# except NameError as e:
#     print(e)  # Вывод: name 'x' is not defined

# my_list = [1, 2, 3, 4, 5]
# print(my_list)  # Вывод: [1, 2, 3, 4, 5]

# del my_list[2]  # Удаление элемента с индексом 2

# print(my_list)  # Вывод: [1, 2, 4, 5]

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict)  # Вывод: {'a': 1, 'b': 2, 'c': 3}

# del my_dict['b']  # Удаление ключа 'b'

# print(my_dict)  # Вывод: {'a': 1, 'c': 3}

# a = 1
# b = 2
# c = 3

# # Удаление нескольких переменных
# del a, b

# # Проверка наличия переменных после удаления
# try:
#     print(a)
# except NameError as e:
#     print(e)  # Вывод: name 'a' is not defined

# try:
#     print(b)
# except NameError as e:
#     print(e)  # Вывод: name 'b' is not defined

# print(c)  # Вывод: 3

# ↑ del
