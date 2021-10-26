def func():
    try:
        i = int(input())
    except ValueError:
        return exit("Введено невалидное значение")
    if i != 0:
        func()
    print(i)


func()
