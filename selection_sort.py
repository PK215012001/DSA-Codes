# This sorts by putting small numbers in the array one by one
nums_list = [12, 3, 2, 4, 134, 98, 25, 3]

for i in range(len(nums_list) - 1):
    min_index = i
    for j in range(i+1, len(nums_list)):
        if (nums_list[j] < nums_list[min_index]):
            min_index = j
    nums_list[i], nums_list[min_index] = nums_list[min_index], nums_list[i]
print(nums_list)