a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))
ab = a - b
ac = a - c
bc = b - c

if ab * bc > 0:
    result = b
elif ab * ac < 0:
    result = a
else:
    result = c

print(result)