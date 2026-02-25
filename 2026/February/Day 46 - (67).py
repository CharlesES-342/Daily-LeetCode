# 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.


# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def toDecimal(binary):
            n = len(binary)
            total = 0
            for i in range(n):
                if binary[i] == '1':
                    total += 2**(n - 1 - i)
            return total
        
        decimal_sum = toDecimal(a) + toDecimal(b)
        return bin(decimal_sum)[2:]  # [2:] removes the '0b' prefix