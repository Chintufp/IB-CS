s = int(input("Please gie the value of s: "))

n = 1
found = False

while not found:
    if n*(n+1)/2 > s:
        found = True
    else:
        n+=1

print(n)
