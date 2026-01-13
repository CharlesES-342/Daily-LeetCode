# 1266. Minimum Time Visiting All Points
# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in
# seconds to visit all the points in the order given by points.

# You can move according to these rules:

# In 1 second, you can either:
# move vertically by one unit,
# move horizontally by one unit, or
# move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
# You have to visit the points in the same order as they appear in the array.
# You are allowed to pass through points that appear later in the order, but these do not count as visits.


class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #aim ot move in diagonals as far as possible, then move in straight lines
        #a point can eith be on teh same vertical, same horizontal or some combination (diagonals will be more optimal)
        

        timeUnits = 0
        startPoint = points[0]
        pointer = 1
        if (pointer >= len(points)): #incase there is only one point
            return 0
        nextPoint = points[1]
        #go through the list and add any time to go to the next point
        while nextPoint:
            dx = nextPoint[0]-startPoint[0]
            dy = nextPoint[1] - startPoint[1]
            if dx == 0 or dy == 0:# on the same vertical or horizontal plane
                timeUnits += max(abs(dx),abs(dy))
            else: #some diagonal combination
                if min(abs(dx), abs(dy)) == abs(dx):
                    timeUnits += abs(dx) + (abs(dy) - abs(dx))
                else:
                    timeUnits += abs(dy) + (abs(dx) - abs(dy))

            startPoint = nextPoint
            pointer += 1
            if pointer < len(points):
                nextPoint = points[pointer]
            else:
                break
        return timeUnits
            
            