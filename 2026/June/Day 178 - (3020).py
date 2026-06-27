# 3020. Find the Maximum Number of Elements in Subset

# You are given an array of positive integers nums.
# You need to select a subset of nums which satisfies the following condition:
# You can place the selected elements in a 0-indexed array such that it follows the pattern: [x, x2, x4, ..., xk/2, xk, xk/2, ..., x4, x2, x] (Note that k can be be any non-negative power of 2). For example, [2, 4, 16, 4, 2] and [3, 9, 3] follow the pattern while [2, 4, 8, 4, 2] does not.
# Return the maximum number of elements in a subset that satisfies these conditions.

# Example 1:
# Input: nums = [5,4,1,2,2]
# Output: 3
# Explanation: We can select the subset {4,2,2}, which can be placed in the array as [2,4,2] which follows the pattern and 22 == 4. Hence the answer is 3.

# Example 2:
# Input: nums = [1,3,2,4]
# Output: 1
# Explanation: We can select the subset {1}, which can be placed in the array as [1] which follows the pattern. Hence the answer is 1. Note that we could have also selected the subsets {2}, {3}, or {4}, there may be multiple subsets which provide the same answer. 

# Constraints:
# 2 <= nums.length <= 105
# 1 <= nums[i] <= 109

from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Count the frequency of each number
        counts = Counter(nums)
        
        # Base case: minimum valid subset length is always 1
        max_len = 1
        
        # handeling the 1's (given infinite number of 1's and length array can be formed)
        if 1 in counts:
            ones_count = counts[1]
            # We can only use an odd number of 1s
            if ones_count % 2 == 0:
                max_len = max(max_len, ones_count - 1)
            else:
                max_len = max(max_len, ones_count)
        
        # form the chains and check
        for x in counts:
            if x == 1:
                continue
                
            current_len = 0
            current_val = x
            
            # Follow the chain of squares
            while current_val in counts:
                if counts[current_val] >= 2:
                    current_len += 2
                    current_val = current_val ** 2
                else:
                    # We only have 1 copy, it must be the peak of the mountain as no step down can occure
                    current_len += 1
                    break
            else:
                # If loop ends, then previous value was the peak as no next value exists
                current_len -= 1
                
            max_len = max(max_len, current_len)
            
        return max_len