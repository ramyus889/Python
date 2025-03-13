
## def example_func():
#     return "Hello"

## is_callable = callable(example_func)  # True
## get_attr = getattr(example_func, '__name__')  # 'example_func'
## set_attr = setattr(example_func, 'new_attr', 42)  # Добавляет атрибут
## del_attr = delattr(example_func, 'new_attr')  # Удаляет атрибут
## has_attr = hasattr(example_func, '__name__')  # True

# print(is_callable, get_attr, set_attr, del_attr, has_attr)

# ↓ callable()
# def my_function():
#     return "Hello, World!"

# print(callable(my_function))  # Вывод: True

# class MyClass:
#     def __call__(self):
#         return "I am callable!"

# obj = MyClass()
# print(callable(obj))  # Вывод: True

# class MyClass:
#     def my_method(self):
#         return "This is a method."

# obj = MyClass()
# print(callable(obj.my_method))  # Вывод: True

# class MyClass:
#     pass

# obj = MyClass()
# print(callable(obj))  # Вывод: False (экземпляр класса не является вызываемым)

# string = "Hello"
# print(callable(string))  # Вывод: False (строка не является вызываемой)

# number = 42
# print(callable(number))  # Вывод: False (число не является вызываемым)

# ↑ callable()

# ↓ getattr()
# class MyClass:
#     def __init__(self):
#         self.attribute = "Hello, World!"

# obj = MyClass()
# value = getattr(obj, 'attribute')
# print(value)  # Вывод: Hello, World!

# class MyClass:
#     pass

# obj = MyClass()
# value = getattr(obj, 'non_existent_attribute', 'Default Value')
# print(value)  # Вывод: Default Value

# class MyClass:
#     def greet(self):
#         return "Hello!"

# obj = MyClass()
# method = getattr(obj, 'greet')
# print(method())  # Вывод: Hello!

# class MyClass:
#     def __init__(self):
#         self.attribute = "Hello!"

# obj = MyClass()

# # Проверка наличия атрибута перед получением
# if hasattr(obj, 'attribute'):
#     value = getattr(obj, 'attribute')
#     print(value)  # Вывод: Hello!


# class MyClass:
#     class_attribute = "I am a class attribute"

# # Получение атрибута класса
# value = getattr(MyClass, 'class_attribute')
# print(value)  # Вывод: I am a class attribute

# ↑ getattr()

# ↓ setattr()
# class MyClass:
#     pass

# obj = MyClass()

# # Установка нового атрибута
# setattr(obj, 'new_attribute', 'Hello, World!')
# print(obj.new_attribute)  # Вывод: Hello, World!

# class MyClass:
#     def __init__(self):
#         self.attribute = "Old Value"

# obj = MyClass()

# # Изменение существующего атрибута
# setattr(obj, 'attribute', 'New Value')
# print(obj.attribute)  # Вывод: New Value

# class MyClass:
#     pass

# obj = MyClass()
# attr_name = 'dynamic_attribute'

# # Установка атрибута с использованием переменной
# setattr(obj, attr_name, 'Dynamic Value')
# print(obj.dynamic_attribute)  # Вывод: Dynamic Value

# class MyClass:
#     pass

# # Установка атрибута класса
# setattr(MyClass, 'class_attribute', 'I am a class attribute')
# print(MyClass.class_attribute)  # Вывод: I am a class attribute

# class MyClass:
#     def __init__(self):
#         self.attribute = "Initial Value"

# obj = MyClass()

# # Установка атрибута только если он не существует
# if not hasattr(obj, 'attribute'):
#     setattr(obj, 'attribute', 'New Value')
# else:
#     print("Attribute already exists:", obj.attribute)

# ↑ setattr()

# ↓ delattr()
# class MyClass:
#     def __init__(self):
#         self.attribute = "Hello, World!"

# obj = MyClass()

# # Удаление атрибута
# delattr(obj, 'attribute')

# # Проверка наличия атрибута после удаления
# print(hasattr(obj, 'attribute'))  # Вывод: False

# class MyClass:
#     pass

# obj = MyClass()

# # Удаление несуществующего атрибута (выдаст исключение)
# try:
#     delattr(obj, 'non_existent_attribute')
# except AttributeError as e:
#     print(e)  # Вывод: 'MyClass' object has no attribute 'non_existent_attribute'

# class MyClass:
#     class_attribute = "I am a class attribute"

# # Удаление атрибута класса
# delattr(MyClass, 'class_attribute')

# # Проверка наличия атрибута после удаления
# print(hasattr(MyClass, 'class_attribute'))  # Вывод: False

# class MyClass:
#     def __init__(self):
#         self.attribute = "To be removed"

# obj = MyClass()

# # Удаление атрибута только если он существует
# if hasattr(obj, 'attribute'):
#     delattr(obj, 'attribute')
#     print("Attribute deleted.")
# else:
#     print("Attribute does not exist.")

# ↑ delattr()

# ↓ hasattr()
# class MyClass:
#     def __init__(self):
#         self.attribute = "Hello, World!"

# obj = MyClass()

# # Проверка наличия атрибута
# print(hasattr(obj, 'attribute'))  # Вывод: True

# class MyClass:
#     pass

# obj = MyClass()

# # Проверка отсутствующего атрибута
# print(hasattr(obj, 'non_existent_attribute'))  # Вывод: False

# class MyClass:
#     def my_method(self):
#         return "This is a method."

# obj = MyClass()

# # Проверка наличия метода
# print(hasattr(obj, 'my_method'))  # Вывод: True

# class MyClass:
#     class_attribute = "I am a class attribute"

# # Проверка наличия атрибута класса
# print(hasattr(MyClass, 'class_attribute'))  # Вывод: True

# class MyClass:
#     def __init__(self):
#         self.attribute = "Initial Value"

# obj = MyClass()

# # Использование hasattr в условии
# if hasattr(obj, 'attribute'):
#     print("Attribute exists:", obj.attribute)  # Вывод: Attribute exists: Initial Value
# else:
#     print("Attribute does not exist.")

# ↑ hasattr()

