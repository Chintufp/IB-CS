found = False
i = 1
while not found:
    if (i**3 -16) % 47 == 0:
        found = True
    else:
        i += 1

print(i)