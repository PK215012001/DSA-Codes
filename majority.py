# returning the element which appears more than half of array's length times
# Brute force approach using two for loops sc -> o(n sqauredo)
nums = [2, 2, 3, 3, 2, 2, 1]
for i in range(len(nums)):
    count = 0
    for num in nums:
        if(num == nums[i]):
            count += 1
    if(count > (len(nums) / 2)):
        print(nums[i])

# Optimal, by using hashing of values
print('---------------')
hash_map = {}
for num in nums:
    if num in hash_map:
        hash_map[num] += 1
    else:
        hash_map[num] = 1
for key, value in hash_map.items():
    if (value > len(nums) / 2):
        print(key)
#  we can even use counter from collections module especially used for counting purposes
from collections import Counter
count = Counter(nums)
print(count)
for key, value in count.items():
    if(value > len(nums) / 2):
        print(key)

print('-------------')

# optimal approach2 times
# this is moores voting algo, it's just if a number appears more than n/2 times, then it will not become 
#  zero if it is cancelled with other numbers
count = 0
for num in nums:
    if(count == 0):
        number = num
        count = 1
    elif(num == number):
        count += 1
    else:
        count -= 1

if(count > 0):
    count = 0
    for num in nums:
        if(num == number):
            count += 1
if(count > len(nums) / 2):
    print(number)

