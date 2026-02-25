#1458. Max Dot Product of Two Subsequences

# Given two arrays nums1 and nums2.
# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with 
# the same length.

# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

# Example 1:

# Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# Output: 18
# Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
# Their dot product is (2*3 + (-2)*(-6)) = 18.
# Example 2:

# Input: nums1 = [3,-2], nums2 = [2,-6,7]
# Output: 21
# Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
# Their dot product is (3*7) = 21.
# Example 3:

# Input: nums1 = [-1,-1], nums2 = [1,1]
# Output: -1
# Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
# Their dot product is -1.

class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        # Initialize DP table
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)] #dp[i][j] represents max dot product using first i elements of nums1 and first j elements of nums2

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                product = nums1[i - 1] * nums2[j - 1]
                
                # Choose the maximum among:
                # 1. add both current elements to the dot product
                # 2. only is a new dot product (start new subsequence with current elements)
                # 3. not including this element in nums1 is a max (skipping current element from nums1)
                # 4. not including this element in nums2 is a max (skipping current element from nums2)
                dp[i][j] = max(dp[i - 1][j - 1] + product, product, dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]