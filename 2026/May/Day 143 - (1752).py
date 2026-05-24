# 1752. Check if Array Is Sorted and Rotated

# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].

# Example 2:
# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.

# Example 3:
# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # go thorugh every position ensuring there is only 1 break in the pattern of always increasing numbers
        # then check (given there is a break) that the value in position 0 is > that in the last
        n = len(nums)
        breaks = 0
        
        for i in range(n):
            # Use modulo to compare the last element back to the first
            if nums[i] > nums[(i + 1) % n]:
                breaks += 1
        
        # If there's more than one break, it's not a rotated sorted array
        return breaks <= 1