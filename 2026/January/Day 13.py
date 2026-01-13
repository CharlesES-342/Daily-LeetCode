#3453. Separate Squares
# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left
# point and the side length of a square parallel to the x-axis.

# Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

# Answers within 10-5 of the actual answer will be accepted.

# Note: Squares may overlap. Overlapping areas should be counted multiple times.

 

# Example 1:

# Input: squares = [[0,0,1],[2,2,1]]

# Output: 1.00000


class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        #based on area
        total_area = 0.0
        min_y = float('inf')
        max_y = float('-inf')
        
        for x, y, l in squares:
            total_area += float(l) * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
            
        target_area = total_area / 2.0

        #binary search for height (mid)
        low = float(min_y)
        high = float(max_y)

        for _ in range (100): #10^5 required accuracy
            mid = (low + high) / 2.0
            current_area_below = 0.0

            for _, y, l in squares:
                if y < mid: #if it is partially or fully below the midline
                    height_below = min(float(l), mid - y)
                    current_area_below += height_below * l
            if current_area_below < target_area:
                low = mid
            else:
                high = mid
        return low

        