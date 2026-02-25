#2943. Maximize Area of Square Hole in GTrid

# You are given the two integers, n and m and two integer arrays, hBars and vBars.
# The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells.
# The bars are indexed starting from 1.

# You can remove some of the bars in hBars from horizontal bars and some of the bars
# in vBars from vertical bars. Note that other bars are fixed and cannot be removed.

# Return an integer denoting the maximum area of a square-shaped hole in the grid, after
# removing some bars (possibly none).

#understanding - what is the greatest square you can remove by removing bars from the allowed list
class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """

        #go through each array of allowed removals and find the biggest gap
        #take the minimum of these 2 numbers and return that squared
        def maxSeporation (arr):
            #this has to be consecutive bar
            count = 1
            maxCount = 1
            for x, y in zip(arr, arr[1:]):
                if (y - x == 1):
                    count += 1
                    maxCount = max(maxCount, count)
                else:
                    count = 1  # Reset to 1, not 0, to represent the new single bar

            print(maxCount)
            return maxCount



        #base case, the arrays of 0 (no removable bars)
        if not hBars or not vBars:
            return 1
        elif len(hBars) == 1 or len(vBars) == 1: #the array size is only 1
            return 4
        else : #array size > 1
            # Sort the bars first, then pass them to your function
            hBars.sort()
            vBars.sort()

            max_approved_separation = min(maxSeporation(hBars), maxSeporation(vBars))
            return (max_approved_separation + 1)**2

        