number = int(input("enter a number: "))
while number > 9:
    result = 1
    for i in str(number):
        result *= int(i)
        number = result
print(number)

