# 3963. Create Grid With Exactly One Path

# You are given two integers m and n, representing the number of rows and columns of a grid.
# Construct any m x n grid consisting only of the characters '.' and '#', where:
# '.' represents a free cell.
# '#' represents an obstacle cell.
# A valid path is a sequence of free cells that:
# Starts at the top-left cell (0, 0).
# Ends at the bottom-right cell (m - 1, n - 1).
# Moves only:
# Right, from (i, j) to (i, j + 1), or
# Down, from (i, j) to (i + 1, j).
# Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell.

# Example 1:
# Input: m = 2, n = 3
# Output: ["..#","#.."]
# Explanation:
# The only valid path is: (0,0) → (0,1) → (1,1) → (1,2)

# Example 2:
# Input: m = 3, n = 3
# Output: ["..#","#..","##."]
# Explanation:
# The only valid path is: (0,0) → (0,1) → (1,1) → (1,2) → (2,2)

# Example 3:
# Input: m = 1, n = 4
# Output: ["...."]
# Explanation:
# The only valid path is: (0,0) → (0,1) → (0,2) → (0,3)

# Constraints:
# 1 <= m, n <= 25

class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        # initialise grid
        grid = [['#' for _ in range(n)] for _ in range(m)]
        
        # right first
        for j in range(n):
            grid[0][j] = '.'
            
        # go down in final column
        for i in range(m):
            grid[i][n - 1] = '.'
            
        # convert to string and combine
        return ["".join(row) for row in grid]