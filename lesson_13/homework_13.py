"""
++++++++++++++++++++++++++++++++++++++++++++++++
Декораторы в Python
++++++++++++++++++++++++++++++++++++++++++++++++
===============================================
1. Напишите декоратор uppercase_decorator, который делает результат выполнения функции прописными буквами.
Пример вызова:
@uppercase_decorator
def say_hello():
    return "hello, world!"
print(say_hello())  # "HELLO, WORLD!"
==============================================="""

# def uppercase_decorator(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs).upper()
#     return wrapper
#
# @uppercase_decorator
# def say_hello():
#     return "hello, world!"
#
# print(say_hello())

"""2. Создайте декоратор repeat(n), который выполняет функцию n раз.
Пример вызова:
@repeat(3)
def hello():
    print("Hello!")
hello()
Вывод:
Hello!
Hello!
Hello!
==============================================="""

# def repeat(n):
#     def repeat_n(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return repeat_n
#
# @repeat(3)
# def hello():
#     print("Hello!")
#
# hello()

"""3. Создайте декоратор cache, который кэширует результаты выполнения функции.
Если функция вызывается с теми же аргументами – возвращать сохраненный результат вместо нового вычисления.
Пример вызова:
@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b
print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
print(slow_add(2, 3))  # 5 (результат взят из кэша)
==============================================="""

# def cache(func):
#     results = {}
#     def wrapper(*args):
#         if args in results:
#             print("результат взят из кэша")
#             return results[args]
#         res = func(*args)
#         results[args] = res
#         return res
#     return wrapper
#
# @cache
# def slow_add(*args):
#     str_with_numbers = " + ".join(str(arg) for arg in args)
#     print(f"Вычисляю {str_with_numbers}...")
#     return sum(args)
#
# print(slow_add(2, 3), '\n')
# print(slow_add(2, 3), '\n')
# print(slow_add(1, 3), '\n')
# print(slow_add(2, 3, 4))

"""4. Создайте декоратор с таймером timer(repeat), который выполняет функцию repeat раз и выводит среднее время выполнения.
Пример вызова:
@timer(3)
def slow_function():
    time.sleep(1)
slow_function()  # Среднее время выполнения: 1.0002 сек
"""

# import time
#
# def timer(repeat=0):
#     def timer_in(func):
#         results_time = []
#         def wrapper(*args, **kwargs):
#             for i in range(1, repeat+1):
#                 time_before = time.time()
#                 func(*args,**kwargs)
#                 time_after = time.time()
#                 result = time_after - time_before
#                 results_time.append(result)
#                 print(f"Время выполнения {i}-{'ей' if i == 3 else 'ой'} функции {func.__name__} = {result}") # для себя добавил, так красивее как будто
#             print(f"Среднее время выполнения: {sum(results_time) / len(results_time)}")
#         return wrapper
#     return timer_in
#
# @timer(3)
# def slow_function():
#     time.sleep(1)
#
# slow_function()














