
## for i in range(5):         # Генерация чисел от 0 до 4
#     print(i)

## enumerated = list(enumerate(['a', 'b', 'c']))  # [(0, 'a'), (1, 'b'), (2, 'c')]
## zipped = list(zip([1, 2, 3], ['a', 'b', 'c'])) # [(1, 'a'), (2, 'b'), (3, 'c')]
## mapped = list(map(lambda x: x * 2, [1, 2, 3])) # [2, 4, 6]
## filtered = list(filter(lambda x: x > 1, [1, 2, 3])) # [2, 3]

# print(enumerated, zipped, mapped, filtered)

# ↓ for in range()
# Итерация по элементам списка
# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)

# # Итерация по символам строки
# word = "Python"
# for char in word:
#     print(char)

# # Итерация по элементам кортежа
# tuple_numbers = (10, 20, 30)
# for number in tuple_numbers:
#     print(number)

# # Итерация с использованием функции range()
# for i in range(5):
#     print(i)  # Вывод: 0, 1, 2, 3, 4

# # Итерация по ключам словаря
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key in my_dict:
#     print(f"{key}: {my_dict[key]}")

# # Итерация по элементам с индексами
# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits):
#     print(f"Индекс {index}: {fruit}")

# # Вложенные циклы
# for i in range(3):
#     for j in range(2):
#         print(f"i = {i}, j = {j}")

# # Использование break и continue
# for i in range(10):
#     if i == 5:
#         break  # Прерывает цикл, если i равно 5
#     if i % 2 == 0:
#         continue  # Пропускает четные числа
#     print(i)  # Вывод: 1, 3

# # Генерация списка с помощью цикла for
# squared_numbers = [x**2 for x in range(10)]
# print(squared_numbers)  # Вывод: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ↑ for in range()

# ↓ list(enumerate())
# Пример использования enumerate()
# fruits = ['apple', 'banana', 'cherry']
# enumerated_fruits = list(enumerate(fruits))
# print(enumerated_fruits)
# # Вывод: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# # Итерация по элементам с индексами
# for index, fruit in enumerate(fruits):
#     print(f"Индекс {index}: {fruit}")

# # Начало отсчета с 1
# enumerated_fruits_start_1 = list(enumerate(fruits, start=1))
# print(enumerated_fruits_start_1)
# # Вывод: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]

# # Использование с кортежем
# numbers = (10, 20, 30)
# enumerated_numbers = list(enumerate(numbers))
# print(enumerated_numbers)
# # Вывод: [(0, 10), (1, 20), (2, 30)]

# # Генерация списка индексов и значений
# items = ['a', 'b', 'c']
# indexed_items = list(enumerate(items))
# print(indexed_items)  # Вывод: [(0, 'a'), (1, 'b'), (2, 'c')]

# # Применение в условиях
# for index, value in enumerate(fruits):
#     if value == 'banana':
#         print(f"Банан найден на индексе {index}.")

# ↑ list(enumerate())

# ↓ list(zip())
# Пример использования zip() с двумя списками
# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]

# zipped = list(zip(names, ages))
# print(zipped)
# # Вывод: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# # Использование с тремя списками
# cities = ['New York', 'Los Angeles', 'Chicago']
# countries = ['USA', 'USA', 'USA']

# zipped_multiple = list(zip(names, ages, cities, countries))
# print(zipped_multiple)
# # Вывод: [('Alice', 25, 'New York', 'USA'), ('Bob', 30, 'Los Angeles', 'USA'), ('Charlie', 35, 'Chicago', 'USA')]

# # Обработка списков разной длины
# list1 = [1, 2, 3]
# list2 = ['a', 'b']

# zipped_short = list(zip(list1, list2))
# print(zipped_short)
# # Вывод: [(1, 'a'), (2, 'b')]

# # Распаковка данных
# zipped_data = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
# names_unpacked, ages_unpacked = zip(*zipped_data)

# print(names_unpacked)  # Вывод: ('Alice', 'Bob', 'Charlie')
# print(ages_unpacked)   # Вывод: (25, 30, 35)

# # Применение в циклах
# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old.")

# # Использование с итераторами
# iter1 = iter([1, 2, 3])
# iter2 = iter(['x', 'y', 'z'])

# zipped_iter = list(zip(iter1, iter2))
# print(zipped_iter)  # Вывод: [(1, 'x'), (2, 'y'), (3, 'z')]

# ↑ list(zip())

# ↓ list(map())
# Пример использования map() с функцией
# def square(x):
#     return x ** 2

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))
# print(squared_numbers)
# # Вывод: [1, 4, 9, 16, 25]

# # Использование map() с лямбда-функцией
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)
# # Вывод: [1, 4, 9, 16, 25]

# # Применение map() к нескольким итерируемым объектам
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# summed_lists = list(map(lambda x, y: x + y, list1, list2))
# print(summed_lists)
# # Вывод: [5, 7, 9]

# # Применение map() к строкам
# words = ['hello', 'world']
# capitalized_words = list(map(str.upper, words))
# print(capitalized_words)
# # Вывод: ['HELLO', 'WORLD']

# # Преобразование типов с помощью map()
# string_numbers = ['1', '2', '3', '4']
# int_numbers = list(map(int, string_numbers))
# print(int_numbers)
# # Вывод: [1, 2, 3, 4]

# # Обработка списков разной длины
# list1 = [1, 2, 3]
# list2 = [4, 5]

# summed_lists = list(map(lambda x, y: x + y, list1, list2))
# print(summed_lists)
# # Вывод: [5, 7]

# # Применение в циклах
# numbers = [1, 2, 3, 4, 5]
# for squared in map(lambda x: x ** 2, numbers):
#     print(squared)

# ↑ list(map())

# ↓ list(filter())
# Пример использования filter() с функцией
# def is_even(x):
#     return x % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(is_even, numbers))
# print(even_numbers)
# # Вывод: [2, 4, 6]

# # Использование filter() с лямбда-функцией
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)
# # Вывод: [2, 4, 6]

# # Фильтрация строк по длине
# words = ['apple', 'banana', 'pear', 'kiwi']
# long_words = list(filter(lambda word: len(word) > 4, words))
# print(long_words)
# # Вывод: ['apple', 'banana']

# # Удаление None значений из списка
# data = [1, None, 2, None, 3]
# filtered_data = list(filter(None, data))
# print(filtered_data)
# # Вывод: [1, 2, 3]

# # Фильтрация по условию
# numbers = [-2, -1, 0, 1, 2]
# positive_numbers = list(filter(lambda x: x > 0, numbers))
# print(positive_numbers)
# # Вывод: [1, 2]

# # Фильтрация с несколькими условиями
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filtered_numbers = list(filter(lambda x: x % 2 == 0 and x > 5, numbers))
# print(filtered_numbers)
# # Вывод: [6, 8, 10]

# # Применение в циклах
# numbers = [1, 2, 3, 4, 5, 6]
# for even in filter(lambda x: x % 2 == 0, numbers):
#     print(even)

# ↑ list(filter())
