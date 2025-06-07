#  checking whether the array is sorted or not

def is_sorted(nums):
    for i in range(len(nums) - 1):
        if (nums[i+1] >= nums[i]):
            continue
        else:
            return False
    return True

print(is_sorted([0, 0, 2, 3, 4, 5]))