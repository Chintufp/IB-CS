s = int(input("Enter a number: "))
n = 1
value = n**3-10*n**2
while value < s:
    n += 1
    value = n**3-10*n**2

print(n, value)