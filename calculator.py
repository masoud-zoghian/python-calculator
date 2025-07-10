import time

def add(x,y):
    return x + y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x * y
def divide(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        print("y can not be zero!")
while True:
    print("Select the math operation")
    print("1 . sum")
    print("2 . subtract")
    print("3 .multiply")
    print("4 . divide")
    print("5 . exit")

    choise = input("(1,2,3,4,5) enter your choise: ")
    if choise == "5":
        break
    if choise not in ("1,2,3,4"):
        print("invalid selection")
        continue

    num1 = float(input("first number: "))
    num2 = float(input("second number: "))

    if choise == "1":
        print("result: ",add(num1 , num2))
    elif choise == "2":
        print("result: ",subtract(num1,num2))
    elif choise == "3":
        print("result: ",multiply(num1,num2))
    elif choise == "4":
        print("result: ","{:.2f}".format(divide(num1,num2)))
    time.sleep(1)