"""
# ! Netology Python Basic
Списки:
- strings: Список строк.
- numbers: Список целых чисел.
- data: Список, содержащий смешанные типы данных.
- summa: Конкатенирует два списка.
- first, second: Доступ к элементам списка по индексу.
- strings_length: Получает длину списка.
- s: Суммирует элементы списка.
Словари:
- dictionary: Словарь с ключами 'name', 'age' и 'city'.
- name: Доступ к значению, связанному с ключом 'name'.
- countries: Словарь с названиями стран в качестве ключей и списками городов в качестве значений.
- dagestan: Доступ к списку городов в Дагестане.
- dagestan_key: Переменная, содержащая ключ 'Dagestan'.
- countries["Dagestan"].append: Добавляет город в список городов в Дагестане.
- countries["Jamaica"]: Добавляет новую пару ключ-значение в словарь.
- countries[0]: Добавляет новую пару ключ-значение с целочисленным ключом.
- len(countries["Dagestan"]): Получает количество городов в Дагестане.
Ввод пользователя:
- name: Запрашивает имя пользователя.
- age: Запрашивает возраст пользователя и преобразует в целое число.
Логические операторы:
- name: Запрашивает имя пользователя.
- name1: Строка с именем "Frontend".
- name == name1: Сравнивает введенное имя с "Frontend".
Условные операторы:
- name: Запрашивает имя пользователя.
- login: Строка с именем "Dev".
- if-elif-else: Проверяет введенное имя и выводит соответствующее сообщение.
- len(name): Получает длину введенного имени.
- name == login: Сравнивает введенное имя с "Dev".
- name == "Admin": Сравнивает введенное имя с "Admin".
- else: Выводит сообщение о неверном имени.
Команды и задачи:
- HELP: Отображает справочную информацию о программе.
- add: Добавляет задачу в список.
- show: Выводит список задач.
- command: Запрашивает команду.
- task: Запрашивает задачу.
- tasks: Список задач.
- tasks.append(task): Добавляет задачу в список.
- print(tasks): Выводит список задач.
- print("Задача добавлена"): Выводит сообщение о добавлении задачи.
- command == "help": Проверяет, является ли команда "help".
- command == "show": Проверяет, является ли команда "show".
- command == "add": Проверяет, является ли команда "add".
- else: Выводит сообщение о неверной команде.
Цикл while:
- HELP: Отображает справочную информацию о программе.
- add: Добавляет задачу в список.
- show: Выводит список задач.
- command: Запрашивает команду.
- task: Запрашивает задачу.
- tasks: Список задач.
- tasks.append(task): Добавляет задачу в список.
- print(tasks): Выводит список задач.
- print("Задача добавлена"): Выводит сообщение о добавлении задачи.
- command == "help": Проверяет, является ли команда "help".
- command == "show": Проверяет, является ли команда "show".
- command == "add": Проверяет, является ли команда "add".
- command == "exit": Проверяет, является ли команда "exit".
- else: Выводит сообщение о неверной команде.
Цикл while с date:
- HELP: Отображает справочную информацию о программе.
- add: Добавляет задачу в список.
- show: Выводит список задач.
- command: Запрашивает команду.
- task: Запрашивает задачу.
- tasks: Список задач.
- tasks.append(task): Добавляет задачу в список.
- print(tasks): Выводит список задач.
- print("Задача добавлена"): Выводит сообщение о добавлении задачи.
- command == "help": Проверяет, является ли команда "help".
- command == "show": Проверяет, является ли команда "show".
- command == "add": Проверяет, является ли команда "add".
- command == "exit": Проверяет, является ли команда "exit".
- date: Запрашивает дату.
- task: Запрашивает задачу.
- tasks: Список задач.
Цикл while с command random:
- HELP: Отображает справочную информацию о программе.
- add: Добавляет задачу в список.
- show: Выводит список задач.
- command: Запрашивает команду.
- task: Запрашивает задачу.
- tasks: Список задач.
- tasks.append(task): Добавляет задачу в список.
- print(tasks): Выводит список задач.
- print("Задача добавлена"): Выводит сообщение о добавлении задачи.
- command == "help": Проверяет, является ли команда "help".
- command == "show": Проверяет, является ли команда "show".
- command == "add": Проверяет, является ли команда "add".
- command == "exit": Проверяет, является ли команда "exit".
- command == "random": Проверяет, является ли команда "random".
- random_task: Случайная задача.
- tasks: Список задач.
Функциия def:
- multiply: Принимает два аргумента a и b и возвращает результат умножения.
- a: Первый аргумент.
- b: Второй аргумент.
- result: Результат умножения.
- return result: Возвращает результат умножения.
- c: Результат умножения.
- multiply(2, 3): Вызов функции multiply с аргументами 2 и 3.
- multiply(10, 9): Вызов функции multiply с аргументами 10 и 9.
- multiply(4, 5): Вызов функции multiply с аргументами 4 и 5.
- print_dev: Функция print_dev не принимает аргументов.
- print_dev(): Вызов функции print_dev дважды.
- dev_input(prompt): Функция dev_input принимает один аргумент prompt.
Функция def с command random:
- random_task: Случайная задача.
- print(random_task): Выводит случайную задачу.
- command == "help": Проверяет, является ли команда "help".
- command == "show": Проверяет, является ли команда "show".
- command == "add": Проверяет, является ли команда "add".
- command == "exit": Проверяет, является ли команда "exit".
- command == "random": Проверяет, является ли команда "random".
- date: Запрашивает дату.
- task: Запрашивает задачу.
- tasks: Список задач.
- tasks.append(task): Добавляет задачу в список.
- print(tasks): Выводит список задач.
- print("Задача добавлена"): Выводит сообщение о добавлении задачи.
"""

# -------------------------------------------------------------------------------------------
# ! Netology Python Basic

# → Списки

# strings = ["Frontend", "Developer"]
# numbers = [1, 2, 3, 4, 5]
# data = ["Dev", 1]

# print(strings)
# print(numbers)
# print(data)

# summa = numbers + data
# print(summa)

# numbers.append(6)
# print(numbers)

# first = strings[0]
# second = strings[1]
# print(first)
# print(second)

# strings_length = len(strings)
# print(strings_length)

# s = sum(numbers)
# print(s)

# ------------------------------ 

# → Словари

# dictionary = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# print(dictionary)
# name = dictionary["name"]
# print(name)

# countries = {
#     "Dagestan": ["Makhachkala", "Kaspiysk", "Derbent", "Kayakent"],
#     "Chechnya": ["Grozny", "Argun", "Gudermes", "Urus-Martan"],
#     "Ingushetia": ["Nazran", "Karabulak", "Magas", "Sleptsovsk"]
# }

# dagestan = countries["Dagestan"]
# print(dagestan[3])

# dagestan_key = "Dagestan"
# print(countries[dagestan_key])
# print(countries[dagestan_key][2])

# countries["Dagestan"].append("Khasavyurt")
# print(countries)

# countries["Jamaica"] = ["Kingston", "Montego Bay", "Spanish Town", "Portmore"]
# print(countries)

# print(countries["Jamaica"])

# countries[0] = "Moscow"
# print(countries)

# print(len(countries["Dagestan"]))

# ------------------------------ 

# →  Ввод пользователя

# name = input ("Введите ваше имя: ")
# print(name)

# age = input ("Введите ваш возраст: ")
# age = int(age)  # Преобразование строки в целое число
# print("Вам " + str(age) + " лет..")

# ------------------------------ 

# →  Логические операторы

# name = input("Name: ")
# print(name)

# name1 = "Frontend"
# print(name == name1) 

# ------------------------------ 

# → Условные операторы

# name = input("Enter your name: ")
# login = "Dev"

# if name == login:
#     print("Hello", name)
# elif len(name) < 3:
#     print("Name is too short")
# elif name == "Admin":
#     print("Hello Admin")
# else:
#     print("You are not Dev")

# ------------------------------ 

# → Команды и задачи списком

# HELP = """
# help - напечатать справку по программе
# add - добавить задачу в список (название задачи запрашивается у пользователя)
# show - напечатать все добавленные задачи
# """

# tasks = []

# command = input("Введите команду: ")
# if command == "help":
#     print(HELP)
# elif command == "show":
#     print(tasks)
# elif command == "add":
#     task = input("Введите задачу: ")
#     tasks.append(task)
#     print("Задача добавлена")
# else:
#     print("Неизвестная команда")
    
# ------------------------------ 

# → Цикл while

# HELP = """
# help - напечатать справку по программе
# add - добавить задачу в список (название задачи запрашивается у пользователя)
# show - напечатать все добавленные задачи
# """

# tasks = []

# run = True
# while run:
#     command = input("Введите команду: ")
#     if command == "help":
#         print(HELP)
#     elif command == "show":
#         print(tasks)
#     elif command == "add":
#         task = input("Введите задачу: ")
#         tasks.append(task)
#         print("Задача добавлена")
#     elif command == "exit":
#         run = False
#     else:
#         print("Неизвестная команда")

# ------------------------------ 

# → Цикл while с date

# HELP = """
# help - напечатать справку по программе
# add - добавить задачу в список (название задачи запрашивается у пользователя)
# show - напечатать все добавленные задачи
# """

# tasks = {}

# run = True

# while run:
#     command = input("Введите команду: ")
#     if command == "help":
#         print(HELP)
#     elif command == "show":
#         date = input("Введите дату для просмотра списка задач: ")
#         if date in tasks:
#           for task in tasks[date]:
#             print('-', task)
#         else:
#           print("Задач на дату", date, "отсутствуют")
#     elif command == "add":
#         date = input("Введите дату: ")
#         task = input("Введите задачу: ")
#         if date in tasks:
#           tasks[date].append(task)
#         else:
#           tasks[date] = []
#           tasks[date].append(task)
#         print("Задача", task, "для даты", date, "успешно добавлена")
#     elif command == "exit":
#         run = False
#         print("Спасибо за использование! До свидания!")
#     else:
#         print("Неизвестная команда")

# ------------------------------ 

# → Цикл while с command random

# HELP = """
# help - напечатать справку по программе
# add - добавить задачу в список (название задачи запрашивается у пользователя)
# show - напечатать все добавленные задачи
# random - добавить случайную задачу в список
# """

# RANDOM_TASKS = "Записаться на курсы по Python"

# tasks = {}

# run = True

# while run:
#     command = input("Введите команду: ")
#     if command == "help":
#         print(HELP)
#     elif command == "show":
#         date = input("Введите дату для просмотра списка задач: ")
#         if date in tasks:
#           for task in tasks[date]:
#             print('-', task)
#         else:
#           print("Задач на дату", date, "отсутствуют")
#     elif command == "add":
#         date = input("Введите дату: ")
#         task = input("Введите задачу: ")
#         if date in tasks:
#           tasks[date].append(task)
#         else:
#           tasks[date] = []
#           tasks[date].append(task)
#         print("Задача", task, "для даты", date, "успешно добавлена")
#     elif command == "random":
#         if "Сегодня" in tasks:
#           tasks["Сегодня"].append(RANDOM_TASKS)
#         else:
#           tasks["Сегодня"] = []
#           tasks["Сегодня"].append(RANDOM_TASKS)
#     elif command == "exit":
#         run = False
#         print("Спасибо за использование! До свидания!")
#     else:
#         print("Неизвестная команда")

# ------------------------------ 

# → Функция def

# def multiply(a, b):
#     print("a =", a)  
#     print("b =", b) 
#     result = a * b  
#     return result  


# c = multiply(2, 3)
# print(c) 

# c = multiply(10, 9)
# print(c) 

# c = multiply(4, 5)
# print(c)  

# def print_dev():
#     print("Frontend")  
#     print("Backend") 

# Вызов функции print_dev дважды
# print_dev()
# print_dev()

# def dev_input(prompt):
#     print(prompt)  
#     inp = ...  
#     return inp  

# ------------------------------ 

# → Функция def с command random

# HELP = """
# help - напечатать справку по программе
# add - добавить задачу в список (название задачи запрашивается у пользователя)
# show - напечатать все добавленные задачи
# random - добавить случайную задачу в список
# """

# RANDOM_TASKS = "Записаться на курсы по Python"

# tasks = {}

# run = True

# def add_todo(date, task):
#    if date in tasks:
#        tasks[date].append(task)
#    else:
#        tasks[date] = []
#        tasks[date].append(task)
#    print("Задача", task, "для даты", date, "успешно добавлена")

# while run:
#     command = input("Введите команду: ")
#     if command == "help":
#         print(HELP)
#     elif command == "show":
#         date = input("Введите дату для просмотра списка задач: ")
#         if date in tasks:
#           for task in tasks[date]:
#             print('-', task)
#         else:
#           print("Задач на дату", date, "отсутствуют")
#     elif command == "add":
#         date = input("Введите дату: ")
#         task = input("Введите задачу: ")
#         add_todo(date, task)
#     elif command == "random":
#         add_todo("Сегодня", RANDOM_TASKS)
#     # elif command == "random_date":
#     #    add_todo(RANDOM_DATE, RANDOM_TASKS)
#     elif command == "exit":
#         run = False
#         print("Спасибо за использование! До свидания!")
#     else:
#         print("Неизвестная команда")



# -------------------------------------------------------------------------------------------
