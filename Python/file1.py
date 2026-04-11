word = "Python"
line = 1
data = True

with open("data.txt", "r") as f:
    while data:
        data = f.readline()

        if(word in data):
            print(f"{word} found at line {line}")
            break

        line += 1
    


