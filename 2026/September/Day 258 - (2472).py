# 2472. Maximum Number of Non-overlapping Palindrome Substrings

# You are given a string s and a positive integer k.
# Select a set of non-overlapping substrings from the string s that satisfy the following conditions:
# The length of each substring is at least k.
# Each substring is a palindrome.
# Return the maximum number of substrings in an optimal selection.
# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: s = "abaccdbbd", k = 3
# Output: 2
# Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
# It can be shown that we cannot find a selection with more than two valid substrings.

# Example 2:
# Input: s = "adbcda", k = 2
# Output: 0
# Explanation: There is no palindrome substring of length at least 2 in the string.

# Constraints:
# 1 <= k <= s.length <= 2000
# s consists of lowercase English letters.

class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # dp[i] answer for the prefix[0..i]
        # for each there are 3 operations:
        #   1.skip the character (dp[i] = dp[i-1])
        #   2.found palindrome of length k (dp[i] = max(dp[i], dp[i-k]+1))
        #   3.found palindrome of length k+1
        #       if s[i-k-1...i-1] is a palindrome, dp[i] = max(dp[i], dp[i-k-1]+1)
        # return dp[n-1]
        
        n = len(s)
        dp = [0] * (n + 1)

        # Helper Function: chekc it is a palindrome
        def is_palendrome(l, r):
            '''
            Args: left_pointer, right_pointer
            Return: True is an array is a palendrome
            '''
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        for i in range(1, n + 1):
            # Base Case:
            dp[i] = dp[i - 1]

            # Case 2: check if a valid palandrome exists
            if i >= k and is_palendrome(i-k, i-1):
                dp[i] = max(dp[i], dp[i-k]+1)

            # Case 3: valid palindrome of length k+1
            if i >= k+1 and is_palendrome(i-k-1, i-1):
                dp[i] = max(dp[i], dp[i-k-1]+1)

        return dp[n]


'''
Following submitting this, I had a look at other peoples code and one of the more efficiet appraoches
uses a Greedy Approach, rather than using Dynamic Programming.
The following is the someone elses attempt usin this greedy approach:
'''

class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        ans = 0
        #ensure no overlap
        last_end = -1

        for i in range(n):
            # check palindrome of length k ending at index i
            #end - start + 1
            # we want to end at i because we want the earliest possible to be found
            # this ensures we get the max number of palindromes
            start_k = i - k + 1
            #checks bounds
            # (a full k can fit and is not overlapping where the last palindrome was found) 
            if start_k >= 0 and start_k > last_end:
                #palindrome check
                if s[start_k : i + 1] == s[start_k : i + 1][::-1]:
                    ans += 1
                    last_end = i
                    continue

            # 2. Check palindrome of length k + 1 ending at index i
            start_k1 = i - k
            if start_k1 >= 0 and start_k1 > last_end:
                if s[start_k1 : i + 1] == s[start_k1 : i + 1][::-1]:
                    ans += 1
                    last_end = i

        return ans