# 3411. Maximum Subarray With Equal Products

# You are given an array of positive integers nums.
# An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:
# prod(arr) is the product of all elements of arr.
# gcd(arr) is the GCD of all elements of arr.
# lcm(arr) is the LCM of all elements of arr.
# Return the length of the longest product equivalent subarray of nums.

# Example 1:
# Input: nums = [1,2,1,2,1,1,1]
# Output: 5
# Explanation: 
# The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

# Example 2:
# Input: nums = [2,3,4,5,6]
# Output: 3
# Explanation: 
# The longest product equivalent subarray is [3, 4, 5].

# Example 3:
# Input: nums = [1,2,3,1,4,5,1]
# Output: 5

# Constraints:
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10

class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        # the worst case array contains all characters: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        #   the LCM of this is 2520
        #   from here LCM * GCD = 2520 * max(nums)

        # form a sub-array using an expanding window, store the minimum value
        n = len(nums)
        max_len = 2
        curr_prod = 1
        left = 0

        for right in range(n):
            while gcd(curr_prod, nums[right]) > 1:
                curr_prod //= nums[left]
                left += 1
            curr_prod *= nums[right]
            max_len = max(max_len, right - left + 1)

        return max_len