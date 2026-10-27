def insertion_sort(array):
    n = len(array)
    i = 1
    while i < n:
        val = array[i]          # the number we're inserting
        j = i - 1               # start comparing with the one to its left
        while j >= 0 and array[j] > val:
            array[j + 1] = array[j]   # shift bigger number one spot right
            j = j - 1
        array[j + 1] = val      # drop val into the gap
        i = i + 1
    return array

print(insertion_sort([9, 7, 2, 11]))   


#time complexity O(n)