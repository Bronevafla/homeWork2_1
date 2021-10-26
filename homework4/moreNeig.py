def getMore():
    numS = int(input("Введите колличество чисел: "))
    arr = input("Введите список чисел: ").split(" ")
    if int(numS) != int(len(arr)):
        return exit("Входные данные не валидны")
    count = 0
    i = 1
    while i < numS - 1:
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count = count + 1
        i = i + 1

    return count


print(getMore())

