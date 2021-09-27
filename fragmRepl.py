# Дана строка. Замените в этой строке все появления
# буквы h на букву H, кроме первого и последнего вхождения.
# Вводится строка.
# Выведите ответ на задачу.
#
# Пример
# Ввод
# In the hole in the ground there lived a hobbit.
# Вывод
# In the Hole in tHe ground tHere lived a hobbit.

def func(string):
    count_char = string.count("h")
    fst_input = string.find("h")

    if count_char > 0:
        newstr1 = string.replace("h", "H", count_char - 1)
        newstr2 = newstr1[:fst_input] + "h" + newstr1[fst_input + 1:]
        return newstr2

    return string


print(func(input("Введите строку: ")))
