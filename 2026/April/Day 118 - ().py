# 2033. Minimum Operations to Make a Uni-Value Grid

# You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
# A uni-value grid is a grid where all the elements of it are equal.
# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

# Example 1:
# Input: grid = [[2,4],[6,8]], x = 2
# Output: 4
# Explanation: We can make every element equal to 4 by doing the following: 
# - Add x to 2 once.
# - Subtract x from 6 once.
# - Subtract x from 8 twice.
# A total of 4 operations were used.

# Example 2:
# Input: grid = [[1,5],[2,3]], x = 1
# Output: 5
# Explanation: We can make every element equal to 3.

# Example 3:
# Input: grid = [[1,2],[3,4]], x = 2
# Output: -1
# Explanation: It is impossible to make every element equal.

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 1 <= x, grid[i][j] <= 104

import numpy as np
class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # check all elements and check if they have all the same remainders for MOD x (if not, it is not possible)
        # sort the elements
        # find the number to get them all to and count

        #flattern the grid
        flattened = np.array(grid).flatten()
        flattened.sort()
                
        #find the number of x's needed to make the max value
        # median =  target
        median = flattened[len(flattened) // 2]
        total_ops = 0
        rem = flattened[0] % x

        for val in flattened:
            # if the remainder is different, you cant get the target (not possible)
            if val % x != rem:
                return -1
            
            # find number of x's needed to get to median
            total_ops += abs(val - median) // x
            
        return total_ops
