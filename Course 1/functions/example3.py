def swap(lst, ind1, ind2):
    lst[ind1], lst[ind2] = (lst[ind2], lst[ind1])

lst = list(range(5))

swap(lst, 0,2)
print(lst)