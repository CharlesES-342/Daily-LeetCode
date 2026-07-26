# 628. Maximum Product of Three Numbers

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# Example 1:
# Input: nums = [1,2,3]
# Output: 6

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 24

# Example 3:
# Input: nums = [-1,-2,-3]
# Output: -6

# Constraints:
# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # there are 3 cases (3 positives - all of max), 2 negatives (2 smallest and 1 largest)
        # and 3 negative (all of max value - this is the same logic as the 3 positives approach)
        # so directly compair case of 3, and the case of 1 (positive numbers chosen)
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])        