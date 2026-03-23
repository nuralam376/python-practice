a = 10
b = 5

# Arithmatic
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

# Relational
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# Assignment
a = b
print(a)
a += b 
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)
a %= b
print(a)
a **=b
print(a)

# Logical
print(not (5 > 8))
print((5 > 3) and (6 > 1))
print((5 > 3) or (3 > 9))

# Type Conversion
a = int(5 + 10.0) # Type Casting
print(a, type(a))
a = 5 + 10.0 # Type Concersion
print(a, type(a))
val = bool(1)
print(val, type(val))
val = bool(0);
print(val, type(val))
val = bool(-10)
print(val, type(val))