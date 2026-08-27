x = int(input("Enter a number: "))
y = int(input("Enter exponent number: "))

result = 1

while y > 0:
    if y % 2 == 0:
        y = y / 2
        x = x * x
    else :
        y = y - 1
        result = result * x

print(result)