# 3548. Equal Sum Grid Partition II

# You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:
# Each of the two resulting sections formed by the cut is non-empty.
# The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
# If a cell is discounted, the rest of the section must remain connected.
# Return true if such a partition exists; otherwise, return false.
# Note: A section is connected if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.

# Example 1:
# Input: grid = [[1,4],[2,3]]
# Output: true
# Explanation:
# A horizontal cut after the first row gives sums 1 + 4 = 5 and 2 + 3 = 5, which are equal. Thus, the answer is true.

# Example 2:
# Input: grid = [[1,2],[3,4]]
# Output: true
# Explanation:
# A vertical cut after the first column gives sums 1 + 3 = 4 and 2 + 4 = 6.
# By discounting 2 from the right section (6 - 2 = 4), both sections have equal sums and remain connected. Thus, the answer is true.

# Example 3:
# Input: grid = [[1,2,4],[2,3,5]]
# Output: false
# Explanation:
# A horizontal cut after the first row gives 1 + 2 + 4 = 7 and 2 + 3 + 5 = 10.
# By discounting 3 from the bottom section (10 - 3 = 7), both sections have equal sums, but they do not remain connected as it splits the bottom section into two parts ([2] and [5]). Thus, the answer is false.

# Example 4:
# Input: grid = [[4,1,8],[3,2,6]]
# Output: false
# Explanation:
# No valid cut exists, so the answer is false.

# Constraints:
# 1 <= m == grid.length <= 105
# 1 <= n == grid[i].length <= 105
# 2 <= m * n <= 105
# 1 <= grid[i][j] <= 105

#initial attmpt ran out of time:
class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        # same logic as the part 1, but you can only remove the ends for row/column size of 1, for anything else, you can remove any element you want
    
        rows, cols = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)

        # Vertical Cuts
        col_sums = [sum(grid[r][c] for r in range(rows)) for c in range(cols)]
        curr_v = 0
        for c in range(cols - 1):
            curr_v += col_sums[c]
            # Check Left Partition
            if self.is_valid(grid, curr_v, total_sum - curr_v, 0, 0, rows, c + 1):
                return True
            # Check Right Partition
            if self.is_valid(grid, total_sum - curr_v, curr_v, 0, c + 1, rows, cols):
                return True

        # Horizontal Cuts
        curr_h = 0
        for r in range(rows - 1):
            curr_h += sum(grid[r])
            # Check Top Partition
            if self.is_valid(grid, curr_h, total_sum - curr_h, 0, 0, r + 1, cols):
                return True
            # Check Bottom Partition
            if self.is_valid(grid, total_sum - curr_h, curr_h, r + 1, 0, rows, cols):
                return True

        return False

    def is_valid(self, grid, heavy_sum, light_sum, r_start, c_start, r_end, c_end):
        diff = heavy_sum - light_sum
        if diff == 0: return True
        if diff < 0: return False
        
        h = r_end - r_start
        w = c_end - c_start

        # if it's a 1D line - only remove ends
        if h == 1:
            return grid[r_start][c_start] == diff or grid[r_start][c_end - 1] == diff
        if w == 1:
            return grid[r_start][c_start] == diff or grid[r_end - 1][c_start] == diff
            
        # if it's 2D - anything can go
        for r in range(r_start, r_end):
            for c in range(c_start, c_end):
                if grid[r][c] == diff:
                    return True
                    
        return False
    
#this was based on the example answer:
# this was generate by Gemini.ai based on the editorial:
class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        # We check the grid, then rotate it 90 degrees 3 times to cover all 4 directions
        current_grid = grid
        for _ in range(4):
            if self.check_horizontal_upper(current_grid):
                return True
            # Rotate 90 degrees clockwise
            current_grid = list(zip(*current_grid[::-1]))
        return False

    def check_horizontal_upper(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        if rows < 2:
            return False
            
        total_sum = sum(sum(row) for row in grid)
        seen_elements = {0} # Handles the "no deletion" case (x=0)
        current_upper_sum = 0

        for r in range(rows - 1):
            # Update the sum with the current row
            row_sum = sum(grid[r])
            current_upper_sum += row_sum
            
            # The target element to remove: x = 2*sum - total
            # Because: sum - x = total - sum
            target_x = 2 * current_upper_sum - total_sum
            
            # Case 1: First Row (Thin Horizontal)
            if r == 0:
                # Only ends are removable in a 1D-style row
                if target_x in {0, grid[0][0], grid[0][cols-1]}:
                    return True
            
            # Case 2: Single Column (Thin Vertical)
            elif cols == 1:
                # Only the top element of the whole grid or the current bottom row element
                if target_x in {0, grid[0][0], grid[r][0]}:
                    return True
            
            # Case 3: Standard 2D Block
            else:
                # Any element seen so far in the upper part can be removed
                if target_x in seen_elements:
                    return True
            
            # Add current row's elements to the set for the next row's check
            for val in grid[r]:
                seen_elements.add(val)
                
        return False
    
    # while my approach isnt bad, this is far superior and I think it would have taken me longer than
    # i would have liked without the editorial (gemini was just used to make clear my understaning though
    # the code)

    # HOW IT WORKS:
    # in default (large grid) environments it can be determined that it is possible there exisnts an
    # element x such that ht efollowing are satisfied
    # side_sum - x = total - side_sum
    # so x = 2(side_sum) - total

    # this is made more efficint by rotating the grid. Rather than seporate logic for
    # vertical and horizontal, it can simply just be rotated and then the same logic applied