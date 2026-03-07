# 1888. Minimum Number of Flips to Make the Binary String Alternating

# You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:
# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.
# The string is called alternating if no two adjacent characters are equal.
# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

# Example 1:
# Input: s = "111000"
# Output: 2
# Explanation: Use the first operation two times to make s = "100011".
# Then, use the second operation on the third and sixth elements to make s = "101010".

# Example 2:
# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating.

# Example 3:
# Input: s = "1110"
# Output: 1
# Explanation: Use the second operation on the second element to make s = "1010".

# Constraints:
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.

class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # Double the string to simulate all possible Type 1 rotations (allows all combinations to be formed later on)
        s = s + s
        
        # Targets for the doubled string
        target1 = ""
        target2 = ""
        for i in range(len(s)):
            target1 += "0" if i % 2 == 0 else "1"
            target2 += "1" if i % 2 == 0 else "0"
            
        res = float('inf')
        diff1, diff2 = 0, 0
        l = 0
        
        for r in range(len(s)):
            # Add the new character's difference to the counts
            if s[r] != target1[r]:
                diff1 += 1
            if s[r] != target2[r]:
                diff2 += 1
            
            # When the window size exceeds n, slide the left pointer
            if (r - l + 1) > n:
                if s[l] != target1[l]:
                    diff1 -= 1
                if s[l] != target2[l]:
                    diff2 -= 1
                l += 1
            
            # Once we have a valid window of size n, track the minimum flips
            if (r - l + 1) == n:
                res = min(res, diff1, diff2)
                
        return res