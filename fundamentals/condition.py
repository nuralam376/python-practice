age = 18

if age >= 18:
    print("You can vote")
    print("You can drive")
else:
    print("You can't vote")
    print("You can't drive")


color = input("Enter color: ")

if color == "red":
    print("Stop")
elif color == "green":
    print("Go")
elif color == "yellow":
    print("Look")
else:
    print("Wrong Color")


age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif (age >= 13 and age <= 18):
    print("Teenager")
else:
    print("Adult")


number = int(input("Enter number: "))

if(number % 5 == 0):
    print("Multiple of 5")
else:
    print("Not a multiple of 5")


username = input("Enter username: ")
password = input("Enter password: ")

if (username == "admin" and password == "password"):
    print("Login Successful")
elif username != "admin":
    print("Wrong username")
else:
    print("Wrong password")

n = int(input("Enter number: "))

if n % 2 == 0:
    print("Even")
else:
    print("ODD")

if (username == "admin" and password == "pass"):
    print("Login Successful")
else:
    if (username != "admin"):
        print("Wrong username")
    else:
        print("Wrong Password")


match color:
    case "green":
        print("Go")
    case "yellow":
        print("Look")
    case "red": 
        print("Stop")
    case _:
        print("Wrong input")