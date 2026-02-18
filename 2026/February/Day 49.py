# 693. Binary Number with Alternating Bits

# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

# Example 1:
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101

# Example 2:
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.

# Example 3:
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.

# Constraints:
# 1 <= n <= 231 - 1

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        xor = n ^ (n >> 1) # n xor n_shifted_by_one
        
        bit_length = n.bit_length()
        for i in range(bit_length - 1):
            if not (xor >> i) & 1: #if there is a 1, there is a match
                return False
        return True
        