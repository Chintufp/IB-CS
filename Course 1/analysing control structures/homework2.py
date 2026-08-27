def fun(x):
    flag = True
    i = 2
    while flag and i < len(x):
        if x[i] - x[i-1] != x[i-1] - x[i-2]:
            flag = False
        else:
            i += 1

    return flag

k = [7,3,-1, -5, -8, -12]
print(fun(k))

# The purpose of this program is to check if the difference between consecutive numbers is the same. It checks to see if the list is an arithmetic sequence.

