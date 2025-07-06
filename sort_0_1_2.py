# Here the array contains only 0, 1, 2 and we want to sort it
#  Brute force approach is using any type of sort and takes o(nlogn) TC, o(n) sc

# Better approach taking no.of 0's, 1's, 2's in seperate variables and then overwrite the array with that 
# no.of values

nums = [0, 1, 2, 0, 1, 1, 2, 2, 0, 0, 0, 1, 1, 1]
cnt0 = 0
cnt1 = 0
cnt2 = 0
for num in nums:
    if(num == 0):
        cnt0 += 1
    elif(num == 1):
        cnt1 += 1
    elif(num == 2):
        cnt2 += 1

nums[:cnt0] = [0] * (cnt0)
nums[cnt0: cnt0+cnt1] = [1] * (cnt1)
nums[cnt0 + cnt1:] = [2] * (cnt2)
print(nums)

# above TC -> o(2n), SC -> o(1)

# optimal approach -> dutch national flag approach,uses low, mid, high
# at any time
#  0->low-1, sorted and contains 0
# low->mid-1, sorted and contains 1
# mid -> high, unsorted and can contains anything
# high+1 -> end, sorted and contaisn 2's

low = 0
mid = 0
high = len(nums) - 1

while mid <= high:
    if(nums[mid] == 0):
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
    elif(nums[mid] == 1):
        mid += 1
    else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1

print(nums)
