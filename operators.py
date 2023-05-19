# Arithmetic operators
x = 2
y = 3
total = x + y
print(total)

total = x - y
print(total)

total = x * y
print(total)

total = x / y
print(total)

total = x % y
print(total)

total = x ** y
print(total)

# Comparison operator

a = 30
b = 60
out = (a < b)
print(out)

out = (a > b)
print(out)

out = (a == b)
print(out)

out = (a != b)
print(out)

out = (a <= b)
print(out)

out = (a >= b)
print(out)

# Assignment operator

c = 0
d = 1

# c+=d # c = c + d
print(c)

c-=d # c = c + d
print(c)

# Logical operator

# and
# or

a = 40
b = 60

y = 2
x = 3

out = (a < b) or (y > x)
print(out)

out = (a < b) and (y > x)
print(out)

# Membership operator

first_tuple = ("DevOps", "str", "iot", 12)
ans = "DevOps" in first_tuple
print(ans)

ans = "DevOps" not in first_tuple
print(type(ans))

ans = 12 not in first_tuple
print(ans)

# Identity operator

a = 12
b = 11

result = a is b
print(result)

result = a is not b
print(result)
