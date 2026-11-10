# 3693. Climbing Stairs II

# You are climbing a staircase with n + 1 steps, numbered from 0 to n.
# You are also given a 1-indexed integer array costs of length n, where costs[i] is the cost of step i.
# From step i, you can jump only to step i + 1, i + 2, or i + 3. The cost of jumping from step i to step j is defined as: costs[j] + (j - i)2
# You start from step 0 with cost = 0.
# Return the minimum total cost to reach step n.

# Example 1:
# Input: n = 4, costs = [1,2,3,4]
# Output: 13
# Explanation:
# One optimal path is 0 → 1 → 2 → 4
# Jump	Cost Calculation	Cost
# 0 → 1	costs[1] + (1 - 0)2 = 1 + 1	2
# 1 → 2	costs[2] + (2 - 1)2 = 2 + 1	3
# 2 → 4	costs[4] + (4 - 2)2 = 4 + 4	8
# Thus, the minimum total cost is 2 + 3 + 8 = 13

# Example 2:
# Input: n = 4, costs = [5,1,6,2]
# Output: 11
# Explanation:
# One optimal path is 0 → 2 → 4
# Jump	Cost Calculation	Cost
# 0 → 2	costs[2] + (2 - 0)2 = 1 + 4	5
# 2 → 4	costs[4] + (4 - 2)2 = 2 + 4	6
# Thus, the minimum total cost is 5 + 6 = 11

# Example 3:
# Input: n = 3, costs = [9,8,3]
# Output: 12
# Explanation:
# The optimal path is 0 → 3 with total cost = costs[3] + (3 - 0)2 = 3 + 9 = 12

# Constraints:
# 1 <= n == costs.length <= 105​​​​​​​
# 1 <= costs[i] <= 104

class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        # for each step, there are 3 states (depending on which of the 3 previous steps you came from, keep every state)
        # you only need to store the weight of 4 steps (the 3 previous and the current)
        # increment throguh each step, assigning the minimum cost to that current step
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Starting at step 0 with cost 0
        
        for j in range(1, n + 1):
            # We can reach step j from step i, where j - 3 <= i < j (and i >= 0)
            for i in range(max(0, j - 3), j):
                # Jump cost: costs[j] + (j - i)^2
                # Note: costs is 1-indexed for steps 1 to n, so costs[j - 1] corresponds to step j.
                current_cost = dp[i] + costs[j - 1] + (j - i) ** 2
                if current_cost < dp[j]:
                    dp[j] = current_cost
                    
        return dp[n]
    



'''
You can also skip additinoal step processing as it is mathmatically equivalent to the above,
but with less space complexity as steps can be taken from the same step to give a constant minimum outcome
and so steps can be looked at and assigned in blocks of 3
'''
class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        v0 = v1 = v2 = 0 # all initially 0 as you can start on any of the first 3 steps

        # for all 3 next steps (from a surrent step), you can step from the same step to have a minimum cost
        # as a result, assign all 3 next steps with the minimum step value and then repeat
        for c in costs:
        # USING SQUARE JUMP DISTANCE PENALTY

            v0, v1, v2 = v1, v2, min(v0 + 9, v1 + 4, v2 + 1) + c
        return v2