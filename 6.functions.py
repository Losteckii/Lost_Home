# ***** Функции *****

# Создание (определение) функции

# 1 вариант. 
# Функция, которая не принимает данные (нет аргументов)
# и ничего не возвращает 

import re


def func_1():
    var_1 = 10
    var_2 = 20
    res = var_1 + var_2
    print(res)

# вызов функции 
# func_1()

# 2 вариант
# Функция, принимающая параметры (значения, данные) (обладает аргументами)
# и ничего не возвращающая 

# def func_2(arg_1):
#     res = arg_1 ** 2
#     print(res)

# func_2(10)


# def func_3(a, b, c):
#     res = a + b * c
#     print(res)

# func_3(1, 2, 3)

# Аргумент может иметь значение по умолчанию 
# def func_4(arg_1, arg_2=20):
#     print(arg_1 * arg_2)

# передача одного параметра 
# второй аргумент воспользуется значением по умолчанию 
# func_4(10)

# передача двух параметров 
# передоваемый параметр имеет приоритет над значением по умолчанию 
# func_4(10, 30)

# Позиционная передача параметров - позиции параметров соответствуют 
# позициям аргументов

# Именованная передача параметров
def func_5(a=10, b=20, c=30):
    print(a + b + c)

# func_5()
# func_5(c=100)
# func_5(5, 3)

# Передача произвольного количества параметров
# 1. позиционные параметры
def func_6(*args):
    print(args)
    res = args[0] + args[3]
    print(res)

# func_6(10, 20, 30, 40, 50)

# 2. Именованные параметры 
def func_7(**kwargs):
    print(kwargs)
    res = kwargs["val_1"] * kwargs["val_2"]
    print(res)

# func_7(val_1=10, val_2=20)

# 3 вариант.
# Функция, возвращающая значение 

# def func_8(arg_1, arg_2):
#     res = arg_1 // arg_2
#     return res

# a = func_8(100, 20)
# print(a)

def func_9(x, y):
    a = x * y
    b = x ** y
    return a , b

# print(func_9(2, 8))
# var_1, var_2 = func_9(2, 8)
# print(var_1, var_2)

# *** Безымянная функция (лямбда-функция, лямбда-выражение)

# Особенности
# - однострочная конструкция 
# - всегда обладает аргументами 
# - всегда возвращает значение 

my_lambda = lambda arg_1: arg_1 ** 3

# print(my_lambda(10))

# Пример 1. Передача лямбда выражения в функцию в качестве параметра
def func_10(f, a):
    res = f(a)  # тут применяется лямбда
    print(res)

# func_10(lambda x: x * x, 100)

# Пример 2. Словарь лямбда-выражений 
my_lambdas = {
    "key_1": lambda arg_1, arg_2: arg_1 + arg_2,
    "key_2": lambda a, b, c: a * b + c
}

res = my_lambdas["key_2"](10, 20, 30)

print(res)