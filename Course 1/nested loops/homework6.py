def symm_diff(a,b):
    lst = []
    for i in a:
        if i not in b: lst.append(i)
    for i in b:
        if i not in a: lst.append(i)
    return lst

a = [4,4,6,11,-2,3]
b = [5,11,11,-3,3,5]
print(symm_diff(a,b))