# 1391. Check if There is a Valid Path in a Grid

# You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:
# 1 which means a street connecting the left cell and the right cell.
# 2 which means a street connecting the upper cell and the lower cell.
# 3 which means a street connecting the left cell and the lower cell.
# 4 which means a street connecting the right cell and the lower cell.
# 5 which means a street connecting the left cell and the upper cell.
# 6 which means a street connecting the right cell and the upper cell.
# You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.
# Notice that you are not allowed to change any street.
# Return true if there is a valid path in the grid or false otherwise.

# Example 1:
# Input: grid = [[2,4,3],[6,5,2]]
# Output: true
# Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).

# Example 2:
# Input: grid = [[1,2,1],[1,2,1]]
# Output: false
# Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)

# Example 3:
# Input: grid = [[1,1,2]]
# Output: false
# Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# 1 <= grid[i][j] <= 6
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        # follow the path (if you run into a stree that is not valid, it fails (or if it loops))
        n, m = len(grid), len(grid[0])
        
        # Mapping pipe types to compatible directions (row_offset, col_offset)
        # 1: horizontal, 2: vertical, 3: left-down, 4: right-down, 5: left-up, 6: right-up
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        visited = set()

        def dfs(r, c):
            if r == n - 1 and c == m - 1:
                return True
            
            visited.add((r, c))
            
            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc
                
                # Check bounds - still in grid
                # Check if already visited - loop (shouldnt happen unless you end back at (0,0) as there are no forks in the road
                #  Check if the next pipe actually connects BACK to this one (you dont drive into a wall)
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                    if (-dr, -dc) in directions[grid[nr][nc]]:
                        if dfs(nr, nc):
                            return True
            return False

        return dfs(0, 0)