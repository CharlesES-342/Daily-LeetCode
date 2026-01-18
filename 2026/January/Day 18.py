#1895. Largest Magic Square

# A k x k magic square is a k x k grid filled with integers such that every row sum, every
# column sum, and both diagonal sums are all equal. The integers in the magic square do not
# have to be distinct. Every 1 x 1 grid is trivially a magic square.

# Given an m x n integer grid, return the size (i.e., the side length k) of the largest
# magic square that can be found within this grid.


class Solution(object):
    def largestMagicSquare(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def is_magic(r, c, k):
            #get the target sum from the first row
            target = sum(grid[r][c:c+k])
            
            #check all Rows
            for i in range(r, r + k):
                if sum(grid[i][c:c+k]) != target:
                    return False
            
            #check all Columns
            for j in range(c, c + k):
                col_sum = sum(grid[i][j] for i in range(r, r + k))
                if col_sum != target:
                    return False
            
            # check Main Diagonal
            if sum(grid[r + i][c + i] for i in range(k)) != target:
                return False
            
            #check Anti-Diagonal
            if sum(grid[r + i][c + k - 1 - i] for i in range(k)) != target:
                return False
            
            return True

        # Try every possible square size k, starting from the largest possible
        for k in range(min(rows, cols), 1, -1):
            for r in range(rows - k + 1):
                for c in range(cols - k + 1):
                    if is_magic(r, c, k):
                        return k
        
        return 1 #the smallest magic square is always 1x1 if nothing larger exists