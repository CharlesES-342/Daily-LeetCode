# 3739. Count Subarrays With Majority Element II

# You are given an integer array nums and an integer target.
# Return the number of subarrays of nums in which target is the majority element.
# The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.

# Example 1:
# Input: nums = [1,2,2,3], target = 2
# Output: 5
# Explanation:
# Valid subarrays with target = 2 as the majority element:
# nums[1..1] = [2]
# nums[2..2] = [2]
# nums[1..2] = [2,2]
# nums[0..2] = [1,2,2]
# nums[1..3] = [2,2,3]
# So there are 5 such subarrays.

# Example 2:
# Input: nums = [1,1,1,1], target = 1
# Output: 10
# Explanation:
# ​​​​​​​All 10 subarrays have 1 as the majority element.

# Example 3:
# Input: nums = [1,2,3], target = 4
# Output: 0
# Explanation:
# target = 4 does not appear in nums at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.

# Constraints:
# 1 <= nums.length <= 10​​​​​​​5
# 1 <= nums[i] <= 10​​​​​​​9
# 1 <= target <= 109

class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        
        # Transform the elements into +1 and -1 (+1 for the target, -1 othrewise)
        transformed = [1 if x == target else -1 for x in nums]
        
        # Form the prefix sum array (size n + 1)
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + transformed[i - 1]
            
        # Coordinate compression (Hint 4) - assing each weight a position
        unique_vals = sorted(list(set(pref)))
        ranks = {val: idx + 1 for idx, val in enumerate(unique_vals)}
        
        # Fenwick Tree (Binary Indexed Tree - Hint 4) Implementation
        tree_size = len(ranks)
        bit = [0] * (tree_size + 1)
        
        def update(idx, val):
            while idx <= tree_size:
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        # Count pairs (i < j) where pref[j] > pref[i]
        count = 0
        for v in pref:
            rank = ranks[v]
            # Query how many previous elements have a strictly smaller rank
            count += query(rank - 1)
            # Add the current element's rank to the Fenwick Tree
            update(rank, 1)
            
        return count