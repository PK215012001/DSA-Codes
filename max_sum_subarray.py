# Programme to find the subarray with max sum
# better approach
#  brute force is taking anothe loop inside
nums = [-2, -3, 4, -7, -2, 1, 6, -3]
max_sum = float('-inf')
for i in range(len(nums)):
    sum = 0
    for j in range(i, len(nums)):
        sum += nums[j]
        max_sum = max(sum, max_sum)
print(max_sum)
print('---------')

# kaydens algo, it just takes subarrays when sum >0
max_sum = float('-inf')
sum = 0
indx = 0
for i in range(len(nums)):
    sum += nums[i]
    if (sum > max_sum):
        max_sum = sum
        sub_start = indx
        sub_end = i
    if(sum < 0):
        sum = 0
        indx = i + 1
print(max_sum)
print(sub_start, sub_end)
    