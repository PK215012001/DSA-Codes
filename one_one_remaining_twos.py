# Code to find that one number which appers only once but remaining appears twice
nums = [1, 1, 2, 3, 3, 4, 4]
for num in nums:
    count = 0
    for i in range(len(nums)):
        if(nums[i] == num):
            count += 1
    if (count == 1):
        print(num)
        break
# Better solution is to form hash list withg max element value, first finding
# max element in it and form hash table according to it
max = nums[0]
for num in nums:
    if(num > max):
        max = num
hash_list = [0] * (max+1)
for num in nums:
    hash_list[num] += 1
for i in range(len(hash_list)):
    if(hash_list[i] == 1):
        print(i)

hash_dict = {}
count = 0
for num in nums:
    if num in hash_dict:
        hash_dict[num] += 1
    else:
        hash_dict[num] = 1
for key,value in hash_dict.items():
    if(value == 1):
        print(key)

# Optimal using xor on entire list because every element appers twice so xor is 0
# and the unique element will be resulted out itself
xor = 0
for num in nums:
    xor = xor ^ num
print(xor)

# One excellent leetcode solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = set()
        for i in nums:
            if i not in single:
                single.add(i)
            else:
                single.remove(i)
        return single.pop()

