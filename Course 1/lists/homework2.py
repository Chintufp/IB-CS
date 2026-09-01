positive = []
negative = []

while (num := int(input("Enter a number (0 to stop): "))) != 0:
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)

print("Positive numbers:", positive)
print("Negative numbers:", negative)