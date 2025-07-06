# finding max subarray length of having sum k and it contains only psoitive elements
nums = [1, 2, 3, 0, 1, 1, 1, 0, 4, 2, 3] 
k = 3
# brute force approach, finding summation of all sub arrays
length = 0
for i in range(len(nums)):
    sum = 0
    for j in range(i, len(nums)):
        sum += nums[j]
        if (sum == k):
            length = max(length, j-i+1)
print(length)
print('--------------')

#  better approach
#  we will use prefixsum method
prefix_sum = 0
length = 0
sum_map = {}
for i in range(len(nums)):
    prefix_sum += nums[i]
    if (prefix_sum not in sum_map):
        sum_map[prefix_sum] = i
    if(prefix_sum == k):
        length = max(length, i+1)
    if(prefix_sum - k in sum_map):
        length = max(length, i - sum_map[prefix_sum - k])
print(length)
#  the above is also the optimal solution if the array contains negatives also, but it is only better if
# contains only non negative members
# optimal solution
print('--------------')
sum = 0
start = 0
length = 0
for end in range(len(nums)):
    sum += nums[end]
    while(sum > k):
        sum -= nums[start]
        start += 1
    if (sum == k):
        length = max(length, end - start +1)
print(length)