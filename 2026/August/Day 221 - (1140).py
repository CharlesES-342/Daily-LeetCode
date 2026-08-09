# 1140. Stone Game II

# Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.
# Alice and Bob take turns, with Alice starting first.
# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.
# The game continues until all the stones have been taken.
# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

# Example 1:
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:
# If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 stones in total.
# If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 stones in total.
# So we return 10 since it's larger.

# Example 2:
# Input: piles = [1,2,3,4,5,100]
# Output: 104

# Constraints:
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 104

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        # Suffix sums to quickly get the sum of remaining piles from index i to the end
        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            # In the event the next choice exceeds the array of choosable piles
            if i + 2 * m >= n:
                return suffix_sums[i]

            # Return reviously reviewed state in the event it occures again from some previous other combination of choices
            if (i, m) in memo:
                return memo[(i, m)]

            # Determine the current state max and move to the next state
            max_stones = 0
            # Try taking X piles, where 1 <= X <= 2M
            # check the combinaitons that are possible from the next players (BOBs) next go, and determine Alices optimal play
            # for each state, determine the maximum next play (storing values for M and the state value)
            for x in range(1, 2 * m + 1):
                # The stones the other player can get from the remaining state
                opponent_stones = dp(i + x, max(m, x))
                # Current player's stones = Total remaining from i - Opponent's best subsequent result
                current_stones = suffix_sums[i] - opponent_stones
                max_stones = max(max_stones, current_stones) # save the curent maximum output form this state

            # stoire state change with new max
            memo[(i, m)] = max_stones
            return max_stones

        return dp(0, 1) # initial max of 0 and M=1


'''
For this problem, I didnt understand what was being asked. I asked Gemini.ai to help me understand what the significance
of M was within this operation and instead it gave me the code (givedn above).
From this however, I added my own comments and reviewd it to get an understanding.
Below is my imporved understanding as proof of achnoledgement.

This problem consists of several piles of stones. For each go you can take as many as 2M stones.
By takingt this selected number of stones, you consequently update the number of new stoes that the other play can choose
from. This can be to your detrement and result in a loss, so the idea is to consider both your possible moves as well as their
next moves (given that both players play optimally). As a resuilt, you make use of states for your gameplay and determin
how best to move forward to ensure a maximum value is obtained. The above coed uses a memory and recustion to store the best
values achecived for each state and then return the maximum value possible for the first player (Alice) given that both
players play optimally.
'''