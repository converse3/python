def createText(len, str):
    for i in range(len):
        print(str)


len = int(input("Количество повтороений слова: "))
str = (input("Слово для повторения: "))
createText(len, str)
