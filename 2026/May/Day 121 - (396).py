# 396. Rotate Function

# You are given an integer array nums of length n.
# Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:
# F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
# Return the maximum value of F(0), F(1), ..., F(n-1).
# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:
# Input: nums = [4,3,2,6]
# Output: 26
# Explanation:
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
# So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

# Example 2:
# Input: nums = [100]
# Output: 0

# Constraints:
# n == nums.length
# 1 <= n <= 105
# -100 <= nums[i] <= 100

class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)
        
        # Calculate F(0) initially
        current_f = 0
        for i in range(n):
            current_f += i * nums[i]
        
        max_f = current_f
        
        # Iteratively calculate F(1) to F(n-1) using the pattern
        # We go backwards through the array to pick the element 
        # that moves from index (n-1) to index 0
        for k in range(1, n):
            # find curent, and minus the previous to complete the pattern
            current_f = current_f + total_sum - n * nums[n - k]
            if current_f > max_f:
                max_f = current_f
                
        return max_f
    
# Initially I miss-understood the question but after giving the question to Gemini to clear up, this all makes sense.