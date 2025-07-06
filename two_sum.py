# Programme to find if two numbers will be added to reach target
nums = [2, 6, 5, 8, 11]
target = 14
# Brute force approach
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if(nums[i] + nums[j] == target):
            print(i, j, True)
            break

# Next one is using hashing in dict, we will store eleemnts serially from list into
# dict and if the other number to reach the target is found we will return it
hash_dict = {}
for i in range(len(nums)):
    more = target - nums[i]
    if(more in hash_dict):
        print(i, hash_dict[more], True)
    hash_dict[nums[i]] = i

# this one is spatially optimised, then we can use below one
nums = sorted(nums)
left = 0
right = len(nums) - 1
while(left < right):
    sum1 = nums[left] + nums[right]
    if(sum1 == target):
        print(True)
        break
    elif(sum1 < target):
        left += 1
    else:
        right -= 1
