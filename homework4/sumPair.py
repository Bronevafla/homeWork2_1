def sumPair():
    numS = int(input("Введите колличество чисел: "))
    arr = input("Введите список чисел: ").split(" ")

    if int(numS) != int(len(arr)):
        return exit("Входные данные не валидны")

    i = 0
    count = 0
    while i < numS - 1:
        j = i + 1
        while j <= numS - 1:
            if int(arr[i]) == int(arr[j]):
                count = count + 1
            j = j + 1
        i = i + 1
    return count


try:
    print(sumPair())
except ValueError:
    print(exit("Введены невалидные значения"))
