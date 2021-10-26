def isContainsNumber():
    set = {formatNumber(input("Введите проверяемый номер: "))}
    list = []
    for i in range(3):
        list.append(formatNumber(input("Введите номер из книги: ")))
    for el in list:
        if el in set:
            print("YES")
        else:
            print("NO")


def formatNumber(number: str):
    reformat = number.replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
    if reformat.startswith("7495"):
        editNumber = "8" + reformat[1:]
        return editNumber
    if reformat[0] != "7" and reformat[0] != "8":
        editNumber = "8495" + reformat
        return editNumber
    else:
        return reformat


isContainsNumber()
