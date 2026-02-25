#1975. Maximum Matrix Sum

# You are given an n x n integer matrix. You can do the following operation any number of times:
# Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.

# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.


# Example 1:
# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.

# Example 2:
# Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# Output: 16
# Explanation: We can follow the following step to reach sum equals 16:
# - Multiply the 2 last elements in the second row by -1.


# Constraints:
# n == matrix.length == matrix[i].length
# 2 <= n <= 250
# -105 <= matrix[i][j] <= 105



#attempt 1 - dont need to perform operations, just need to think of whta the end result could look like

#if there are odd numbers of negative numbers, we can make all but one positive, so we need to subtract twice the smallest absolute value
#   (one to not count it (as it is already part of the sum), one to count it as a negative)
#if there are even numbers of negative numbers, we can make all positive (by some combination of operationas)
class Solution:
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total_sum = 0
        negative_count = 0
        min_abs_value = float('inf')

        for row in matrix:
            for value in row:
                abs_value = abs(value)
                total_sum += abs_value
                if value < 0:
                    negative_count += 1
                min_abs_value = min(min_abs_value, abs_value) # Track the smallest absolute value

        # If there is an odd number of negative numbers, we need to subtract twice the smallest absolute value
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs_value

        return total_sum