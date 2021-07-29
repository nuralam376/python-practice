num1 = input("Enter first number : ")
num2 = input("Enter second number : ")

num1 = int(num1)
num2 = int(num2)

if(num1 > num2):
    print("num1 is greater than num2")
    if num1 > 100:
        print("num1 is greater than 100")
    else:
        print("num1 is less than 100")
elif num1 < num2:
    print("num1 is less than num2")
    if(num2 >= 0):
        print("num2 is positive")
    else:
        print("num2 is negative")
else:
    print("num1 is equal to num2")
