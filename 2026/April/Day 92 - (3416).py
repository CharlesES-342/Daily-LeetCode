# 3418. Maximum Amount of Money Robot Can Earn

# You are given an m x n grid. A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). The robot can move either right or down at any point in time.
# The grid contains a value coins[i][j] in each cell:
# If coins[i][j] >= 0, the robot gains that many coins.
# If coins[i][j] < 0, the robot encounters a robber, and the robber steals the absolute value of coins[i][j] coins.
# The robot has a special ability to neutralize robbers in at most 2 cells on its path, preventing them from stealing coins in those cells.
# Note: The robot's total coins can be negative.
# Return the maximum profit the robot can gain on the route.

# Example 1:
# Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
# Output: 8
# Explanation:
# An optimal path for maximum coins is:
# Start at (0, 0) with 0 coins (total coins = 0).
# Move to (0, 1), gaining 1 coin (total coins = 0 + 1 = 1).
# Move to (1, 1), where there's a robber stealing 2 coins. The robot uses one neutralization here, avoiding the robbery (total coins = 1).
# Move to (1, 2), gaining 3 coins (total coins = 1 + 3 = 4).
# Move to (2, 2), gaining 4 coins (total coins = 4 + 4 = 8).

# Example 2:
# Input: coins = [[10,10,10],[10,10,10]]
# Output: 40
# Explanation:
# An optimal path for maximum coins is:
# Start at (0, 0) with 10 coins (total coins = 10).
# Move to (0, 1), gaining 10 coins (total coins = 10 + 10 = 20).
# Move to (0, 2), gaining another 10 coins (total coins = 20 + 10 = 30).
# Move to (1, 2), gaining the final 10 coins (total coins = 30 + 10 = 40).

# Constraints:
# m == coins.length
# n == coins[i].length
# 1 <= m, n <= 500
# -1000 <= coins[i][j] <= 1000

class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        # from each location,  move in each direction
        # add the value to a max array which tracks the max pay and k robbers (dp[i][j][k])
        rows = len(coins)
        cols = len(coins[0])
        
        inf = float('inf')
        dp = [[[-inf] * 3 for _ in range(cols)] for _ in range(rows)]
        
        # initial start location
        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = max(coins[0][0], 0)
        dp[0][0][2] = max(coins[0][0], 0)

        #move thorugh the array
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                
                current_val = coins[i][j]
                #go thorugh each neutralisation state none, 1 and 2
                for k in range(3):
                    # move down
                    if i > 0:
                        # take the coin value (could be robbed)
                        if dp[i-1][j][k] != -inf:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + current_val)
                        
                        # neutralize this coin (requires k > 0)
                        if k > 0 and dp[i-1][j][k-1] != -inf:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])

                    # move right
                    if j > 0:
                        # take the coin value (could be robbed)
                        if dp[i][j-1][k] != -inf:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + current_val)
                        
                        # neutralise teh coin value (requires k > 0)
                        if k > 0 and dp[i][j-1][k-1] != -inf:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
                            
        #return the max value of the bottom-right cell
        return max(dp[rows-1][cols-1])
        
        
# I did not write the code becuase I simply could not be bothered, however I understood
# all principles used becuase I asked for them secifically when prompting gemini.ai.
# It returned something that was exactly as I wanted. I understood how to do the question,
# just couldnt be bothered thismorning :(