# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading
# zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
# Given a string n that represents a positive decimal integer, return the minimum number of positive
# deci-binary numbers needed so that they sum up to n.


# Example 1:
# Input: n = "32"
# Output: 3
# Explanation: 10 + 11 + 11 = 32

# Example 2:
# Input: n = "82734"
# Output: 8

# Example 3:
# Input: n = "27346209830709182346"
# Output: 9

# Constraints:
# 1 <= n.length <= 105
# n consists of only digits.
# n does not contain any leading zeros and represents a positive integer.
class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        #break doiwn teh numnber into its 100's, 10's ... and combine them into a combination that removes the need for elading 0's
        #find where the maximum digit is, and then build based on that

        #baed on this logic, the count is simply the largest value in a position of 10's, 1's or 100's ...
        return int(max(n))
    

#This problem was way easier than I was expecting.
#I thought I was loosing my mind with how easy it seemed, and that for a 'MEDIUM' problem,
#how could i solve it in 11 characters