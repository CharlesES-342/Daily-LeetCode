# 2812. Find the Safest Path in a Grid

# You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:
# A cell containing a thief if grid[r][c] = 1
# An empty cell if grid[r][c] = 0
# You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.
# The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.
# Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).
# An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.
# The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

# Example 1:
# Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
# Output: 0
# Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).

# Example 2:
# Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
# Output: 2
# Explanation: The path depicted in the picture above has a safeness factor of 2 since:
# - The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
# It can be shown that there are no other paths with a higher safeness factor.

# Example 3:
# Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
# Output: 2
# Explanation: The path depicted in the picture above has a safeness factor of 2 since:
# - The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
# - The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
# It can be shown that there are no other paths with a higher safeness factor.

# Constraints:
# 1 <= grid.length == n <= 400
# grid[i].length == n
# grid[i][j] is either 0 or 1.
# There is at least one thief in the grid.

from collections import deque

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0])

        # 1. Multi-Source BFS to populate the distance matrix
        def BFS(sources):
            '''
            :type sources: list[tuple]
            :rtype: None (updates the dist matrix in-place)
            '''
            queue = deque()
            
            # Initialize the queue with all thieves and set their distance to 0
            for r, c in sources:
                dist[r][c] = 0
                queue.append((r, c))
            
            # Directions for moving up, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If the neighbor is within bounds and hasn't been visited yet
                    if 0 <= nr < rows and 0 <= nc < columns:
                        if dist[nr][nc] == float('inf'):
                            # The distance to the closest thief is the current cell's distance + 1
                            dist[nr][nc] = dist[r][c] + 1
                            queue.append((nr, nc))

        # Find the thieves (where the value in the grid is 1)
        thiefs = []
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    thiefs.append((r, c))

        # Initialise distance matrix with infinity to track unvisited cells easily
        dist = [[float('inf')] * columns for _ in range(rows)]
        
        # Populate the distance matrix from all thieves
        BFS(thiefs)

        # 2. Implementing Dijkstras to determine a path of maximum safeness
        # Always try and move in hte direction of highest value of safeness

        import heapq

        # Base Case: If the start or end has a thief, safeness factor is instantly 0
        if dist[0][0] == 0 or dist[rows-1][columns-1] == 0:
            return 0

        # Max-Heap stores: (-safeness_of_path, r, c)
        # We start with the safeness value of the starting cell itself
        max_heap = [(-dist[0][0], 0, 0)]
        
        # Track the maximum safeness found to reach any cell
        max_safeness = [[-1] * columns for _ in range(rows)]
        max_safeness[0][0] = dist[0][0]
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while max_heap:
            current_safe, r, c = heapq.heappop(max_heap)
            current_safe = -current_safe # Convert back to positive
            
            # If we reached the destination, this is our maximum bottleneck path
            # all other paths will be atmos equal to this path (we dont need the best route to all nodes, just the end node/gid location)
            if r == rows - 1 and c == columns - 1:
                return current_safe
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < columns:
                    # The safeness of the path is limited by the smallest distance to a thief previously, as well as in this next step
                    path_safe = min(current_safe, dist[nr][nc])
                    
                    # If we found a safer way to reach (nr, nc), update and push to heap
                    if path_safe > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = path_safe
                        heapq.heappush(max_heap, (-path_safe, nr, nc))
                        
        return 0