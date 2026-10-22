# 3942. Minimum Operations to Sort a Permutation

# You are given an integer array nums of length n, where nums is a permutation of the integers from 0 to n - 1.
# You may perform only the following operations:
# Reverse the entire array.
# Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.
# Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.

# Example 1:
# Input: nums = [0,2,1]
# Output: 2
# Explanation:
# Rotate Left by one: [2, 1, 0]
# Reverse the array: [0, 1, 2]
# The array becomes sorted in 2 operations, which is minimal

# Example 2:
# Input: nums = [1,0,2]
# Output: 2
# Explanation:
# Reverse the array: [2, 0, 1]
# Rotate Left by one: [0, 1, 2]
# The array becomes sorted in 2 operations, which is minimal.

# Example 3:
# Input: nums = [2,0,1,3]
# Output: -1
# Explanation:
# It is impossible to reach [2, 0, 1, 3]. Thus, the answer is -1.

# Constraints:
# 1 <= n == nums.length <= 105
# 0 <= nums[i] <= n - 1
# nums is a permutation of integers from 0 to n - 1.

class Solution(object):
    def minOperations(self, nums):
        """:type nums: List[int]""" \
            """:rtype: int"""
        n = len(nums)
        
        try:
            zero_idx = nums.index(0)
        except ValueError:
            return -1
        
        # Check if array is a cyclic shift of increasing order [0, 1, ..., n-1]
        is_increasing = True
        for i in range(n):
            if nums[(zero_idx + i) % n] != i:
                is_increasing = False
                break
                
        # Check if array is a cyclic shift of decreasing order [0, n-1, n-2, ..., 1]
        is_decreasing = True
        for i in range(n):
            val = (n - i) % n
            if nums[(zero_idx + i) % n] != val:
                is_decreasing = False
                break
                
        if not is_increasing and not is_decreasing:
            return -1
            
        ans = float('inf')
        
        if is_increasing:
            # 1. Left shift until 0 is at index 0
            shift_left = zero_idx
            ans = min(ans, shift_left)
            
            # 2. Reverse, left shift, reverse strategy
            ans = min(ans, 2 + ((n - zero_idx) % n))
            
        if is_decreasing:
            # Shift 0 to the final position (index n-1), then reverse
            # Shifts needed: (zero_idx + 1) % n, plus 1 reverse operation
            shift_to_end = (zero_idx + 1) % n
            ans = min(ans, shift_to_end + 1)
            
            # Alternative fallback (reverse then shift)
            ans = min(ans, 1 + (n - 1 - zero_idx))
            
        return ans