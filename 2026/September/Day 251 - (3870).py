# 3870. Count Commas in Range

# You are given an integer n.
# Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
# In standard formatting:
# A comma is inserted after every three digits from the right.
# Numbers with fewer than 4 digits contain no commas.

# Example 1:
# Input: n = 1002
# Output: 3
# Explanation:
# The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

# Example 2:
# Input: n = 998
# Output: 0
# Explanation:
# All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

# Constraints:
# 1 <= n <= 105

class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = str(n)
        if len(num) < 4:
            return 0
        else:
            # the max value is 100,000 (10^5)
            # the min value of importance is 1,000
            # for each there are only 1 comma
            # remove the numbers 0-999 from the consideration, and add 1 for every remaining number
            return n - 999

''' similarly: removing convertions to string types'''

class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        return max(0,n-999)
        