# 1401. Circle and Rectangle Overlapping

# You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.
# Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.

# Example 1:
# Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
# Output: true
# Explanation: Circle and rectangle share the point (1,0).

# Example 2:
# Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
# Output: false

# Example 3:
# Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
# Output: true

# Constraints:
# 1 <= radius <= 2000
# -104 <= xCenter, yCenter <= 104
# -104 <= x1 < x2 <= 104
# -104 <= y1 < y2 <= 104

class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        # Find the point on/inside the rectangle closest to the circle center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        # Calculate distance from circle center to closest point
        dx = xCenter - closest_x
        dy = yCenter - closest_y

        # Check if the squared distance is <= radius^2
        return (dx * dx + dy * dy) <= (radius * radius)        


'''
This works because the rectangle is axis-aligned, so the closest point on the rectangle to
the circle center can be found by clamping the circle center coordinates to the rectangle's
corner bounds. (it finds the closest point to the circle center that is inside or on the 
rectange). Then, given this, it checks this point's distance to the circles centre using
pythagoras, if it is less than or equal to the radius, then the circle and rectangle
overlap.

Being Axis-Aligned is the key part, as you can determine the point on the rectangle closest
to the rectangle as it will be on the edge of the rectangle or a corner. this can be
found using the min/max functions to get the X/Y coordinates of this point.
'''