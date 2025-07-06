# code to find the max no.of consecutive ones in an array
nums = [1, 1, 2, 1, 1, 1, 3, 1, 1]
max_count = 0
count = 0
for num in nums:
    if(num == 1):
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print(max_count) 