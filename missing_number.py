# finding the missing number from the given n, where the list contains 1 to n
nums = [3, 2, 4, 5]
n = 5

# Brute force approach
for i in range(1, n+1):
    flag = 0
    for num in nums:
        if(num == i):
            flag = 1
            break
    if(flag == 0):
        print(i)
        break

# Better solution involves using hash array
temp = [0] * (n+1)
for i in range(len(nums)):
    temp[nums[i]] = 1
for i in range(1, len(temp)):
    if(temp[i] == 0):
        print(i)

# Optimal1: By using sum method
sum1 = (n*(n+1))/2
sum2 = 0
for num in nums:
    sum2 += num
print(sum1 - sum2)

nums = [1, 2, 3, 4]
# optimal solution using xor method
xor1 = 0
xor2 = 0
for i in range(n - 1):
    xor1 = xor1 ^ nums[i]
    xor2 = xor2 ^ (i+1)
xor2 = xor2 ^ n
print(xor1 ^ xor2)