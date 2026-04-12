# 1320. Minimum Distance to Type a Word Using Two Fingers

# You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.
# For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).
# Given the string word, return the minimum total distance to type such string using only two fingers.
# The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.
# Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.


# Example 1:
# Input: word = "CAKE"
# Output: 3
# Explanation: Using two fingers, one optimal way to type "CAKE" is: 
# Finger 1 on letter 'C' -> cost = 0 
# Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
# Finger 2 on letter 'K' -> cost = 0 
# Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
# Total distance = 3

# Example 2:
# Input: word = "HAPPY"
# Output: 6
# Explanation: Using two fingers, one optimal way to type "HAPPY" is:
# Finger 1 on letter 'H' -> cost = 0
# Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
# Finger 2 on letter 'P' -> cost = 0
# Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
# Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
# Total distance = 6

# Constraints:
# 2 <= word.length <= 300
# word consists of uppercase English letters.

class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        #you could use either fingure for a letter (e.g. 1111121111 might be the most efficient)
        #go thorugh the word dynamically and add a letter (choose a fingure) and go from there
        #choose the minimum from teh previous letter

        #define initial table:
        grid = {}
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for i, letter in enumerate(letters):
            x = i % 6
            y = i // 6
            grid[letter] = (x, y)

        # --- helper function: distance between 2 points ---
        def dist(a, b):
            # not determined the other point yet
            if a is None or b is None:
                return 0
            #determine the absolute distance
            x1, y1 = grid[a]
            x2, y2 = grid[b]
            return abs(x1 - x2) + abs(y1 - y2)
        
        #hold the costs for each fingure
        dp = {(None, None): 0}

        #now go through the word
        for char in word:
            new_dp = {}
            #go through orevious fingure positions which resulted in a valid word so-far
            for (f1, f2), cost in dp.items():
                #move finger 1
                state = (char, f2)
                new_cost = cost + dist(char, f1)
                if state not in new_dp or new_dp[state] > new_cost:
                    new_dp[state] = new_cost #this is more efficient
                
                #move finger 2
                state = (f1, char)
                new_cost = cost + dist(f2, char)
                if state not in new_dp or new_dp[state] > new_cost:
                    new_dp[state] = new_cost #this is more efficient
                
            dp = new_dp
    
        return min(dp.values()) #return the option that took the least distance
    
# despite being a hard problem, it was way too easy!