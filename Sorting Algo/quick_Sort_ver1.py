#Lomuto partition scheme
def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p-1)
        quicksort(arr, p+1, hi)
    return(arr)
    
def partition(arr, lo, hi):
    pivot = arr[hi]   #set last element as pivot
    i = lo
    for j in range(lo, hi+1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return(i)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test, 0, len(test)-1))
#on initialisation, lo=starting index,=0 and
#hi=last index,=len(array)-1