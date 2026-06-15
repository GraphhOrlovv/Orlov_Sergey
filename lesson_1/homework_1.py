""" 1."""
# name = 'Сергей'
# age = '24'
# height = '175.5'
#
# a = [1,2,3,4]
# b = 1
#
# word_age = ''
# if int(age) % 10 == b:
#     word_age = 'год'
# elif int(age) % 10 in a:
#     word_age = 'года'
# else:
#     word_age = 'лет'
#
# print(f'Меня зовут {name}\nМне {age} {word_age}\nМой рост равен {height} см')

""" 2."""
# x = 10
# print(type(x))
#
# x = 25.5
# print(type(x))
#
# x = 'Python'
# print(x)
# print(type(x))

""" 3."""
# a = 7
# b = a
# print(a,b)
#
# a = 10
# print(a,b)
# print('b не поменяло значения, так как она ссылается на тот же объект,\n'
#       ' что и а в момент присваивания, которое тогда было 7\n'
#       '     но а не хранит в себе информацию, она лишь ссылается на объект\n'
#       '         который мы ей присвоили')

""" 4."""
# x = y = z = 100
# print(x, y, z)
# print(id(x))
# print(id(y))
# print(id(z))
#
# if id(x) == id(y) == id(z):
#     print('id одинаковые\n')
# else:
#     print('id разные\n')
#
# x, y, z = 100, 101, 102
# print(x, y, z)
# print(id(x))
# print(id(y))
# print(id(z))
#
# if id(x) == id(y) == id(z):
#     print('id одинаковые')
# else:
#     print('id разные')

""" 5."""
# a = 5
# b = 10
# a, b = 10, 5
# print(a, b)

""" 6."""
# True = 5
# print = 10
# if = 20
# '''Это зарезервированные переменные'''

# import keyword
# print(keyword.kwlist)

""" 7."""
# var1 = 42
# var2 = 3.14
# var3 = "Hello"
# print(type(var1))
# print(type(var2))
# print(type(var3))
#
# var1 = 'Какая-то строка'
# print(type(var1))

""" 8."""
# name = 'Сергей'
# age = 30
# phone = '8-920-933-67-59'
# email = 'sergey@mail.ru'
# weight = '75.3'
#
# print(f'name = {name}, тип: {type(name)}')
# print(f'age = {age}, тип: {type(age)}')
# print(f'phone = {phone}, тип: {type(phone)}')
# print(f'email = {email}, тип: {type(email)}')
# print(f'weight = {weight}, тип: {type(weight)}')

переменная = 10
print(переменная)
print('\nРаботает, но лучше так не делать)))')
