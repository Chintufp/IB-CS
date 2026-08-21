smallest = 0
largest = 0
for n in range(51):
    value = n*(n-30)*(n-50)
    if value < smallest:
        smallest = value
    if value > largest:
        largest = value

print(smallest, largest)