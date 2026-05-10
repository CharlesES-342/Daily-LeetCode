# 1914. Cyclically Rotating a Grid

# You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.
# The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:
# A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:
# Return the matrix after applying k cyclic rotations to it.

# Example 1:
# Input: grid = [[40,10],[30,20]], k = 1
# Output: [[10,20],[40,30]]
# Explanation: The figures above represent the grid at every state.

# Example 2:
# Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
# Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
# Explanation: The figures above represent the grid at every state.

# Constraints:
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 50
# Both m and n are even integers.
# 1 <= grid[i][j] <= 5000
# 1 <= k <= 109


class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # extract the layer as an array
        # perform the move
        # add all the layers back together by re-assigning the original
        m = len(grid)
        n = len(grid[0])
        num_layers = min(m, n) // 2

        for layer in range(num_layers):
            # Define boundaries for the current layer
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer
            
            # 1. Extract elements in counter-clockwise order
            elements = []
            
            # Top row (left to right)
            for j in range(left, right + 1):
                elements.append(grid[top][j])
            # Right column (top to bottom)
            for i in range(top + 1, bottom + 1):
                elements.append(grid[i][right])
            # Bottom row (right to left)
            for j in range(right - 1, left - 1, -1):
                elements.append(grid[bottom][j])
            # Left column (bottom to top)
            for i in range(bottom - 1, top, -1):
                elements.append(grid[i][left])
            
            # 2. Calculate effective rotation (incase it is more than the size, you only do what is necessary)
            L = len(elements)
            net_rotation = k % L
            
            # add those before after the end
            rotated = elements[net_rotation:] + elements[:net_rotation]
            
            # 3. Put elements back into the grid
            idx = 0
            # Top row
            for j in range(left, right + 1):
                grid[top][j] = rotated[idx]
                idx += 1
            # Right column
            for i in range(top + 1, bottom + 1):
                grid[i][right] = rotated[idx]
                idx += 1
            # Bottom row
            for j in range(right - 1, left - 1, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1
            # Left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1
                
        return grid