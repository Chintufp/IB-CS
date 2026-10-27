def bubble_sort(arr):
    ordered = False
    while not ordered:
        ordered = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1] :
                (arr[i], arr[i+1]) = (arr[i+1], arr[i])
                ordered = False


array = [7,9,11,2]
bubble_sort(array)
print(array)


