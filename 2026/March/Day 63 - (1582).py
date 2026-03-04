# 1582. Special Positions in a Binary Matrix

# Given an m x n binary matrix mat, return the number of special positions in mat.
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i
# and column j are 0 (rows and columns are 0-indexed).

# Example 1:
# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

# Example 2:
# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

# Constraints
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] is either 0 or 1.

class Solution(object):
    def numSpecial(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        #pre-calculate the number of 1s in each row and column
        row_count = [sum(row) for row in mat]
        col_count = [sum(mat[r][c] for r in range(rows)) for c in range(cols)]
        
        special_count = 0
        
        #check each cell that contains a 1
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    # If this is the ONLY 1 in its row and column
                    if row_count[r] == 1 and col_count[c] == 1:
                        special_count += 1
                        
        return special_count