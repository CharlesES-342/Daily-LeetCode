# 799. Champagne Tower

# We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.
# Each glass holds one cup of champagne.

# Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will
# fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall
# equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

# For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses
# on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total
# now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter
# full, as pictured below.
# Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are
# 0-indexed.)

# Example 1:
# Input: poured = 1, query_row = 1, query_glass = 1
# Output: 0.00000
# Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid
# so all the glasses under the top glass will remain empty.

# Example 2:
# Input: poured = 2, query_row = 1, query_glass = 1
# Output: 0.50000
# Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess
# liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half
# cup of champange.

# Example 3:
# Input: poured = 100000009, query_row = 33, query_glass = 17
# Output: 1.00000

# Constraints:
# 0 <= poured <= 109
# 0 <= query_glass <= query_row < 100



class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        #can do it as a choice triangle with different values
        # Create a 2D array to track champagne in each glass
        # We only need to simulate up to query_row
        glasses = [[0.0] * (i + 1) for i in range(query_row + 1)]
        
        # Pour all champagne into the top glass
        glasses[0][0] = poured
        
        # Simulate the flow down the pyramid
        for row in range(query_row):
            for col in range(len(glasses[row])):
                # Calculate overflow from current glass
                overflow = (glasses[row][col] - 1.0) / 2.0
                
                if overflow > 0:
                    # Pour to left glass below
                    glasses[row + 1][col] += overflow
                    # Pour to right glass below
                    glasses[row + 1][col + 1] += overflow
        
        # Return how full the queried glass is (capped at 1.0)
        return min(1.0, glasses[query_row][query_glass])
    
# basically pascals triangle with different input numbers            