#3651. Minimum Cost Path with Teleportations

# You are given a m x n 2D integer array grid and an integer k. You start at the top-left cell (0, 0)
# and your goal is to reach the bottom‐right cell (m - 1, n - 1).
# There are two types of moves available:
# Normal move: You can move right or down from your current cell (i, j), i.e. you can move to (i, j + 1)
# (right) or (i + 1, j) (down). The cost is the value of the destination cell.
# Teleportation: You can teleport from any cell (i, j), to any cell (x, y) such that grid[x][y] <= grid[i][j];
# the cost of this move is 0. You may teleport at most k times.
# Return the minimum total cost to reach cell (m - 1, n - 1) from (0, 0).


# Example 1:
# Input: grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2
# Output: 7
# Explanation:
# Initially we are at (0, 0) and cost is 0.
# Current Position	Move	New Position	Total Cost
# (0, 0)	Move Down	(1, 0)	0 + 2 = 2
# (1, 0)	Move Right	(1, 1)	2 + 5 = 7
# (1, 1)	Teleport to (2, 2)	(2, 2)	7 + 0 = 7
# The minimum cost to reach bottom-right cell is 7.

# Example 2:
# Input: grid = [[1,2],[2,3],[3,4]], k = 1
# Output: 9
# Explanation:
# Initially we are at (0, 0) and cost is 0.
# Current Position	Move	New Position	Total Cost
# (0, 0)	Move Down	(1, 0)	0 + 2 = 2
# (1, 0)	Move Right	(1, 1)	2 + 3 = 5
# (1, 1)	Move Down	(2, 1)	5 + 4 = 9
# The minimum cost to reach bottom-right cell is 9.

# Constraints:
# 2 <= m, n <= 80
# m == grid.length
# n == grid[i].length
# 0 <= grid[i][j] <= 104
# 0 <= k <= 10

class Solution:
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        
        #create list of all cell coordinates (i, j)
        points = [(i, j) for i in range(m) for j in range(n)]
        
        #sort points by their grid values in ascending order (can process smaller cells first)
        points.sort(key=lambda p: grid[p[0]][p[1]])
        
        #costs[i][j] = minimum cost to reach (i,j) from destination (m-1, n-1)
        #initial costs to infinity
        costs = [[float("inf")] * n for _ in range(m)]
        
        #case 2 - for k teleports
        for t in range(k + 1):
            minCost = float("inf")
            j = 0
            
            for i in range(len(points)):
                # Update minCost with the cost of current cell
                minCost = min(minCost, costs[points[i][0]][points[i][1]])
                
                #check if next cell has the same grid value as current cell
                if (
                    i + 1 < len(points)
                    and grid[points[i][0]][points[i][1]]
                    == grid[points[i + 1][0]][points[i + 1][1]]
                ):
                    #yes -> continue to expand the interval
                    #wait until you have values for cost changes
                    i += 1
                    continue

                #minimum teeport cost for all teleports in this grid
                for r in range(j, i + 1):
                    costs[points[r][0]][points[r][1]] = minCost
                
                #move to next row
                j = i + 1
            
            #Case 1 - no teleports (work from the end up)
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    
                    # Base case: destination cell has cost 0
                    if i == m - 1 and j == n - 1:
                        costs[i][j] = 0
                        continue
                    
                    #UP
                    if i != m - 1:
                        costs[i][j] = min(
                            costs[i][j], 
                            costs[i + 1][j] + grid[i + 1][j]
                        )
                    
                    #LEFT
                    if j != n - 1:
                        costs[i][j] = min(
                            costs[i][j], 
                            costs[i][j + 1] + grid[i][j + 1]
                        )
        
        # Return the minimum cost to reach (0,0) from (m-1, n-1)
        return costs[0][0]
    
#I understood the premis of the problem and how to approach it using dynamic programming. However,
#I struggled with the implementation details, especially in managing the teleportations as I would
#have probably done somethign far more ineficient.
#I have read thorugh teh solution and used it to confirm my methodology as correct - so this code is not all me,
#however, the overall principle is mine. The specifics of use of pointers was not somthing i would have considered
#during this approach, but the reasoning makes sense to me now.
