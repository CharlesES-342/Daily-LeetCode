# 3742. Maximum Path Score in a Grid

# You are given an m x n grid where each cell contains one of the values 0, 1, or 2. You are also given an integer k.
# You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.
# Each cell contributes a specific score and incurs an associated cost, according to their cell values:
# 0: adds 0 to your score and costs 0.
# 1: adds 1 to your score and costs 1.
# 2: adds 2 to your score and costs 1. ​​​​​​​
# Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.
# Note: If you reach the last cell but the total cost exceeds k, the path is invalid.

# Example 1:
# Input: grid = [[0, 1],[2, 0]], k = 1
# Output: 2
# Explanation:​​​​​​​
# The optimal path is:
# Cell	grid[i][j]	Score	Total
# Score	Cost	Total
# Cost
# (0, 0)	0	0	0	0	0
# (1, 0)	2	2	2	1	1
# (1, 1)	0	0	2	0	1
# Thus, the maximum possible score is 2.

# Example 2:
# Input: grid = [[0, 1],[1, 2]], k = 1
# Output: -1
# Explanation:
# There is no path that reaches cell (1, 1)​​​​​​​ without exceeding cost k. Thus, the answer is -1.

# Constraints:
# 1 <= m, n <= 200
# 0 <= k <= 103​​​​​​​
# ​​​​​​​grid[0][0] == 0
# 0 <= grid[i][j] <= 2
class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        # Initialize DP table with -1
        # dp[r][c][cost] = max_score
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        
        # Starting point (0, 0)
        start_val = grid[0][0]
        start_cost = 0 if start_val == 0 else 1
        
        if start_cost <= k:
            dp[0][0][start_cost] = start_val
        else:
            return -1

        for r in range(m):
            for c in range(n):
                curr_val = grid[r][c]
                curr_cost = 0 if curr_val == 0 else 1
                
                for prev_cost in range(k + 1):
                    if dp[r][c][prev_cost] == -1:
                        continue
                    
                    # Current score at this state
                    current_score = dp[r][c][prev_cost]
                    
                    # Try moving Down
                    if r + 1 < m:
                        next_val = grid[r+1][c]
                        next_cost = prev_cost + (0 if next_val == 0 else 1)
                        if next_cost <= k:
                            dp[r+1][c][next_cost] = max(dp[r+1][c][next_cost], current_score + next_val)
                            
                    # Try moving Right
                    if c + 1 < n:
                        next_val = grid[r][c+1]
                        next_cost = prev_cost + (0 if next_val == 0 else 1)
                        if next_cost <= k:
                            dp[r][c+1][next_cost] = max(dp[r][c+1][next_cost], current_score + next_val)

        # Find the maximum score in the last cell for any cost <= k
        max_total_score = -1
        for c in range(k + 1):
            max_total_score = max(max_total_score, dp[m-1][n-1][c])
            
        return max_total_score
    
    # I didnt write the code, but i wrote this exact how to in code/words, just didnf fill it in.
    # I know exactly how it works and why and thought of it on my own :)