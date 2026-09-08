def share(a,b):
    match = False
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                match = True
    return match
a = [1,2,3,4]
b = [4,5,6,7]

print(share(a,b))