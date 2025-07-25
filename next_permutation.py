class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = float('-inf')
        for i in range(len(nums) -2, -1, -1):
            if(nums[i] < nums[i+1]):
                index = i
                break
        if(index != float('-inf')):
            for i in range(len(nums) -1, -1, -1):
                if(nums[i] > nums[index]):
                    nums[i], nums[index] = nums[index], nums[i]
                    break
            nums[index+1:] = nums[len(nums)-1 : index: -1]
        else:
            nums[:] = nums[::-1]