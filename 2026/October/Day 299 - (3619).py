# 3619. Count Islands With Total Value Divisible by K

# You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).
# The total value of an island is the sum of the values of all cells in the island.
# Return the number of islands with a total value divisible by k.

# Example 1:
# Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5
# Output: 2
# Explanation:
# The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

# Example 2:
# Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3
# Output: 6
# Explanation:
# The grid contains six islands, each with a total value that is divisible by 3.

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# 0 <= grid[i][j] <= 106
# 1 <= k <= 106

class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Get sizes
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Base case: if the cell goes out of bounds or hits water (0), return 0
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            # Save the current land value and set it to 0 to mark it as visited
            val = grid[r][c]
            grid[r][c] = 0
            
            # Recursively explore all 4 directions (down, up, right, left) 
            # and sum up their values along with the current cell's value
            return val + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        # Counter for islands whose total value is divisible by k
        valid_islands_count = 0
        
        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # When we find unvisited land (> 0), start a DFS to find the total island sum
                if grid[r][c] > 0:
                    total_island_value = dfs(r, c)
                    
                    # Check if the total island value is divisible by k
                    if total_island_value % k == 0:
                        valid_islands_count += 1
                        
        return valid_islands_count
    

'''
Alternatavely, a DFS by se of a queue ratehr than recursion could be used.
'''