# Дана строка. Получите новую строку, вставив между символами исходной
# строки символ *. Выведите полученную строку.
# Пример
# Ввод:
# Python
# Вывод:
# P*y*t*h*o*n

def func(string: str):
    for i in range(len(string)):
        newstr = string.replace("", "*")

    return newstr[1:len(newstr) - 1]


print(func(input("Введите строку: ")))
