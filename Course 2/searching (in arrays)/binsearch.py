def bin_search(key, array):
    lo = 0
    hi = len(array) -1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = array[mid]
        if key == val: 
            return True
        elif key < val:
            hi = mid -1
        else:
            lo = mid +1
    return False



lst = [-2, 3, 6, 11, 224, 1001]
print(bin_search(3, lst))
print(bin_search(5, lst))
