# 1545. Find Kth Bit in Nth Binary String

# Given two positive integers n and k, the binary string Sn is formed as follows:
# S1 = "0"
# Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
# Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).
# For example, the first four strings in the above sequence are:
# S1 = "0"
# S2 = "011"
# S3 = "0111001"
# S4 = "011100110110001"
# Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

# Example 1:
# Input: n = 3, k = 1
# Output: "0"
# Explanation: S3 is "0111001".
# The 1st bit is "0".

# Example 2:
# Input: n = 4, k = 11
# Output: "1"
# Explanation: S4 is "011100110110001".
# The 11th bit is "1".

# Constraints:
# 1 <= n <= 20
# 1 <= k <= 2n - 1

class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        #base Case: S1 = "0"
        if n == 1:
            return "0"
        
        # Calculate length of Sn: 2^n - 1
        length = (1 << n) - 1
        mid = (length // 2) + 1
        
        if k == mid:
            return "1"  # The middle bit is always "1"
        elif k < mid:
            # If k is in the left half, it's the same as the kth bit in Sn-1
            return self.findKthBit(n - 1, k)
        else:
            # If k is in the right half, it's the reverse-inverted 
            # version of a bit from the left half.
            # Mirror position from the right: length - k + 1
            corresponding_bit = self.findKthBit(n - 1, length - k + 1)
            return "1" if corresponding_bit == "0" else "0"
        
#while the code is not mine, the ideas of using recusion to form the binary string as well as the  fact that there is a mid point that is a 1 was my own approach
#this is an O(n) solution