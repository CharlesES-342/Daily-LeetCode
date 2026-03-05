# 1758. Minimum Changes To Make Alternating Binary String

# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string
# "0100" is not.
# Return the minimum number of operations needed to make s alternating.


# Example 1:
# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.

# Example 2:
# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.

# Example 3:
# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".

# Constraints:
# 1 <= s.length <= 104
# s[i] is either '0' or '1'.


class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        #either '0' in position 1 or in position 2
        #count through and check the bits (if it is wrong count this)
        #   only need 1 pass, if it fufills one condition, the other is not fulfilled
        #min(of the 2 counts) = answer
        n = len (s)
        swap = 0
        alt = '0'
        for i in s:
            if alt == '1':
                if i == '0':
                    swap += 1
                alt = '0'
            elif alt == '0':
                if i == '1':
                    swap += 1
                alt = '1'
        
        return min(swap, n-swap)


        