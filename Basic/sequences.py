list = [1, 2, 3, 4]

print(list[2])
print(list[:3])
print(list[-3:-1])

list.insert(2,9)
list.append(6)
print(list)


list.pop()
list.pop(2)
print(list)

list.remove(2)
print(list)


print(list.index(3))

for i in range(len(list)):
    print(i)

print(min(list))
print(max(list))


person = {"name" : "Abc", "age" : 25}
print(person)
print(person.items())
print(person.values())
print(person.keys())


tuple = (1,2,4)
print(tuple)
print(2 in list)
print(9 not in list)


x = 18

if type(x) is int:
    print("x is int")
else:
    print("x is not int")
