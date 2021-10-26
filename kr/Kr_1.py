import math


def func(maxStd1: int, maxStd2: int, maxStd3: int):
    sumStd = maxStd1 + maxStd2 + maxStd3
    return math.ceil(sumStd / 2)


print(func(int(input("std1 ")), int(input("std2 ")), int(input("std3 ")))
      )
