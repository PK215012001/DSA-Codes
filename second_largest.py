# code to find second largest number of an array
class Solution:
    def secondLargestElement(self, nums):
        first = nums[0]
        second = float('-inf')
        for num in nums:
            if (num > first):
                second = first
                first = num
            elif(num > second and num < first):
                second = num
        if (second == float('-inf')):
            return -1
        return second

nums = [8, 8, 8, 8, 8]
s1 = Solution()
print(s1.secondLargestElement(nums))