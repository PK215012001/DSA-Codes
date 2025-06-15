# rotating an array by n places, brute force approach

arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 4
temp = arr[:k]
arr[:len(arr) -k-1] = arr[k:]
arr[k:] = temp


# optimal solution
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
k = 3

def reverse_array(arr, start, end):
    '''Function to reverse an array'''
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

reverse_array(arr1, 0, k-1)
reverse_array(arr1, k, len(arr1) -1)
reverse_array(arr1, 0, len(arr1) - 1)
print(arr1)


def reverse_array_1(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
arr2 = [1, 2, 3, 4, 5, 6,7]
reverse_array(arr2,0, len(arr2) - 1)        
reverse_array(arr2,0,k-1)
reverse_array(arr2, k, len(arr2) - 1)
print(arr2)