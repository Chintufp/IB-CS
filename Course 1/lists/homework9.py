lst = [[5,11,7],[1,2,3],[4,5,6]]

def transpose(a):
    new = []
    for lists in lst:
        for i in range(len(lists)):
            if len(new) <= i:
                new.append([])
            new[i].append(lists[i])
    return new

print(transpose(lst))