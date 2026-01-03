# 1411. Number of Ways to Paint N x 3 Grid

# You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow,
# or Green while making sure that no two adjacent cells have the same color
# (i.e., no two cells that share vertical or horizontal sides have the same color).

# Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

# Example 1
# Input: n = 1
# Output: 12
# Explanation: There are 12 possible way to paint the grid as shown.

# Example 2:
# Input: n = 5000
# Output: 30228214

class Solution(object):
    def numOfWays(self, n):
        MOD = 10**9 + 7

        #there are 2 types of blocks possible
        #type A: 3 different colors (eg. RGB)
        #type B: 2 different colors (eg. RGR)
        typeA, typeB = 6,6 #for first row/bse cases - there are 6 possible combinations for each

        for i in range(1,n): #move thorugh each block and work out the number of posibilities given it is typeA or typeB
            newTypeA = (typeA * 3 + typeB * 2) % MOD
            newTypeB = (typeA * 2 + typeB * 2) % MOD

            typeA, typeB = newTypeA, newTypeB

        return (typeA+typeB) % MOD
    

#required some additional help for understanding which patterns to look at
#initially was looking at howmany diffferent options for the next row based on a previos row (quess)
    #this would be good if there already existed a Turing machine (some algorithm) to already determine if the solution is valid, not for finding hte solution