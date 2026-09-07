# 940. Distinct Subsequences II

# Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.

# Example 1:
# Input: s = "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

# Example 2:
# Input: s = "aba"
# Output: 6
# Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".

# Example 3:
# Input: s = "aaa"
# Output: 3
# Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".

# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase English letters.

class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        total = 0
        dp = [0] * 26

        # go through and determine the number of subsequences that end with c in dp[c]
        # For each new sequence created by c new = total + 1 - dp[c]
        for char in s:
            idx = ord(char) - ord('a') # get index number (a - a = 0)...
            # Distinct sequences formed
            new_seq = total + 1 - dp[idx] % MOD
            # total = (total + new) % MOD
            total = (total + new_seq) % MOD

            # dp[c] = (dp[c] + new) % MOD
            dp[idx] = (dp[idx] + new_seq) % MOD

        return total