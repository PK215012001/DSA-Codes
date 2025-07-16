# Programme to find the largest consecutive sequence
nums = [102, 4, 100, 1, 101, 3, 2, 1, 1]
#Brute force approach
def linear_search(arr, num):
    '''function to linear search the element'''
    for x in arr:
        if(x == num):
            return True
    return False

max_count = 1
for num in nums:
    x = num
    count = 1
    while (linear_search(nums, x+1) == True):
        x = x + 1
        count += 1
    max_count = max(max_count, count)
print(max_count)

# Better approach is to sort it out and then do based on previous element
current_count = 0
last_smallest = float('-inf')
largest_count = 1
for num in sorted(nums):
    if(num - 1 == last_smallest):
        current_count += 1
        last_smallest = num
    elif(last_smallest != num):
        current_count = 1
        last_smallest = num
    largest_count = max(largest_count, current_count)
print(largest_count)

# optimal solution includes storing the array into set and we will use that
num_set = set(nums)
max_length = 1
for num in num_set:
    if(num - 1 not in num_set):
        current = num
        length = 1
        while(current + 1 in num_set):
            current += 1
            length += 1
        max_length = max(max_length, length)
print(max_length)