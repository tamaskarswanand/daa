import time

def partition(array, low, high):
    pivot = array[low]

    i = low + 1
    j = high

    while i <= j:
        while array[i] <= pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        
        if i <= j:
            array[i], array[j] = array[j], array[i]

    array[j], array[low] = array[low], array[j]
    return j

def quicksort(array, low, high):
    if low < high:
        j = partition(array, low, high)
        quicksort(array,low,j-1)
        quicksort(array,j+1,high)

array = [12, 4, 5, 6, 7, 3, 1, 15]
low = 0
high = len(array)-1

start_time = time.time()

for i in range(0,10000):
    array = [1,2,3,4,5,6,7,8,9,10]
    low = 0
    high = len(array)-1
    quicksort(array, low, high)  
     
end_time =  time.time()

execution_time = end_time - start_time
print("Sorted Array: ", array)
print(f"deterministic quicksort execution time: {execution_time:.4f}")