def alternate(lst):
    out =[]
    while lst !=[]:
        if len(lst) == 1:
            out.append(lst.pop(0))
        else:
            out.append(lst.pop(0))
            out.append(lst.pop())
    return out

print(alternate([1,2,3,4,5,6]))