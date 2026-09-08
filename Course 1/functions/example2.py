def interleave(a,b):
    flattened =[]
    for a,b in  zip(a,b):
        flattened.append(a)
        flattened.append(b)
    return flattened

print(interleave([1,2,3,4],['a','b','c','d']))