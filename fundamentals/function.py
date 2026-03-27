def hello():
    print("Hello")
    print("From Python")

hello()

def sum(a,b):
    ans = a + b
    print("Greater" if a > b else "Not Greater")
    return ans

ans = sum(3,4)
print("Sum ", ans)
print(sum(5,9))

def calc_avg(a,b,c):
    sum = a + b + c;
    avg = sum / 3
    return avg

print(calc_avg(1,2,3))

def multiply(a,b = 2):
    return a * b

print(multiply(3))


sum = lambda a,b,c : a + b + c

print(sum(1,2,3))

def calc_factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i
    
    return fact

n = int(input("Enter n: "))
print(calc_factorial(n))