#3507. Minimum Pair Removal to Sort Array 1

# Given an array nums, you can perform the following operation any number of times:

# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist,
# choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.

# An array is said to be non-decreasing if each element is greater than or equal to its
# previous element (if it exists).

# Example 1:
# Input: nums = [5,2,3,1]
# Output: 2
# Explanation:
# The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# The array nums became non-decreasing in two operations.

# Example 2:
# Input: nums = [1,2,2]
# Output: 0
# Explanation:
# The array nums is already sorted.

class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        
        operations = 0
        
        while not self.isNonDecreasing(nums):
            # Find the minimum sum among all adjacent pairs
            min_sum = float('inf')
            min_idx = -1
            
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_idx = i
            
            # Replace the pair at min_idx with their sum
            nums[min_idx] = nums[min_idx] + nums[min_idx + 1]
            nums.pop(min_idx + 1)
            operations += 1
        
        return operations

    #helperfunction to check if it is decreasing
    def isNonDecreasing(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True