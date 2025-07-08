#  Rearranging the array as +ve, -ve in the given order
nums = [-4, -3, -2, 1, 2, 3]
pos_list = [x for x in nums if x>0]
neg_list = [x for x in nums if x<0]
for i in range(len(nums)):
    if(i %2 == 0):
        nums[i] = pos_list[i//2]
    else:
        nums[i] = neg_list[(i - 1)//2]
print(nums)

# another method
for i in range(len(nums)//2):
    nums[2*i] = pos_list[i]
    nums[2*i + 1] = neg_list[i]
print(nums)

# Optimal approach
pos_index = 0
neg_index = 1
ans = [0] * len(nums)
for num in nums:
    if (num > 0):
        ans[pos_index] = num
        pos_index += 2
    else:
        ans[neg_index] = num
        neg_index += 2
print(ans)

# second variety consists of unequal positive and negative numbers, then we have to follow brute force only
nums = [-2, -3, 1, 2, 3, 4, 5, 6, -9, -7, -3, -7, -56]
pos_list = [num for num in nums if num> 0]
neg_list = [num for num in nums if num <0]
if(len(pos_list) > len(neg_list)):
    for i in range(len(neg_list)):
        nums[2 * i] = pos_list[i]
        nums[2*i + 1] = neg_list[i]
    nums[2*i + 2 : ] = pos_list[len(neg_list) :]
else:
    for i in range(len(pos_list)):
        nums[2 * i] = pos_list[i]
        nums[2*i + 1] = neg_list[i]
    nums[2*i + 2 : ] = neg_list[len(pos_list) :]
print(nums)