a = int(input("Enter exponent: "))
b = int(input("Enter another number: "))

i = 0
answer = 1

while i < a:
    answer *= b
    i += 1

print(answer)