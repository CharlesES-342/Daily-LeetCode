# 2333. Minimum Sum of Squared Difference

# You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.
# The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.
# You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.
# Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.
# Note: You are allowed to modify the array elements to become negative integers.

# Example 1:
# Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
# Output: 579
# Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. 
# The sum of square difference will be: (1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)2 = 579.

# Example 2:
# Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
# Output: 43
# Explanation: One way to obtain the minimum sum of square difference is: 
# - Increase nums1[0] once.
# - Increase nums2[2] once.
# The minimum of the sum of square difference will be: 
# (2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
# Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.

# Constraints:
# n == nums1.length == nums2.length
# 1 <= n <= 105
# 0 <= nums1[i], nums2[i] <= 105
# 0 <= k1, k2 <= 109

import collections

class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        n = len(nums1)
        total_k = k1 + k2
        
        # Calculate initial differences and count frequencies
        diff_counts = collections.defaultdict(int)
        max_diff = 0
        total_difference_sum = 0
        
        for i in range(n):
            d = abs(nums1[i] - nums2[i])
            if d > 0:
                diff_counts[d] += 1
                max_diff = max(max_diff, d)
                total_difference_sum += d
                
        # Base Case: return 0 if the total difference sum <= K
        if total_difference_sum <= total_k:
            return 0
            
        # Greedily reduce the largest differences using available operations
        current_diff = max_diff
        while total_k > 0 and current_diff > 0:
            if current_diff not in diff_counts:
                current_diff -= 1
                continue
                
            count = diff_counts[current_diff]
            
            # If we have enough K to reduce this entire group of max differences by 1
            if total_k >= count:
                total_k -= count
                diff_counts[current_diff] = 0
                diff_counts[current_diff - 1] += count
                current_diff -= 1
            else:
                # Partial reduction using the remaining K
                diff_counts[current_diff] -= total_k
                diff_counts[current_diff - 1] += total_k
                total_k = 0
                
        # Calculate the final sum of squared differences and return it
        result = 0
        for d, count in diff_counts.items():
            result += (d ** 2) * count
            
        return result

'''
All of the above code was written by gemini.ai, however all code prompts for structure were my own,
I just didn't want to type.
Prompt:
    Please give me the code for this question based on... Combine k1 and k2 into one K as these
    overall operations can be written in different ways. Determine the difference between the two
    arrays. Sort these and startin from the largest element, redice the difference by 1, and
    reduce K by 1. Continue this (even over new largest differences). Then calculate the result
    based on this final new difference.
    Also, add the base case at the beginning where if the total differences at the beiginning <=
    the total K, then return 0.
'''