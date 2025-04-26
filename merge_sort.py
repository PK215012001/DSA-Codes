# This algo will divide and merge the subarrays
num_list = [25, 87, 102, 15, 2, 32]
def merge(num_list, low,mid, high):
    temp = []
    left = low
    right = mid + 1
    while(left <= mid and right <= high):
        if (num_list[left] <= num_list[right]):
            temp.append(num_list[left])
            left +=1
        else:
            temp.append(num_list[right])
            right+=1
    while(left <= mid):
        temp.append(num_list[left])
        left+=1
    while(high >= right):
        temp.append(num_list[right])
        right+=1
    # copying back the sorted temp array into num_list
    for i in range(len(temp)):
        num_list[low+i] = temp[i]

def sort(num_list, low, high):
    if (low == high):
        return 
    mid = (low + high) // 2
    sort(num_list, low, mid)
    sort(num_list, mid+1, high)
    merge(num_list, low, mid, high)

sort(num_list, 0, len(num_list) - 1)
print(num_list)
