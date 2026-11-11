# 3789. Minimum Cost to Acquire Required Items

# You are given five integers cost1, cost2, costBoth, need1, and need2.
# There are three types of items available:
# An item of type 1 costs cost1 and contributes 1 unit to the type 1 requirement only.
# An item of type 2 costs cost2 and contributes 1 unit to the type 2 requirement only.
# An item of type 3 costs costBoth and contributes 1 unit to both type 1 and type 2 requirements.
# You must collect enough items so that the total contribution toward type 1 is at least need1 and the total contribution toward type 2 is at least need2.
# Return an integer representing the minimum possible total cost to achieve these requirements.

# Example 1:
# Input: cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2
# Output: 3
# Explanation:
# After buying three type 3 items, which cost 3 * 1 = 3, the total contribution to type 1 is 3 (>= need1 = 3) and to type 2 is 3 (>= need2 = 2).
# Any other valid combination would cost more, so the minimum total cost is 3.

# Example 2:
# Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3
# Output: 22
# Explanation:
# We buy need1 = 2 items of type 1 and need2 = 3 items of type 2: 2 * 5 + 3 * 4 = 10 + 12 = 22.
# Any other valid combination would cost more, so the minimum total cost is 22.

# Example 3:
# Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0
# Output: 0
# Explanation:
# Since no items are required (need1 = need2 = 0), we buy nothing and pay 0.

# Constraints:
# 1 <= cost1, cost2, costBoth <= 106
# 0 <= need1, need2 <= 109

class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        # check if the combined cost is less than the cost individually
        #   if so, add costBoth x min(need1, need2)
        #   then add the rest
        #   else: add them all individually

        # another thing to consider is that it is atleast. If the cost of both is alos less than an individuals cost then it may be better to add both (exceeding the minimum needed) to be the cheapest
        
        in_common = min(need1, need2)
        # get the cheapest combination
        cost_common = min(costBoth, cost1 + cost2)

        total = in_common * cost_common

        # see how many are reamaining and only add in the cheapest form available (one of these will already be done - as the minimum is taken from the min(), the lower "need" is removed/completed already)
        total += (need1 - in_common) * min(cost1, costBoth)
        total += (need2 - in_common) * min(cost2, costBoth)

        return total