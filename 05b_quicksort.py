import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)

# Driver code
if __name__ == "__main__":
    # Example usage
    arr = [12, 4, 5, 6, 7, 3, 1, 15]
    n = len(arr)
    print("Original array:", arr)
    
    randomized_quick_sort(arr, 0, n - 1)
    
    print("Sorted array:", arr)
