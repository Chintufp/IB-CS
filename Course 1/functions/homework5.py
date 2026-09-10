def REMOVE(orig, x, out):
    i = 0
    while x in orig:
        orig.remove(x)
        orig.append(0)
        i += 1
    out = orig
    return out

orig = [1,2,3,4,5,5,4,3,2,1]
out = [6,6,6,6,6,6,6,6]

print(REMOVE(orig, 4, out))