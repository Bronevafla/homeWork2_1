# Исполнитель “Раздвоитель” преобразует натуральные числа. У него есть две команды: “Вычесть 1” и “Разделить на 2”,
# первая команда уменьшает число на 1, вторая команда уменьшает число в два раза, если оно чётное, иначе
# происходит ошибка.
# Дано два натуральных числа A и B (A>B).
# Напишите алгоритм для "Раздвоителя", который преобразует число A в число B и при этом содержит минимальное
# число команд.
# Команды алгоритма нужно выводить по одной в строке, первая команда обозначается, как -1, вторая команда как :2.
# Вводятся два натуральных числа A и B.
# Выведите ответ на задачу.

def func(source, final):
    if source <= 0 or final <= 0:
        print(exit("number not natural"))
    if final >= source:
        print(exit("\'A\' should be > \'B\'"))

    if source / 2 == final:
        source = source / 2
        print(":2")
    if source / 2 > final:
        if source % 2 == 0:
            source = source / 2
            print(":2")
            func(source, final)
        else:
            source = source - 1
            print("-1")
            func(source, final)
    else:
        while source != final:
            source = source - 1
            print("-1")


func(int(input("Введите первое число: ")),
     int(input("Введите второе число: ")))
