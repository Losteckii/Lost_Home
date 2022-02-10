# Генератор паролей
# Пример:
# Pwd1234 - основа
# _google - "соль"
# хеш-строка 

# ***** Генератор паролей ********

# Импортирование модулей Ткинтер
# import tkinter 
from cgitb import text
from tkinter import Tk, StringVar, Label, Entry, Button 
import hashlib
from turtle import color

# объект окна
window = Tk() # пустые скобки (конструктор будет использовать значения по умолчанию)
window.title("Генератор паролей v.0.1")

# основная функция
def generator():
    """
    Функция хеширования строк паролей
    """
    # прием строки сырой пароли
    pwd_str = pwd.get()
    # 1. кодирование в байт-строку
    byte_str = pwd_str.encode()

    # 2. работа с функцией хеширование (применение хеш-функций)
    hash_str = hashlib.sha256(byte_str)

    # 3. преобразование объект хеш-строки в обычную строку (конвертация)
    hex_str = hash_str.hexdigest()[:10]

    # print(hex_str)

    # запись(set) хеш-строки в объект StringVar 
    hash_pwd.set(hex_str)

# generator("password")

# контейнеры для хранения строк
pwd = StringVar()
hash_pwd = StringVar()

# Виджет (компонент) текстовой метки приложения
Label(text="Пароль:").grid(row=0, column=0, padx=10, pady=10)
# виджет поля ввода
Entry(textvariable=pwd).grid(row=0, column=1, padx=10, pady=10)
# виджет кнопки
btn = Button(text="СТАРТ", command=generator)
btn.grid(row=1, column=0, padx=10, pady=10) 
# виджет поля вывода 
Entry(textvariable=hash_pwd).grid(row=1, column=1, padx=10, pady=10)


# запуск программы (точка входа программы)
window.mainloop()
