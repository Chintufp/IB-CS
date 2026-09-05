ints = []
while (x:= int(input("Enter non-negative integers: "))) > 0:
    ints.append(x)

print(ints)

filtered = list(set(ints))
print(filtered)


## OR ##
filtered = [i for i in ints if i not in filtered]