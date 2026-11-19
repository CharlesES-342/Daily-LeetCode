# 2567. Minimum Score by Changing Two Elements

# You are given an integer array nums.
# The low score of nums is the minimum absolute difference between any two integers.
# The high score of nums is the maximum absolute difference between any two integers.
# The score of nums is the sum of the high and low scores.
# Return the minimum score after changing two elements of nums.

# Example 1:
# Input: nums = [1,4,7,8,5]
# Output: 3
# Explanation:
# Change nums[0] and nums[1] to be 6 so that nums becomes [6,6,7,8,5].
# The low score is the minimum absolute difference: |6 - 6| = 0.
# The high score is the maximum absolute difference: |8 - 5| = 3.
# The sum of high and low score is 3.

# Example 2:
# Input: nums = [1,4,3]
# Output: 0
# Explanation:
# Change nums[1] and nums[2] to 1 so that nums becomes [1,1,1].
# The sum of maximum absolute difference and minimum absolute difference is 0.

# Constraints:
# 3 <= nums.length <= 105
# 1 <= nums[i] <= 109

class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # can either decrease the max difference or decrease the minimum difference (or both if one of the numbers is in both)
        # each pair can be changed, go through every combination of change to make this different
        # the low score can always be made 0 because you can just change a value to be the same
        n = len(nums)

        # Base Case: if the max and min are the same
        if n <= 2:
            return 0

        # if the min score is 0 then only changes to the max are required
        # can either:
        #   reduce the max 2 to make it closer (so the final 3 are the same when sorted)
        #   reduce the min 2 to make it closer (so the first 3 are the same when sorted)
        #   can also move one element at either end to match another to make a difference
        nums.sort()
        return min(
            nums[n-1] - nums[2],    # change the two smallest
            nums[n-3] - nums[0],    # change the two largest
            nums[n-2] - nums[1],    # change the smallest and the largest
        )