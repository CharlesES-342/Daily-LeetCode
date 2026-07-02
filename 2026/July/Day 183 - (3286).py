# 3286. Find a Safe Walk Through a Grid

# You are given an m x n binary matrix grid and an integer health.
# You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).
# You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.
# Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.
# Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

# Example 1:
# Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1
# Output: true
# Explanation:
# The final cell can be reached safely by walking along the gray cells below.

# Example 2:
# Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3
# Output: false
# Explanation:
# A minimum of 4 health points is needed to reach the final cell safely.

# Example 3:
# Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5
# Output: true
# Explanation:
# The final cell can be reached safely by walking along the gray cells below.
# Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 2 <= m * n
# 1 <= health <= m + n
# grid[i][j] is either 0 or 1.

class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        # Dijstras but with a route consisting a minimum health reduction is best
        # If by the end, the minimum route weight is greater than yuor health, then it is not possible

        m, n = len(grid), len(grid[0])
        
        # Directions for moving up, down, left, and right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Min-heap stores tuples of (health_lost, row, col)
        # Starting at (0, 0), the initial health lost is the value of grid[0][0]
        start_loss = grid[0][0]
        min_heap = [(start_loss, 0, 0)]
        
        # Track the minimum health cost to reach each cell
        # Initialise with infinity for all cells
        min_cost = [[float('inf')] * n for _ in range(m)]
        min_cost[0][0] = start_loss
        
        while min_heap:
            current_loss, r, c = heapq.heappop(min_heap)
            
            # If we reached the destination, check if we survive
            if r == m - 1 and c == n - 1:
                return current_loss < health
            
            # If we found a worse path to an already processed cell, skip it
            if current_loss > min_cost[r][c]:
                continue
                
            # Explore neighbours
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    # The cost to move to the neighbour is the current loss + neighbour's grid value
                    next_loss = current_loss + grid[nr][nc]
                    
                    # If this path is cheaper than any previously found path to (nr, nc)
                    if next_loss < min_cost[nr][nc]:
                        min_cost[nr][nc] = next_loss
                        heapq.heappush(min_heap, (next_loss, nr, nc))
                        
        # If the destination is unreachable
        return False
        