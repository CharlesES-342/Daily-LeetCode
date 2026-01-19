#1293. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

# Given a m x n matrix mat and an integer threshold, return the maximum side-length
# of a square with a sum less than or equal to threshold or return 0 if there is no
# such square.

# Example 1:
# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as shown.

# Example 2:
# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
# Output: 0


#first attempt - brute force (runs in to a time limit exceeded error))
# class Solution(object):
#     def maxSideLength(self, mat, threshold):
#         """
#         :type mat: List[List[int]]
#         :type threshold: int
#         :rtype: int
#         """
#         maxSideLength = min(len(mat), len(mat[0])) #gives the maximum potential side length

#         #for every side lenght (starting from the max size)
#         for s in range(maxSideLength, 0, -1):
#             #for every square location
#             for y in range(len(mat) +1 -s):
#                 for x in range(len(mat[0])-s+1):
#                     #add together what is in this square
#                     total = sum(sum(row[x : x + s]) for row in mat[y : y + s])
#                     if(total <= threshold):
#                         #this is a valid square
#                         return s
#         #base case - if every indervidual value is greater than the threshold
#         return 0

#could use a cumulative approach - has a better time complexity - O(n^2)
class Solution(object):
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])

        #form a cummulative array of differences - O(n^2)
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + mat[i-1][j-1]

        #helper function - to give the sum between 2 locaitons
        def getSum(r1, c1, r2, c2):
            return P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]

        #loop though all squares possible - O(n^2)
        res = 0
        for y in range(m):
            for x in range(n):
                #try to increase the size
                s = res + 1
                
                #check the square will fit
                if y >= s - 1 and x >= s - 1:
                    #if it fits, check the value
                    if getSum(y - s + 1, x - s + 1, y, x) <= threshold:
                        res = s #bigger square found
        return res
        