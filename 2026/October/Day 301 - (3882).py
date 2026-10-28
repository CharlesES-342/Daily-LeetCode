# 3882. Minimum XOR Path in a Grid

# You are given a 2D integer array grid of size m * n.
# You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).
# At each step, you may move either right or down.
# The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.
# Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).

# Example 1:
# Input: grid = [[1,2],[3,4]]
# Output: 6
# Explanation:
# There are two valid paths:
# (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
# (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6
# The minimum XOR value among all valid paths is 6.

# Example 2:
# Input: grid = [[6,7],[5,8]]
# Output: 9
# Explanation:
# There are two valid paths:
# (0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
# (0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11
# The minimum XOR value among all valid paths is 9.

# Example 3:
# Input: grid = [[2,7,5]]
# Output: 0
# Explanation:
# There is only one valid path:
# (0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0
# The XOR value of this path is 0, which is the minimum possible.

# Constraints:
# 1 <= m == grid.length <= 1000
# 1 <= n == grid[i].length <= 1000
# m * n <= 1000
# 0 <= grid[i][j] <= 1023​

class Solution(object):
    def minCost(self, grid):
        """:type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] will be a set of all possible XOR values reachable at cell (i, j)
        # Using a set to automatically handle duplicates at each cell
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        # Base case: top-left cell
        dp[0][0].add(grid[0][0])
        
        for i in range(m):
            for j in range(n):
                # If there are reachable values at this cell, propagate them right and down
                if not dp[i][j]:
                    continue
                
                current_values = dp[i][j]
                
                # Move Right
                if j + 1 < n:
                    val = grid[i][j + 1]
                    for x in current_values:
                        dp[i][j + 1].add(x ^ val)
                
                # Move Down
                if i + 1 < m:
                    val = grid[i + 1][j]
                    for x in current_values:
                        dp[i + 1][j].add(x ^ val)
                        
        # The answer is the minimum XOR value present in the bottom-right cell
        return min(dp[m - 1][n - 1])


'''
Code formed by Gemini.ai.
Initial thought processes involved looking at each state, but mid way through I realised
that a minimum at a current cell might not result in a minimum at the next cell (or a minimum
overall). So I decided to track all possible XOR values at each cell, and then carry froward
these, but this does result in large spill over into neighbouring cells.
'''

'''
While this solution is correct, it is not efficient.
'''
import numpy as np

class Solution(object):
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        V = 1 << max(max(row) for row in grid).bit_length()  # power of two > max value
        idx = np.arange(V)

        prev = [None] * n
        for i in range(m):
            cur = [None] * n
            for j in range(n):
                s = np.zeros(V, dtype=bool)
                if i == 0 and j == 0:
                    s[grid[0][0]] = True
                else:
                    if i > 0:
                        s |= prev[j]
                    if j > 0:
                        s |= cur[j - 1]
                    s = s[idx ^ grid[i][j]]   # XOR every reachable value by this cell
                cur[j] = s
            prev = cur

        return int(np.flatnonzero(prev[-1])[0])  # smallest reachable XOR

    '''
    This solution is more efficient than the previous one, as it uses a boolean array to track
    reachable XOR values instead of a set, which reduces overhead. The use of numpy allows for
    vectorized operations, improving performance.
    '''