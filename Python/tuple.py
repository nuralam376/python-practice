tup = (1,2,"abc", None, 3.14, True)

print(tup)
print(type(tup))
print(tup[2:4])
print(tup[:])

nums = (1) 
print(type(nums)) #int
nums = (1,2,3,4,5)
print(type(nums))

# nums[2] = 3 is not possible, because tuple is immutable like string

sum = 0
for val in nums:
    sum += val

print(f"Sum of nums is {sum}")
print(nums.index(3))
print(nums.count(2))