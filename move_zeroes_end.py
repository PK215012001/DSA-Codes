# to move zeroes to the end
nums = [1, 0, 2, 3, 4, 0, 0, 0, 4, 7, 8]
temp = []
for num in nums:
    if (num != 0):
        temp.append(num)
nums[:len(temp)] = temp[:]
nums[len(temp):] = [0] * (len(nums) - len(temp))


# optimal solution 
arr1 = [1, 0, 2, 3, 4, 0, 0, 0, 4, 7, 8]
j = 0
for i in range(len(arr1)):
    if(arr1[i] != 0):
        arr1[i], arr1[j] = arr1[j], arr1[i]
        j += 1

print(arr1)