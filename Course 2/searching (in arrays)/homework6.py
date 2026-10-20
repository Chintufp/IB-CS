def interpolation_search(k, vals):
    l = 0
    h = len(vals)-1
    
    i = 0
    while l <= h  and vals[l] <= k <= vals[h]: # make sure list aint empty and k is between them vals
        if vals[l] == vals[h]: return l

        i = int(l + ((k-vals[l])/(vals[h]- vals[l])) * (h-l)) #index gotta be a int
        if vals[i] == k:
            return i
        elif vals[i] < k:
            l = i + 1   # k must be to the right
        else:
            h = i - 1   # k must be to the left

    return -1

vals = [3, 8, 12, 15, 21, 27, 30, 34, 41, 45, 52, 58, 63, 67, 72, 79, 84, 88, 93, 99]

print(interpolation_search(41, vals))   # 8 