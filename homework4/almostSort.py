def isCanDell():
    s = input("Введите массив чисел: ")
    arr = s.split(" ")

    i = len(arr) - 1
    count = 0
    while i > 1:
        if arr[i] < arr[i - 1]:
            count = count + 1
            if arr[i] < arr[i - 2]:
                count = count + 1
        i = i - 1

    if count <= 1:
        return "YES"
    return "NO"


print(isCanDell())
