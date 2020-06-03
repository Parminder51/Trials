#Hoare Partition Scheme
def quicksort(arr, lo, hi):
    if lo < hi:
        partition_border = partition(arr, lo, hi)
        quicksort(arr, lo, partition_border)
        quicksort(arr, partition_border+1, hi)
    return(arr)
    
def partition(arr, lo, hi):
    pivot = arr[((hi+lo)//2)]#pivot is taken
    i = lo                   #from the middle
    j = hi
    while True:
        while arr[i] < pivot:
            i+=1
        while arr[j] > pivot:
            j-=1
        if i>=j:
            return(j)
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test, 0, len(test)-1))
#on initialisation, lo=starting index,=0 and
#hi=last index,=len(array)-1