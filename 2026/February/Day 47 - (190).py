# 190. Reverse Bits

# Reverse bits of a given 32 bits signed integer.

# Example 1:
# Input: n = 43261596
# Output: 964176192
# Explanation:
# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000

# Example 2:
# Input: n = 2147483644
# Output: 1073741822

# Explanation:
# Integer	Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110

# Constraints:
# 0 <= n <= 231 - 2
# n is even.

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        #convert to binary string (32 bits, padded with zeros)
        binary_str = bin(n)[2:].zfill(32)
        
        #reverse the binary string
        reversed_binary = binary_str[::-1]
        
        # Convert back to integer
        return int(reversed_binary, 2)
    
#knew exactly how to do it, but wanted to find a way that waws more efficient in terms of code quantity.
#asked claud to make my code simpler, and this was the result