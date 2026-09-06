# 115. Distinct Subsequences

# Given two strings s and t, return the number of distinct subsequences of s which equals t.
# The test cases are generated so that the answer fits on a 32-bit signed integer.

# Example 1:
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit

# Example 2:
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag

# Constraints:
# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # number of possible sequences are at most ... for the smaller sequence, check they exist in the other, return that final count
        m, n = len(s), len(t)

        # dp[j] will store the number of distinct subsequences of t[:j] in s[:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty target string t can be formed in 1 way

        for i in range(1, m + 1):
            # Iterate backwards to use the results from the previous step
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]

'''
For eac location at the final letter, iterate forward to find the next letter, and so on.
'''