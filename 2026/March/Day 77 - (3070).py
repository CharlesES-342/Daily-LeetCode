# 3070. Count Submatrices with Top-Left Element and Sum Less Than k

# You are given a 0-indexed integer matrix grid and an integer k.
# Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.

# Example 1:
# Input: grid = [[7,6,3],[6,6,1]], k = 18
# Output: 4
# Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.

# Example 2:
# Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
# Output: 6
# Explanation: There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.

# Constraints:
# m == grid.length 
# n == grid[i].length
# 1 <= n, m <= 1000 
# 0 <= grid[i][j] <= 1000
# 1 <= k <= 109

class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        valid_subarrays = 0
        
        # build 2D Prefix Sum Matrix
        # P[r][c] stores the sum of the rectangle from (0,0) to (r,c) -> cumulitively store the sum
        P = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                # Standard 2D prefix sum formula
                P[r+1][c+1] = grid[r][c] + P[r][c+1] + P[r+1][c] - P[r][c]
                
                # Since every submatrix MUST start at (0,0), 
                # P[r+1][c+1] IS the total sum of that submatrix.
                if P[r+1][c+1] <= k:
                    valid_subarrays += 1
                else:
                    # Optimization: Since grid values are non-negative (0-1000),
                    # if the sum exceeds k, any larger submatrix 
                    # extending further right in this row will also exceed k.
                    break 

        return valid_subarrays
    
# initially, I forgot that it har to include the top-left element (0,0) so was doing based on the change in cumulitive points based
# on a top-left and bottom-right point 