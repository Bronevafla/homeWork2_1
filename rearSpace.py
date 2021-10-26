# Дана строка слов, разделенных пробелами.
# Между словами может быть один
# или несколько пробелов, требуется заменить
# одиночный пробел или группу пробелов на символ "*".
# Пример
# Ввод
# мама мыла раму
# Вывод
# мама*мыла*раму

def rearSpc(string: str):
    arr = string.split()
    arr1 = []
    count = 0

    while count < len(arr) - 1:
        arr1.append(arr[count] + "*")
        count = count + 1
    else:
        arr1.append(arr[len(arr) - 1])

    return ''.join(map(str, arr1))


print(rearSpc(input("Введите строку: ")))
