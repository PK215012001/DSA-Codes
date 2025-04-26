num_list = [25, 87, 102, 15, 2, 32]

def sort(arr, low, high):
    i = low
    j = high
    pivot = low
    while(i<j):
        while(arr[i]<= arr[pivot] and i <= high-1):
            i+=1
        while(arr[j] > arr[pivot] and j>= low+1):
            j-= 1
        if(i<j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j

def quicksort(arr, low, high):
    if (low < high):
        part_index = sort(arr, low, high)
        quicksort(arr, low, part_index-1)
        quicksort(arr, part_index+1, high)

quicksort(num_list, 0, len(num_list) - 1)
print(num_list)