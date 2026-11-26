# 3360. Stone Removal Game

# Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.
# Alice starts by removing exactly 10 stones on her first turn.
# For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
# The player who cannot make a move loses the game.
# Given a positive integer n, return true if Alice wins the game and false otherwise.

# Example 1:
# Input: n = 12
# Output: true
# Explanation:
# Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
# Bob cannot remove 9 stones, so Alice wins.

# Example 2:
# Input: n = 1
# Output: false
# Explanation:
# Alice cannot remove 10 stones, so Alice loses.

# Constraints:
# 1 <= n <= 50

class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Available moves: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        # Turn indices (0-based): even index = Alice, odd index = Bob
        cumulative = [10, 19, 27, 34, 40, 45, 49, 52, 54, 55]

        turns = 0
        for total_needed in cumulative:
            if n >= total_needed:
                turns += 1
            else:
                break

        # Alice makes moves on turn 1 (1st move), turn 3 (3rd move), etc.
        return turns % 2 == 1