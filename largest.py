# code to find thge largest element in the given list

class Solution:

    def largest_array(self, num_list):
        largest = num_list[0]
        for num in num_list:
            if (num > largest):
                largest = num
        return largest

list1 = [1, 4, 6, 3, 9, 4]
s1 = Solution()
print(s1.largest_array(list1))
