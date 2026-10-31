# 3665. Twisted Mirror Path Count

# Given an m x n binary grid grid where:
# grid[i][j] == 0 represents an empty cell, and
# grid[i][j] == 1 represents a mirror.
# A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). It can move only right or down. If the robot attempts to move into a mirror cell, it is reflected before entering that cell:
# If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.
# If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.
# If this reflection would cause the robot to move outside the grid boundaries, the path is considered invalid and should not be counted.
# Return the number of unique valid paths from (0, 0) to (m - 1, n - 1).
# Since the answer may be very large, return it modulo 109 + 7.
# Note: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.

# Example 1:
# Input: grid = [[0,1,0],[0,0,1],[1,0,0]]
# Output: 5
# Explanation:
# Number	Full Path
# 1	(0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2)
# 2	(0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)
# 3	(0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)
# 4	(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)
# 5	(0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)
# [M] indicates the robot attempted to enter a mirror cell and instead reflected.

# Example 2:
# Input: grid = [[0,0],[0,0]]
# Output: 2
# Explanation:
# Number	Full Path
# 1	(0, 0) → (0, 1) → (1, 1)
# 2	(0, 0) → (1, 0) → (1, 1)

# Example 3:
# Input: grid = [[0,1,1],[1,1,0]]
# Output: 1
# Explanation:
# Number	Full Path
# 1	(0, 0) → (0, 1) [M] → (1, 1) [M] → (1, 2)
# (0, 0) → (1, 0) [M] → (1, 1) [M] → (2, 1) goes out of bounds, so it is invalid.

# Constraints:
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 500
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0

'''
Once again, based on the constraints of the day, despite the idea being totaly my own, the
code itself was generated my claude.ai. So, I really want to come back to this again to
do it properly!
'''
class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Pre-compute jumps for each cell, for each move into it (right in or down in), determine the resulting directions, toring the jump targets
        # d[i][j] hold number of ways (% 10**9 + 7) of getting to cell (i,j)

        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # down[c]: ways to leave the cell above in column c heading down
        # right:   ways to leave the cell to the left heading right
        down = [0] * n

        for r in range(m):
            right = 0
            for c in range(n):
                in_right, in_down = right, down[c]

                if (r == 0 and c == 0) or grid[r][c] == 0:
                    # Open cell (the start is always treated as open):
                    # free choice of direction, so both exits get the total.
                    total = 1 if (r == 0 and c == 0) else (in_right + in_down) % MOD
                    right = down[c] = total
                else:
                    # Mirror: entering rightwards exits down, entering downwards exits right.
                    right, down[c] = in_down, in_right

        # Entering a mirror on the last cell deflects you out of the grid -> 0 paths
        if grid[m - 1][n - 1] == 1 and m * n > 1:
            return 0
        return down[n - 1]