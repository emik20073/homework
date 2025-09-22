while True:
    num1 = int(input("enter first number: "))
    operation = input("enter an operation (+,-,*,/): ")
    num2 = int(input("enter second number: "))

    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        if num2 == 0:
            print("error: division by zero")
        else:
            print(num1 / num2)
    a = input("continue? (y/n):")
    if a == "n":
        break
