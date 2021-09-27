# Назовем число палиндромом, если оно не меняется при
# перестановке его цифр в обратном порядке.
# Напишите программу, которая по заданному числу K выводит
# количество натуральных палиндромов, не превосходящих K.
# Формат ввода
# Задано единственное число K (1 ≤ K ≤ 100 000).
# Формат вывода
# Необходимо вывести количество натуральных палиндромов, не превосходящих K.
# Пример 1
# Ввод
# 1
# Вывод
# 1
# Пример 2
# Ввод
# 100
# Вывод
# 18
import array


def get_arr(i):
    if i < 1:
        return exit("Введенное число меньше единицы")
    elif i > 100000:
        return exit("Введенное число больше 100.000")

    arr = []
    count = 1

    while len(arr) < i:
        arr.append(count)
        count = count + 1

    return arr


def pali_count(a: array):
    pali_arr = []

    for i in a:
        rev = str(i)[::-1]
        if rev == str(i):
            pali_arr.append(i)

    return len(pali_arr)


print(
    pali_count(
        get_arr(
            int(input("Введите натуральное число: ")))))
