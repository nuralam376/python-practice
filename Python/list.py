marks = [99,89,70,52,65]

print(marks)
print(marks[2])

marks[2] = 55

print(marks)
print(marks[2])
print(type(marks))
print(len(marks))
print(marks[2:len(marks)])

lists = [7, 9, "abc", True, 3.14, None]

print(lists)
print(type(lists))
print(lists[2:-2])

nums = [1,2,3]

nums.append(4)

print(nums)

nums.insert(2,10)

print(nums)

nums.sort()

print(nums)

nums.sort(reverse = True)

print(nums)

nums.reverse()

print(nums)


for val in nums:
    print(val)

x = 4
idx = 0

for val in nums:
    if val == x:
        print(idx)
        break
    idx += 1

print(f"{x} found at index {idx}")