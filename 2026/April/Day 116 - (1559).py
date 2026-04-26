# 1559. Detect Cycles in 2D Grid

# Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.
# A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.
# Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.
# Return true if any cycle of the same value exists in grid, otherwise, return false.

# Example 1:
# Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# Output: true
# Explanation: There are two valid cycles shown in different colors in the image below:

# Example 2:
# Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# Output: true
# Explanation: There is only one valid cycle highlighted in the image below:

# Example 3:
# Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# Output: false

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid consists only of lowercase English letters

class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        # BFS (if you can go to the next node which has already been viewed, a cycle is possible)
        # then check if length >=4
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c, pr, pc):
            visited[r][c] = True
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                # skip out of bounds and different characters
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if grid[nr][nc] != grid[r][c]:
                    continue
                # skip the cell we just came from (prevents false cycle a->b->a)
                if nr == pr and nc == pc:
                    continue
                # if already visited and same char = cycle found
                if visited[nr][nc]:
                    return True
                if dfs(nr, nc, r, c):
                    return True
            return False

        for r in range(m):
            for c in range(n):
                if not visited[r][c]:
                    if dfs(r, c, -1, -1):
                        return True
        return False
    
    # once again, not my code by my idea. Want to come back to this (same time constraints as yesterday
    # , not fair)