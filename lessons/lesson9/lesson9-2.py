try:
    a = int(input("Enter first num: "))
    b = int(input("Enter second num: "))
    print("Result is", a / b)
except ZeroDivisionError:
    print("You can't divide by zero")