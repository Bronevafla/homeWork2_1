# Дана строка, состоящая ровно из двух слов,
# разделенных пробелом. Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся
# строку. При решении этой задачи
# нельзя пользоваться циклами и инструкцией if.
# Пример
# Ввод
# Hello, world!
# Вывод

# world! Hello,
import array


def rearStr(string: str):
    return string.split()[1] + " " + string.split()[0]


print(rearStr(input("Введите строку: ")))
