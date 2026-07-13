# 1291. Sequential Digits

# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

# Example 1:
# Input: low = 100, high = 300
# Output: [123,234]

# Example 2:
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
 

# Constraints:
# 10 <= low <= high <= 10^9

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ans = []
        digits = "123456789" #max valid sequnce is 123456789, min being 0
        
        # Determine the minimum and maximum possible lengths of the target numbers
        min_len = len(str(low))
        max_len = len(str(high))
        
        # go through all possible window sizes (for valid numbers)
        for length in range(min_len, max_len + 1):
            # get the window value and compair to the valid range
            for start in range(10 - length):
                substring = digits[start : start + length]
                num = int(substring)
                
                if low <= num <= high:
                    ans.append(num)
                    
        return ans