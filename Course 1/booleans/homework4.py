a = int(input ("Enter number: "))
b = int(input ("Enter another number: "))

n = 1
while n % a != 0 or n % b != 0:
    n += 1

print(n)
