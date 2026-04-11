f = open("data.txt", "r")

# data  = f.read()
# print(data)
# print(type(data))

firstLine = f.readline()

print(firstLine)

secondLine = f.readline()

print(secondLine)

f.close()