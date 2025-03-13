
## absolute = abs(-5)         # Модуль числа
## rounded = round(3.6)       # Округление
## minimum = min(1, 2, 3)     # Минимальное значение
## maximum = max(1, 2, 3)     # Максимальное значение
## total = sum([1, 2, 3])     # Сумма элементов
## div_result = divmod(10, 3) # Деление с остатком
## power = pow(2, 3)          # Возведение в степень

# print(absolute, rounded, minimum, maximum, total, div_result, power)

# ↓ abs()
# Абсолютное значение целого числа
# negative_integer = -10
# absolute_value = abs(negative_integer)
# print(absolute_value)  # Вывод: 10

# # Абсолютное значение вещественного числа
# negative_float = -3.14
# absolute_value_float = abs(negative_float)
# print(absolute_value_float)  # Вывод: 3.14

# # Абсолютное значение комплексного числа
# complex_number = 3 + 4j
# absolute_value_complex = abs(complex_number)
# print(absolute_value_complex)  # Вывод: 5.0 (модуль комплексного числа)

# # Использование abs() в математических расчетах
# def distance(x1, y1, x2, y2):
#     return abs(x2 - x1) + abs(y2 - y1)

# print(distance(1, 2, 4, 6))  # Вывод: 7

# # Применение abs() в условиях
# value = -20
# if abs(value) > 10:
#     print("Абсолютное значение больше 10.")  # Вывод: Абсолютное значение больше 10.

# # Использование abs() с коллекциями
# numbers = [-1, -2, -3, 4, 5]
# absolute_values = [abs(num) for num in numbers]
# print(absolute_values)  # Вывод: [1, 2, 3, 4, 5]

# ↑ abs()

# ↓ round()
# Округление до ближайшего целого числа
# number = 3.6
# rounded_number = round(number)
# print(rounded_number)  # Вывод: 4

# # Округление с заданным количеством десятичных знаков
# number = 3.14159
# rounded_number = round(number, 2)
# print(rounded_number)  # Вывод: 3.14

# # Округление отрицательных чисел
# negative_number = -2.5
# rounded_negative = round(negative_number)
# print(rounded_negative)  # Вывод: -2

# # Округление до целого числа с использованием отрицательного аргумента
# number = 1234.5678
# rounded_number = round(number, -2)
# print(rounded_number)  # Вывод: 1200.0

# # Округление в списках
# numbers = [1.234, 2.345, 3.456, 4.567]
# rounded_numbers = [round(num, 2) for num in numbers]
# print(rounded_numbers)  # Вывод: [1.23, 2.35, 3.46, 4.57]

# # Округление с использованием встроенной функции
# def format_price(price):
#     return round(price, 2)

# print(format_price(19.995))  # Вывод: 20.0

# # Округление в условиях
# value = 2.675
# rounded_value = round(value, 2)
# if rounded_value == 2.67:
#     print("Округлено до 2.67.")  # Вывод: Округлено до 2.67.

# ↑ round()

# ↓ min()
# Нахождение минимального значения среди нескольких чисел
# min_value = min(3, 1, 4, 2)
# print(min_value)  # Вывод: 1

# # Нахождение минимального значения в списке
# numbers = [10, 20, 5, 15]
# min_in_list = min(numbers)
# print(min_in_list)  # Вывод: 5

# # Нахождение минимального значения в кортеже
# tuple_numbers = (8, 3, 7, 1)
# min_in_tuple = min(tuple_numbers)
# print(min_in_tuple)  # Вывод: 1

# # Нахождение минимального значения в строках
# words = ["apple", "banana", "cherry"]
# min_word = min(words)
# print(min_word)  # Вывод: apple (по алфавиту)

# # Нахождение минимального значения с использованием ключа
# people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
# youngest = min(people, key=lambda x: x["age"])
# print(youngest)  # Вывод: {'name': 'Bob', 'age': 25}

# # Нахождение минимального значения в многомерных структурах
# matrix = [[3, 2, 1], [6, 5, 4]]
# min_in_matrix = min(min(row) for row in matrix)
# print(min_in_matrix)  # Вывод: 1

# # Использование min() в условиях
# a = 10
# b = 20
# minimum = min(a, b)
# if minimum == a:
#     print("a — минимальное значение.")  # Вывод: a — минимальное значение.

# ↑ min()

# ↓ max()
# Нахождение максимального значения среди нескольких чисел
# max_value = max(3, 1, 4, 2)
# print(max_value)  # Вывод: 4

# # Нахождение максимального значения в списке
# numbers = [10, 20, 5, 15]
# max_in_list = max(numbers)
# print(max_in_list)  # Вывод: 20

# # Нахождение максимального значения в кортеже
# tuple_numbers = (8, 3, 7, 1)
# max_in_tuple = max(tuple_numbers)
# print(max_in_tuple)  # Вывод: 8

# # Нахождение максимального значения в строках
# words = ["apple", "banana", "cherry"]
# max_word = max(words)
# print(max_word)  # Вывод: cherry (по алфавиту)

# # Нахождение максимального значения с использованием ключа
# people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
# oldest = max(people, key=lambda x: x["age"])
# print(oldest)  # Вывод: {'name': 'Charlie', 'age': 35}

# # Нахождение максимального значения в многомерных структурах
# matrix = [[3, 2, 1], [6, 5, 4]]
# max_in_matrix = max(max(row) for row in matrix)
# print(max_in_matrix)  # Вывод: 6

# # Использование max() в условиях
# a = 10
# b = 20
# maximum = max(a, b)
# if maximum == b:
#     print("b — максимальное значение.")  # Вывод: b — максимальное значение.

# ↑ max()

# ↓ sum()
# Сумма элементов списка
# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# print(total)  # Вывод: 15

# # Сумма элементов кортежа
# tuple_numbers = (10, 20, 30)
# total_tuple = sum(tuple_numbers)
# print(total_tuple)  # Вывод: 60

# # Сумма с начальным значением
# numbers = [1, 2, 3]
# total_with_start = sum(numbers, 10)
# print(total_with_start)  # Вывод: 16 (1 + 2 + 3 + 10)

# # Сумма элементов в многомерной структуре
# matrix = [[1, 2, 3], [4, 5, 6]]
# total_matrix = sum(sum(row) for row in matrix)
# print(total_matrix)  # Вывод: 21

# # Сумма с использованием генератора
# total_gen = sum(x for x in range(1, 11))  # Сумма чисел от 1 до 10
# print(total_gen)  # Вывод: 55

# # Сумма с фильтрацией
# numbers = [1, 2, 3, 4, 5]
# even_sum = sum(x for x in numbers if x % 2 == 0)
# print(even_sum)  # Вывод: 6 (2 + 4)

# # Использование sum() в условиях
# values = [10, 20, 30]
# if sum(values) > 50:
#     print("Сумма больше 50.")  # Вывод: Сумма больше 50.

# ↑ sum()

# ↓ divmod()
# Простой пример использования divmod()
# result = divmod(10, 3)
# print(result)  # Вывод: (3, 1)
# # 10 // 3 = 3 (частное), 10 % 3 = 1 (остаток)

# # Деление с отрицательными числами
# result_negative = divmod(-10, 3)
# print(result_negative)  # Вывод: (-4, 2)
# # -10 // 3 = -4, -10 % 3 = 2

# # Использование с дробными числами
# result_float = divmod(7.5, 2.5)
# print(result_float)  # Вывод: (3.0, 0.0)
# # 7.5 // 2.5 = 3.0, 7.5 % 2.5 = 0.0

# # Применение в циклах
# for i in range(10):
#     quotient, remainder = divmod(i, 3)
#     print(f"{i} divmod 3 = {quotient}, остаток = {remainder}")

# # Применение в условиях
# a, b = 25, 4
# quotient, remainder = divmod(a, b)
# if remainder == 0:
#     print(f"{a} делится на {b} без остатка.")  # Вывод: 25 делится на 4 без остатка.
# else:
#     print(f"{a} не делится на {b} без остатка.")

# # Использование с большими числами
# large_result = divmod(123456789, 10000)
# print(large_result)  # Вывод: (12345, 6789)

# ↑ divmod()

# ↓ pow()
# Простое возведение в степень
# result = pow(2, 3)
# print(result)  # Вывод: 8 (2 ** 3)

# # Возведение в степень с отрицательным экспонентом
# result_negative_exp = pow(2, -2)
# print(result_negative_exp)  # Вывод: 0.25 (2 ** -2)

# # Использование с тремя аргументами
# result_mod = pow(2, 3, 3)
# print(result_mod)  # Вывод: 2 ((2 ** 3) % 3)

# # Возведение в степень больших чисел
# large_power = pow(10, 6)
# print(large_power)  # Вывод: 1000000 (10 ** 6)

# # Вычисление остатка от большой степени
# large_power_mod = pow(2, 1000, 1000)
# print(large_power_mod)  # Вывод: 24

# # Использование с дробными числами
# result_float = pow(4.0, 0.5)
# print(result_float)  # Вывод: 2.0 (квадратный корень из 4)

# # Применение в циклах
# for i in range(5):
#     print(f"2 в степени {i} = {pow(2, i)}")

# ↑ pow()
