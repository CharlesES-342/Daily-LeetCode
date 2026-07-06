# 1288. Remove Covered Intervals

# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.
# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
# Return the number of remaining intervals.

# Example 1:
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

# Example 2:
# Input: intervals = [[1,4],[2,3]]
# Output: 1

# Constraints:
# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= li < ri <= 105
# All the given intervals are unique.

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # find pairs such that for [a,b] and [c,d], c is smaller than a and d is larger than b
        n = len(intervals)
        # removing table (rather than perform removals, just track the uses as removal has added cost)
        active = [1]*n

        # Brute force
        for i in range(n):
            for j in range(n):
                if i != j:
                    # Check if interval i is fully covered by interval j
                    if intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                        active[i] = 0
                        break # No need to check other intervals for i
        
        return sum(active)

'''
The above can be made more efficient by sorting the elements first to reduce searching time
'''