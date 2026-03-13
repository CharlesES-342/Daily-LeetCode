# 3296. Minimum Number of Seconds to Make Mountain Height Zero

# You are given an integer mountainHeight denoting the height of a mountain.
# You are also given an integer array workerTimes representing the work time of workers in seconds.
# The workers work simultaneously to reduce the height of the mountain. For worker i:
# To decrease the mountain's height by x, it takes workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x seconds. For example:
# To reduce the height of the mountain by 1, it takes workerTimes[i] seconds.
# To reduce the height of the mountain by 2, it takes workerTimes[i] + workerTimes[i] * 2 seconds, and so on.
# Return an integer representing the minimum number of seconds required for the workers to make the height of the mountain 0.


# Example 1:
# Input: mountainHeight = 4, workerTimes = [2,1,1]
# Output: 3
# Explanation:
# One way the height of the mountain can be reduced to 0 is:
# Worker 0 reduces the height by 1, taking workerTimes[0] = 2 seconds.
# Worker 1 reduces the height by 2, taking workerTimes[1] + workerTimes[1] * 2 = 3 seconds.
# Worker 2 reduces the height by 1, taking workerTimes[2] = 1 second.
# Since they work simultaneously, the minimum time needed is max(2, 3, 1) = 3 seconds.

# Example 2:
# Input: mountainHeight = 10, workerTimes = [3,2,2,4]
# Output: 12
# Explanation:
# Worker 0 reduces the height by 2, taking workerTimes[0] + workerTimes[0] * 2 = 9 seconds.
# Worker 1 reduces the height by 3, taking workerTimes[1] + workerTimes[1] * 2 + workerTimes[1] * 3 = 12 seconds.
# Worker 2 reduces the height by 3, taking workerTimes[2] + workerTimes[2] * 2 + workerTimes[2] * 3 = 12 seconds.
# Worker 3 reduces the height by 2, taking workerTimes[3] + workerTimes[3] * 2 = 12 seconds.
# The number of seconds needed is max(9, 12, 12, 12) = 12 seconds.

# Example 3:
# Input: mountainHeight = 5, workerTimes = [1]
# Output: 15
# Explanation:
# There is only one worker in this example, so the answer is workerTimes[0] + workerTimes[0] * 2 + workerTimes[0] * 3 + workerTimes[0] * 4 + workerTimes[0] * 5 = 15.

# Constraints:
# 1 <= mountainHeight <= 105
# 1 <= workerTimes.length <= 104
# 1 <= workerTimes[i] <= 106

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        #Binary search. Given the height is atmost 10^5 it will take one worker (at most)
        # this is the worst case time
        
        #helper to check if the mountain can flatterned in this time
        def can_finish(max_time):
            total_reduced = 0
            for t in workerTimes:
                #find n such that t * n * (n + 1) / 2 <= max_time
                # n * (n + 1) <= (2 * max_time) / t
                # Solving n^2 + n - (2 * max_time / t) <= 0
                limit = (2 * max_time) // t
                n = int(((1 + 4 * limit)**0.5 - 1) // 2) #to reduce time so you dont have to do all the additions (Quadratic formula)
                total_reduced += n
                if total_reduced >= mountainHeight:
                    #it can be done
                    return True
            return total_reduced >= mountainHeight

        low = 1
        # Set high based on the fastest worker doing the whole mountain
        # Max height 10^6, fastest worker 1: (10^6 * 10^6+1) / 2
        #the slowest worker working on their own...(max time)
        high = min(workerTimes) * (mountainHeight * (mountainHeight + 1)) // 2
        ans = high #worst case
        
        while low <= high:
            mid = (low + high) // 2
            if can_finish(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

#How the Quadratic Formula works:
# each personas time can be thought of as a triangle (adding previous time and so on) where the area is the total time
# t = base unit of time (e.g., 3 seconds)
# n = height unit reduction (e.g., 4 units)
# Total Time = t * n * (n + 1) / 2

# Visualization for n=4:
#
#  * (Row 1: 1 * t)
#  * * (Row 2: 2 * t)
#  * * * (Row 3: 3 * t)
#  * * * * (Row 4: 4 * t)
#
# Height (n): 4 units
# Rows represent consecutive steps.
# The area formed is roughly n * (n + 1) / 2.
# Multiply the area by 't' for total time.