lst = [ x % 3 for x in range(10)]
for x in lst:
    print(x, end='-')

print()

lst = [ c for c in "thingamabob"]
for i in range(len(lst)):
    if i % 2 == 0:
        print(lst[i], end=' ')