# 3546. Equal Sum Grid Partition I

# You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:
# Each of the two resulting sections formed by the cut is non-empty.
# The sum of the elements in both sections is equal.
# Return true if such a partition exists; otherwise return false.

# Example 1:
# Input: grid = [[1,4],[2,3]]
# Output: true
# Explanation:
# A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

# Example 2:
# Input: grid = [[1,3],[2,4]]
# Output: false
# Explanation:
# No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.

# Constraints:
# 1 <= m == grid.length <= 105
# 1 <= n == grid[i].length <= 105
# 2 <= m * n <= 105
# 1 <= grid[i][j] <= 105

class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        # make a cumulative sum for all rows and for columns

        # horizontal cuts
        #   go through the list at the end and see if there are any that are the same
        #    (0->n == n+1->max)
        # vertical cases
        #   for every column, see if the total sum is the same

        # retrun true if this can be done, false if after eery iteration it fails

        rows = len(grid)
        cols = len(grid[0])
        
        # total sum of the grid (need to be able to half it)
        total_sum = sum(sum(row) for row in grid)
        
        # if odd, it cant be split evenly
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2

        # Horizontal Cuts
        # cumulative sum of each row
        current_horizontal_sum = 0
        for r in range(rows - 1): # dont got to end as there has to be somthing in the 2nd half
            current_horizontal_sum += sum(grid[r])
            if current_horizontal_sum == target:
                return True

        # Vertical Cuts
        # cumulative sum of each column
        current_vertical_sum = 0
        for c in range(cols - 1): # dont go to end as we need to have 2 halves
            for r in range(rows):
                current_vertical_sum += grid[r][c]
            
            if current_vertical_sum == target:
                return True

        return False