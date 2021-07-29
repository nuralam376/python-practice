x = 0
while x < 5:
    print(x)
    x += 1

x = 1
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1


x = 1
while x < 5:
    x += 1
    if x == 2:
        continue
    print(x)
  
x = 1
for x in range(5):
    print(x)


if x > 25:
    pass

print("Done")
