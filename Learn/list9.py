
## try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Деление на ноль!")
# finally:
#     print("Этот блок выполнится в любом случае.")

# # raise ZeroDivisionError("Деление на ноль!")

# ↓ try
# try:
#     result = 10 / 0  # Это вызовет ZeroDivisionError
# except ZeroDivisionError:
#     print("Деление на ноль невозможно!")  # Вывод: Деление на ноль невозможно!

# try:
#     value = int(input("Введите число: "))
#     result = 10 / value
# except ValueError:
#     print("Ошибка: введено не число!")
# except ZeroDivisionError:
#     print("Ошибка: деление на ноль!")

# try:
#     num = int(input("Введите число: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Ошибка: деление на ноль!")
# except ValueError:
#     print("Ошибка: введено не число!")
# else:
#     print("Результат:", result)  # Этот код выполнится, если исключений не было

# try:
#     file = open("example.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("Файл не найден!")
# finally:
#     # Этот код выполнится в любом случае
#     print("Закрытие файла.")
#     if 'file' in locals():
#         file.close()  # Закрытие файла, если он был открыт

# try:
#     # Код, который может вызвать любое исключение
#     x = 1 / 0
# except Exception as e:
#     print("Произошла ошибка:", e)  # Выводит сообщение об ошибке

# ↑ try
