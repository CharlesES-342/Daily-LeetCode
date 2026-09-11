# 3483. Unique 3-Digit Even Numbers

# You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.
# Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

# Example 1:
# Input: digits = [1,2,3,4]
# Output: 12
# Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

# Example 2:
# Input: digits = [0,2,2]
# Output: 2
# Explanation: The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

# Example 3:
# Input: digits = [6,6,6]
# Output: 1
# Explanation: Only 666 can be formed.

# Example 4:
# Input: digits = [1,3,5]
# Output: 0
# Explanation: No even 3-digit numbers can be formed.

# Constraints:
# 3 <= digits.length <= 10
# 0 <= digits[i] <= 9

class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        # there is a max of 999-99 = 900 numbers that can be made (these are all 3 digits)
        total = 0
        # try every posibility
        made = set()
        for pos_i, i in enumerate(digits):
            if i == 0:  # No leading zeros allowed
                continue
            for pos_j, j in enumerate(digits):
                if pos_i == pos_j:
                    continue
                for pos_k, k in enumerate(digits):
                    # the digits cant be the same
                    if pos_i == pos_k or pos_j == pos_k:
                        continue
                    if k % 2 == 0:  # Must be an even number
                        num = i * 100 + j * 10 + k
                        made.add(num)

        return len(made)    