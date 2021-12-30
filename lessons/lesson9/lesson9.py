with open("1.txt", "w") as file:
    text = "привет"
    n = 1;
    while n < 11:
        file.write(text + "\n")
        n += 1

with open("1.txt", "r") as file:
    file = open("1.txt", "r")
    print(file.read())