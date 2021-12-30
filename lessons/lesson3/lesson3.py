def hello():
    print("Hello, world!")


def sayHello(name):
    print("Hello,", name + "!")


def sum(a, b):
    return a + b


a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))

hello()
print("Sum =", sum(a, b))

name = input("Enter your name: ")
sayHello(name)
