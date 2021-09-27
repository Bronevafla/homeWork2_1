# Пользователь вводит 10 слов.
# Определить, сколько из них начинаются с буквы 'S', содержат букву "i" и имеют длину 6 букв.
# Формат ввода: 10 слов, каждое в отдельной строке.
# Формат вывода: количество найденных слов.
import array


def getCount():
    words = []
    count = 0

    for i in range(5):
        words.append(input("Введите слово: ").strip())

    for w in words:
        if w.find("S") == 0:
            if "i" in w:
                if len(w) == 6:
                    count += 1

    return count


print(getCount())
