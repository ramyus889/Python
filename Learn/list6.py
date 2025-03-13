
# # Запись в файл
## with open('example.txt', 'w') as f:
#     f.write('Hello, World!')

# # Чтение из файла
## with open('example.txt', 'r') as f:
#     content = f.read()

# print(content)

# ↓ open()
# Чтение данных из файла
# with open('example.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# # Запись данных в файл
# with open('example.txt', 'w', encoding='utf-8') as file:
#     file.write('Hello, World!')

# # Добавление данных в файл
# with open('example.txt', 'a', encoding='utf-8') as file:
#     file.write('\nThis is an additional line.')

# # Чтение файла построчно
# with open('example.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line.strip())

# # Чтение бинарного файла
# with open('image.png', 'rb') as file:
#     data = file.read()
#     print(type(data))  # <class 'bytes'>

# # Обработка ошибок при открытии файла
# try:
#     with open('nonexistent.txt', 'r') as file:
#         content = file.read()
# except FileNotFoundError:
#     print("Файл не найден.")

# ↑ open()

