# 3637. Tronic Array 1

# You are given an integer array nums of length n.
# An array is trionic if there exist indices 0 < p < q < n − 1 such that:
# nums[0...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...n − 1] is strictly increasing.
# Return true if nums is trionic, otherwise return false.


# Example 1:
# Input: nums = [1,3,5,4,2,6]
# Output: true
# Explanation:
# Pick p = 2, q = 4:
# nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
# nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
# nums[4...5] = [2, 6] is strictly increasing (2 < 6).

# Example 2:
# Input: nums = [2,1,3]
# Output: false
# Explanation:
# There is no way to pick p and q to form the required three segments.


# Constraints:
# 3 <= n <= 100
# -1000 <= nums[i] <= 1000

class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #up to q increasing
        #from p to q they are decreasing
        #ignor n-1
        n = len(nums)
        i = 0
        #strictly increasing (must move at least one step)
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        p = i
        if p == 0:  # no increasing prefix
            return False

        #strictly decreasing (must move at least one step)
        while i < n - 1 and nums[i] > nums[i + 1]:
            i += 1
        q = i
        if q == p:  # no decreasing middle
            return False

        #strictly increasing (must reach the end)
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1

        #q must not be n-1, and everything has been considered
        return i == n - 1 and q < n - 1
        
            
        