# 1536. Minimum Swaps to Arrange a Binary Grid

# Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
# A grid is said to be valid if all the cells above the main diagonal are zeros.
# Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.
# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).


# Example 1:
# Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
# Output: 3

# Example 2:
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# Explanation: All rows are similar, swaps have no effect on the grid.

# Example 3:
# Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
# Output: 0

# Constraints:
# n == grid.length == grid[i].length
# 1 <= n <= 200
# grid[i][j] is either 0 or 1

class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        total_swaps = 0
        
        #pre-processing: count trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)

        #given these numbers, perform a buble sort to move them into the correct order (this simulates the swapping of adjacent rows)
        for i in range(n):
            # Row i needs at least (n - 1 - i) trailing zeros
            needed = n - 1 - i
            
            #find the first row at or below i that satisfies the requirement
            # choose the 1st as it will be  aminimum swap that fufulls the requirement (does not need to be an optimal permutation)
            found_idx = -1
            for j in range(i, n):
                if trailing_zeros[j] >= needed:
                    found_idx = j
                    break
            
            # If no such row exists, it's impossible (if there is nothing that will fit in teh gap)
            if found_idx == -1:
                return -1
            
            #bubble the found row up to position i (counting the swaps)
            while found_idx > i:
                #swap in the count list to keep track of current state
                trailing_zeros[found_idx], trailing_zeros[found_idx - 1] = \
                    trailing_zeros[found_idx - 1], trailing_zeros[found_idx]
                total_swaps += 1
                found_idx -= 1
                
        return total_swaps
        