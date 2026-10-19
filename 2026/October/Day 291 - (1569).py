# 1569. Number of Ways to Reorder Array to Get Same BST

# Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.
# For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
# Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.
# Since the answer may be very large, return it modulo 109 + 7.

# Example 1:
# Input: nums = [2,1,3]
# Output: 1
# Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.

# Example 2:
# Input: nums = [3,4,5,1,2]
# Output: 5
# Explanation: The following 5 arrays will yield the same BST: 
# [3,1,2,4,5]
# [3,1,4,2,5]
# [3,1,4,5,2]
# [3,4,1,2,5]
# [3,4,1,5,2]

# Example 3:
# Input: nums = [1,2,3]
# Output: 0
# Explanation: There are no other orderings of nums that will yield the same BST.

# Constraints:
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= nums.length
# All integers in nums are distinct.

import math

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 +7

        # 1st number will always be the root
        # Dynamic Programming
        #   split into 2 groupd of equal size (left are smaller, right are larger)
        #   recursively determine the number of ways to for the BST for each left and right
        #       choose the number of ways of choosing the left sub tree (the right subtree will automatically be what is left) - Binomial Coefficient
        #       Left_ways x right_ways x number of ways of choosing the left = Toal ways

        # Choose Formula
        def choose(n, r):
            if r < 0 or r > n:
                return 0
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        
        def helper(arr):
            # Final Case: insuficient length (only one way it can be formed)
            if len(arr) <= 2:
                return 1
            
            # Construst the BST
            # define the root
            root = arr[0]
            # for the left and right sub trees
            left_subtree = [x for x in arr[1:] if x < root]
            right_subtree = [x for x in arr[1:] if x > root]
            
            # Recursively find the number of ways for the left and right subtrees
            ways_left = helper(left_subtree)
            ways_right = helper(right_subtree)
            
            # Use combinations to get the ways of writing the subtrees (n choose k)
            combined_ways = choose(len(left_subtree) + len(right_subtree), len(left_subtree))
            
            return (ways_left * ways_right * combined_ways) % MOD

        # -1 to remove the possibility of the original array
        return (helper(nums) - 1) % MOD