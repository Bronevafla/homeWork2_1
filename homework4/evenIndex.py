def getEven():
    sumN = int(input("Введите колличество чисел: "))
    nums = input("Введите числа: ").split(" ")
    i = 0
    while i < sumN:
        if i % 2 == 0:
            if i < sumN - 1:
                print(nums[i], end=" ")
            else:
                print(nums[i])
        i = i + 1


try:
    getEven()
except ValueError:
    print(exit("Введены невалидные значения"))
