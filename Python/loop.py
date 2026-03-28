i = 1

while i <= 10:
    print(i)
    i+=1


j = 5

while (j > 0):
    print(j)
    j -= 1 

n = int(input("Enter num: "))
i = 0
while i < 10:
    print(n * (i + 1))
    i += 1


i = 0

while i < 10:
    if(i == 6):
        break
    i += 1

print(i)

i = 0

while(i < 10):
    i += 1
    if(i == 6):
        continue
    print(i)

i = 1

while i <= 10:
    print(i)
    i += 2

string = "Hello"

if "o" in string:
    print("o exists in string")

for ch in string:
    print(ch)


for k in range(5):
    print(k)

word = "Artificial Intelligence"
ans = 0

for ch in word:
    if ch == "i":
        ans += 1

print(ans)


word = "artificial"
count = 0

for ch in word:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        count += 1

print(count)

print("===================")
for i in range(1,6):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(2,11,2):
    print(i)

n = int(input("Enter number: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum = " , sum)