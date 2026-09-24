# 3550. Smallest Index With Digit Sum Equal to Index

# You are given an integer array nums.
# Return the smallest index i such that the sum of the digits of nums[i] is equal to i.
# If no such index exists, return -1.

# Example 1:
# Input: nums = [1,3,2]
# Output: 2
# Explanation:
# For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.

# Example 2:
# Input: nums = [1,10,11]
# Output: 1
# Explanation:
# For nums[1] = 10, the sum of digits is 1 + 0 = 1, which is equal to index i = 1.
# For nums[2] = 11, the sum of digits is 1 + 1 = 2, which is equal to index i = 2.
# Since index 1 is the smallest, the output is 1.

# Example 3:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# Since no index satisfies the condition, the output is -1.

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000


class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for pos, i in enumerate(nums):
            # spli the number by digits
            digit_sum = 0
            for j in str(i):
                digit_sum += int(j)
            if pos == digit_sum:
                return pos
        return -1

'''
You can make it more efficient slightly by removing the type conversions and just doig MOD 10 to get the
next index as the units
'''

class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for pos, val in enumerate(nums):
            # Calculate sum of digits mathematically
            digit_sum = 0
            temp = val
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
                
            if pos == digit_sum:
                return pos
                
        return -1