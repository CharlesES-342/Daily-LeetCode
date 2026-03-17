# 1727. Largest Submatrix With Rearrangements

# You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.
# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

# Example 1:
# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.

# Example 2:
# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.

# Example 3:
# Input: matrix = [[1,1,0],[1,0,1]]
# Output: 2
# Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.


# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m * n <= 105
# matrix[i][j] is either 0 or 1.

class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        #biggest area given any column order
        # arrange it such that you can get as many 1's next to eachother
        # order does not matter

        #1. find the howmany 1's are ineach row (at each end location)
        #2. re arrange into order (so there is the max size first)
        #3. calculate the resulting possible areas (return the largest on)
        
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(1, rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r-1][c]

        # now rearrange and calculate the largest possiblearea
        ans = 0
        for r in range(rows):
            curr_row = sorted(matrix[r], reverse=True)
            for c in range(cols):
                    height = curr_row[c]
                    width = c + 1
                    ans = max(ans, height * width)
        
        return ans
