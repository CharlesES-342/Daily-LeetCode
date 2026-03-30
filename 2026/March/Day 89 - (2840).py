# 2840. Check if Strings Can be Made Equal With Operations II

# You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.
# You can apply the following operation on any of the two strings any number of times:
# Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.

# Example 1:
# Input: s1 = "abcdba", s2 = "cabdab"
# Output: true
# Explanation: We can apply the following operations on s1:
# - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
# - Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
# - Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.

# Example 2:
# Input: s1 = "abe", s2 = "bea"
# Output: false
# Explanation: It is not possible to make the two strings equal.

# Constraints:
# n == s1.length == s2.length
# 1 <= n <= 105
# s1 and s2 consist only of lowercase English letters.

class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)
        
        if n1 != n2:
            return False

        #only need to check if the odds are teh same and if the evens are the
        #   if the odds are not then it will never be possible (positions matter)
        #   if the evens are the same, then it could be possible (all posiitons are swappable)
        evens_match = sorted(s1[0::2]) == sorted(s2[0::2])
        odds_match = sorted(s1[1::2]) == sorted(s2[1::2])
        return evens_match and odds_match

        