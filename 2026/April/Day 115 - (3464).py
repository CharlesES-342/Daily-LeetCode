# 3464. Maximize the Distance Between Points on a Square

# You are given an integer side, representing the edge length of a square with corners at (0, 0), (0, side), (side, 0), and (side, side) on a Cartesian plane.
# You are also given a positive integer k and a 2D integer array points, where points[i] = [xi, yi] represents the coordinate of a point lying on the boundary of the square.
# You need to select k elements among points such that the minimum Manhattan distance between any two points is maximized.
# Return the maximum possible minimum Manhattan distance between the selected k points.
# The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.

# Example 1:
# Input: side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4
# Output: 2
# Explanation:
# Select all four points.

# Example 2:
# Input: side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4
# Output: 1
# Explanation:
# Select the points (0, 0), (2, 0), (2, 2), and (2, 1).

# Example 3:
# Input: side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5
# Output: 1
# Explanation:
# Select the points (0, 0), (0, 1), (0, 2), (1, 2), and (2, 2).

# Constraints:
# 1 <= side <= 109
# 4 <= points.length <= min(4 * side, 15 * 103)
# points[i] == [xi, yi]
# The input is generated such that:
# points[i] lies on the boundary of the square.
# All points[i] are unique.
# 4 <= k <= min(25, points.length)

class Solution(object):
    def maxDistance(self, side, points, k):
        """
        :type side: int
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        # turn points into a 1D circular array
        def to1d(x, y):
            if x == 0:
                return y
            elif y == side:
                return side + x
            elif x == side:
                return 3 * side - y
            else:
                return 4 * side - x

        arr = sorted(to1d(x, y) for x, y in points)
        n = len(arr)
        perim = 4 * side
        doubled = arr + [x + perim for x in arr]

        def canAchieve(limit):
            for i in range(n):
                count = 1
                prev = doubled[i]
                for _ in range(k - 1):
                    target = prev + limit
                    idx = bisect.bisect_left(doubled, target, i + 1, i + n)
                    if idx < i + n:
                        prev = doubled[idx]
                        count += 1
                    else:
                        break
                if count == k:
                    if arr[i] + perim - prev >= limit:
                        return True
            return False

        lo, hi = 1, side
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if canAchieve(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
    
    # I struggled with this. It is a problem I'd like to come back to when I have more time and no
    # other deadlines