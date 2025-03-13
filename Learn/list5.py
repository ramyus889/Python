
## sorted_list = sorted([3, 1, 2])  # [1, 2, 3]
## reversed_list = list(reversed([1, 2, 3]))  # [3, 2, 1]
## all_true = all([True, True, False])  # False
## any_true = any([False, False, True])  # True

# print(sorted_list, reversed_list, all_true, any_true)

# ↓ sorted()
# Простой пример сортировки списка
# numbers = [5, 2, 9, 1, 5, 6]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# # Вывод: [1, 2, 5, 5, 6, 9]

# # Сортировка в обратном порядке
# sorted_numbers_desc = sorted(numbers, reverse=True)
# print(sorted_numbers_desc)
# # Вывод: [9, 6, 5, 5, 2, 1]

# # Сортировка строк
# words = ['banana', 'apple', 'cherry']
# sorted_words = sorted(words)
# print(sorted_words)
# # Вывод: ['apple', 'banana', 'cherry']

# # Сортировка по длине строки
# words = ['banana', 'apple', 'cherry', 'kiwi']
# sorted_by_length = sorted(words, key=len)
# print(sorted_by_length)
# # Вывод: ['kiwi', 'apple', 'banana', 'cherry']

# # Сортировка списка кортежей
# data = [(1, 'one'), (3, 'three'), (2, 'two')]
# sorted_data = sorted(data)
# print(sorted_data)
# # Вывод: [(1, 'one'), (2, 'two'), (3, 'three')]

# # Сортировка по нескольким критериям
# data = [('apple', 2), ('banana', 1), ('cherry', 3), ('banana', 2)]
# sorted_data = sorted(data, key=lambda x: (x[0], x[1]))
# print(sorted_data)
# # Вывод: [('apple', 2), ('banana', 1), ('banana', 2), ('cherry', 3)]

# # Сортировка списка на месте
# numbers = [5, 2, 9, 1, 5, 6]
# numbers.sort()
# print(numbers)
# # Вывод: [1, 2, 5, 5, 6, 9]

# # Сортировка строк с учетом регистра
# words = ['banana', 'Apple', 'cherry']
# sorted_case_sensitive = sorted(words)
# print(sorted_case_sensitive)
# # Вывод: ['Apple', 'banana', 'cherry']

# ↑ sorted()

# ↓ list(reversed())
# # Пример использования reversed() с списком
# numbers = [1, 2, 3, 4, 5]
# reversed_numbers = list(reversed(numbers))
# print(reversed_numbers)
# # Вывод: [5, 4, 3, 2, 1]

# # Применение reversed() к строке
# word = "hello"
# reversed_word = ''.join(reversed(word))
# print(reversed_word)
# # Вывод: 'olleh'

# # Применение reversed() к кортеже
# tuple_data = (1, 2, 3, 4, 5)
# reversed_tuple = list(reversed(tuple_data))
# print(reversed_tuple)
# # Вывод: [5, 4, 3, 2, 1]

# # Применение reversed() к списку строк
# words = ['apple', 'banana', 'cherry']
# reversed_words = list(reversed(words))
# print(reversed_words)
# # Вывод: ['cherry', 'banana', 'apple']

# # Использование reversed() в цикле
# numbers = [1, 2, 3, 4, 5]
# for num in reversed(numbers):
#     print(num)
# # Вывод: 5, 4, 3, 2, 1 (каждое число на новой строке)

# # Применение reversed() к списку и преобразование в список
# data = [10, 20, 30, 40, 50]
# reversed_data = list(reversed(data))
# print(reversed_data)
# # Вывод: [50, 40, 30, 20, 10]

# ↑ list(reversed())

# ↓ all()
# Пример использования all() с списком
# numbers = [1, 2, 3, 4, 5]
# result = all(numbers)
# print(result)
# # Вывод: True (все элементы истинные)

# # Пример с ложными значениями
# numbers = [1, 2, 0, 4, 5]
# result = all(numbers)
# print(result)
# # Вывод: False (ноль является ложным значением)

# # Пустой итерируемый объект
# empty_list = []
# result = all(empty_list)
# print(result)
# # Вывод: True (пустой объект считается истинным)

# # Использование all() с условием
# numbers = [2, 4, 6, 8]
# result = all(x % 2 == 0 for x in numbers)
# print(result)
# # Вывод: True (все элементы четные)

# # Пример с различными типами данных
# data = [1, 2, 'hello', True]
# result = all(data)
# print(result)
# # Вывод: True (все элементы истинные)

# # Использование all() с логическим выражением
# conditions = [True, True, False]
# result = all(conditions)
# print(result)
# # Вывод: False (один элемент ложный)

# # Проверка на наличие символов в строке
# string = "Hello"
# result = all(char.isalpha() for char in string)
# print(result)
# # Вывод: True (все символы являются буквами)

# ↑ all()

# ↓ any()
# Пример использования any() с списком
# numbers = [0, 0, 0, 1]
# result = any(numbers)
# print(result)
# # Вывод: True (один элемент истинный)

# # Пример с ложными значениями
# numbers = [0, False, None]
# result = any(numbers)
# print(result)
# # Вывод: False (все элементы ложные)

# # Пустой итерируемый объект
# empty_list = []
# result = any(empty_list)
# print(result)
# # Вывод: False (пустой объект считается ложным)

# # Использование any() с условием
# numbers = [1, 2, 3, 4]
# result = any(x > 3 for x in numbers)
# print(result)
# # Вывод: True (один элемент больше 3)

# # Пример с различными типами данных
# data = [0, '', None, True]
# result = any(data)
# print(result)
# # Вывод: True (True является истинным значением)

# # Использование any() с логическим выражением
# conditions = [False, False, True]
# result = any(conditions)
# print(result)
# # Вывод: True (один элемент истинный)

# # Проверка на наличие символов в строке
# string = "Hello"
# result = any(char.isdigit() for char in string)
# print(result)
# # Вывод: False (нет цифр в строке)

# ↑ any()
