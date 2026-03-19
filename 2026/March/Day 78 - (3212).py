# 3212. Count Submatrices With Equal Frequency of X and Y

# Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:
# grid[0][0]
# an equal frequency of 'X' and 'Y'.
# at least one 'X'.


# Example 1:
# Input: grid = [["X","Y","."],["Y",".","."]]
# Output: 3


# Example 2:
# Input: grid = [["X","X"],["X","Y"]]
# Output: 0
# Explanation:
# No submatrix has an equal frequency of 'X' and 'Y'.

# Example 3:
# Input: grid = [[".","."],[".","."]]
# Output: 0
# Explanation:
# No submatrix has at least one 'X'.

# Constraints:
# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 'X', 'Y', or '.'.

class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        # dp_sum stores the balance of X and Y
        dp_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        # dp_x stores the count of 'X' encountered
        dp_x = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                #current cell value
                val = 1 if grid[r][c] == 'X' else (-1 if grid[r][c] == 'Y' else 0)
                x_val = 1 if grid[r][c] == 'X' else 0
                
                # add the weight of the subarray (its current state - valid or not)
                dp_sum[r+1][c+1] = val + dp_sum[r][c+1] + dp_sum[r+1][c] - dp_sum[r][c]
                
                # add the number of x's found in the subarray
                dp_x[r+1][c+1] = x_val + dp_x[r][c+1] + dp_x[r+1][c] - dp_x[r][c]
                
                # validate the subarray: balance is 0 (same number of x's and y's) AND at least one 'X'
                if dp_sum[r+1][c+1] == 0 and dp_x[r+1][c+1] > 0:
                    count += 1
                    
        return count