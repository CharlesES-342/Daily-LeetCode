# 3702. Longest Subsequence With Non-Zero Bitwise XOR

# You are given an integer array nums.
# Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.

# Example 1:
# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.

# Example 2:
# Input: nums = [2,3,4]
# Output: 3
# Explanation:
# The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.

# Constraints:
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109

class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # max is the value from the entire array
        total = 0
        for i in nums:
            total = total ^ i

        # by removing one element (given it is not 0) will result in a non-zero ourput
        # if only 0's exist then it is not possible
        if total == 0:
            # see if some removal ecists to make it work
            for i in nums:
                if i != 0:
                    return n-1
        else:
            # already works
            return n
        
        return 0 # all elements are 0