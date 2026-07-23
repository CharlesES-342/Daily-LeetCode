# 3513. Number of Unique XOR Triplets I

# You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [1, n].
# A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.
# Return the number of unique XOR triplet values from all possible triplets (i, j, k).

# Example 1:
# Input: nums = [1,2]
# Output: 2
# Explanation:
# The possible XOR triplet values are:
# (0, 0, 0) → 1 XOR 1 XOR 1 = 1
# (0, 0, 1) → 1 XOR 1 XOR 2 = 2
# (0, 1, 1) → 1 XOR 2 XOR 2 = 1
# (1, 1, 1) → 2 XOR 2 XOR 2 = 2
# The unique XOR values are {1, 2}, so the output is 2.

# Example 2:
# Input: nums = [3,1,2]
# Output: 4
# Explanation:
# The possible XOR triplet values include:
# (0, 0, 0) → 3 XOR 3 XOR 3 = 3
# (0, 0, 1) → 3 XOR 3 XOR 1 = 1
# (0, 0, 2) → 3 XOR 3 XOR 2 = 2
# (0, 1, 2) → 3 XOR 1 XOR 2 = 0
# The unique XOR values are {0, 1, 2, 3}, so the output is 4.

# Constraints:
# 1 <= n == nums.length <= 105
# 1 <= nums[i] <= n
# nums is a permutation of integers from 1 to n.

class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # order of the numbers does not matter (from within the array, only the existance)
        # the only thing that matters is the resultint XOR values.
        # given there is some combination of numbers to result in all intermediate numbers, the task is finding the smallest and larges values and returning the differences in results
        #   even if a combination results in a previous value, the counting the possilbe values rules out this duplication (rather than checkiong every time if it is in the set)
        n = len(nums) #n-1 is the max value in this array

        # the smallest value possible consists of all 0's
        #   E.G. by doing 001 XOR 110 XOR 111
        #   combining_factor = 0 if the max number is a round power of 2 (the max number will be the max value)
        #   combining_factor € [0,1]* for all locations of 0's in the largest number (to form a combined number that exceeds the original array max)

        if n < 3:
            return n
        return 1 << n.bit_length() # the next largest value consisting of all 1's, given there is some 0's. If its already all 1's, thats the answer 

'''
Thought this was way too easy. I thought I was loosing it. Didn't look at examples or costraints, followed my cut and it wored perfectly.
'''