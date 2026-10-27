def selection_sort(array):
    n = len(array)
    for i in range(n-1): #selecting ith smallest element
        print(array)
        smallest = array[i]
        smallest_ind = i
        for j in range(i+1, n):
            if array[j] < smallest: 
                smallest= array[j]
                smallest_ind = j
        #swap if necessary
        if smallest_ind != i:
                (array[i], array[smallest_ind]) = (array[smallest_ind], array[i])
    print(array)
    #no return because it mutilates the array itself

def bubble_sort(arr):
    ordered = False
    while not ordered:
        ordered = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1] :
                (arr[i], arr[i+1]) = (arr[i+1], arr[i])
                ordered = False
                print(arr)


lst=[-4,11,7,-12,6,1]
# selection_sort(lst)

bubble_sort(lst)
