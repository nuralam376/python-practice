try:
    number = int(input("Enter number: "))
    ans = 10 / number
except ZeroDivisionError:
    print("Zero Division Error")
except ValueError:
    print("Value Error")
else:
    print(f"Ans = {ans}")
finally:
    print("Programme Stopped")