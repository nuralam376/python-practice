word1 = "Python"
word2 = "Programming"

print(word1 + " " + word2)

print(word1[0])
print(word1[2])
print(word1[2:4])
print(word2[-4:-2])
print(word2[:])
print(word1[2:len(word1)])

a = 5
b = 6
sum = a + b
print("Language is {}".format("Python"))
print("Sum of {} & {} is {}".format(a,b,sum))
print("Sum of {1} & {0} is {2}".format(a,b,sum))
print("Values of {c} and {d}".format(c = 5, d = 6))
print(f"Sum of {a} and {b} is {sum}")
print(f"Avg of {a} and {b} is {(a + b) / 2}")