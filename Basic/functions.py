def printWorld():
    print("Hello World")

printWorld()


def printSum(a, b) : 
    return a + b

print(printSum(1,2))


def printMultiple(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(printMultiple(10,20,2))
