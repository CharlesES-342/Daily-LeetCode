#3047. Find the Largest Area of Square Inside Two Rectangles

# There exist n rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays
# bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and topRight[i] = [c_i, d_i] represent the bottom-left and
# top-right coordinates of the ith rectangle, respectively.

# You need to find the maximum area of a square that can fit inside the intersecting region of at least two rectangles.
# Return 0 if such a square does not exist.

class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        maxSide = 0
        n = len(bottomLeft)

        # 1. Compare every pair (i, j)
        for i in range(n):
            for j in range(i + 1, n):
                # 2. Find the boundaries of the intersection rectangle
                # The overlap's bottom-left is the MAX of the two bottom-lefts
                inter_bl_x = max(bottomLeft[i][0], bottomLeft[j][0])
                inter_bl_y = max(bottomLeft[i][1], bottomLeft[j][1])
                
                # The overlap's top-right is the MIN of the two top-rights
                inter_tr_x = min(topRight[i][0], topRight[j][0])
                inter_tr_y = min(topRight[i][1], topRight[j][1])
                
                # 3. Calculate width and height of the overlap
                dx = inter_tr_x - inter_bl_x
                dy = inter_tr_y - inter_bl_y
                
                # 4. If there is a valid overlap, the side of the 
                # largest square is the smaller of the two dimensions
                if dx > 0 and dy > 0:
                    side = min(dx, dy)
                    maxSide = max(maxSide, side)
        
        # 5. Return the area
        return maxSide * maxSide
    
    #could bebbetter with sweep line but this is good enough for constraints
    #could also be made slightly more efficient by precomputing overlaps but n is small enough
    #also by assigining variables earlier, rather than every inside fo loop
