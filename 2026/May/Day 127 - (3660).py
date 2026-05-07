# 3660. Jump Game IX

# You are given an integer array nums.
# From any index i, you can jump to another index j under the following rules:
# Jump to index j where j > i is allowed only if nums[j] < nums[i].
# Jump to index j where j < i is allowed only if nums[j] > nums[i].
# For each index i, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at i.
# Return an array ans where ans[i] is the maximum value reachable starting from index i.

# Example 1:
# Input: nums = [2,1,3]
# Output: [2,2,3]
# Explanation:
# For i = 0: No jump increases the value.
# For i = 1: Jump to j = 0 as nums[j] = 2 is greater than nums[i].
# For i = 2: Since nums[2] = 3 is the maximum value in nums, no jump increases the value.
# Thus, ans = [2, 2, 3].

# Example 2:
# Input: nums = [2,3,1]
# Output: [3,3,3]
# Explanation:
# For i = 0: Jump forward to j = 2 as nums[j] = 1 is less than nums[i] = 2, then from i = 2 jump to j = 1 as nums[j] = 3 is greater than nums[2].
# For i = 1: Since nums[1] = 3 is the maximum value in nums, no jump increases the value.
# For i = 2: Jump to j = 1 as nums[j] = 3 is greater than nums[2] = 1.
# Thus, ans = [3, 3, 3].

# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109

class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # jump forward given the number is less
        # or jump back where the number is more
        # while you cant move forward if the value is more, you can move back to a number that
        # is more and then move formward again to a lower number, and so on ...

        # for each component that is greater in the prefix than a value in the suffix, assign all
        # intermediary positions this as their max atainable value. Repeat this for every position
        # (taking the max of the prefix and min of the suffix), updating the answer acordingly -
        # incase a later occurence is within those bounds, add the value for that too

        n = len(nums)
        if n == 0:
            return []

        # 1. Precompute Prefix Maximums - up to a point what is the max value possible
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])

        # 2. Precompute Suffix Minimums - up to a point, what is the minimum value possible
        suffix_min = [0] * n
        suffix_min[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])

        ans = [0] * n
        start = 0
        
        # 3. Identify segments and fill the answer
        while start < n:
            end = start
            # A component continues as long as a value on the left 
            # is strictly greater than a value on the right.
            while end < n - 1 and prefix_max[end] > suffix_min[end + 1]:
                end += 1
            
            # Find the maximum value in this connected component
            current_max = 0
            for k in range(start, end + 1):
                if nums[k] > current_max:
                    current_max = nums[k]
            
            # Fill the segment in the answer array
            for k in range(start, end + 1):
                ans[k] = current_max
                
            start = end + 1

        return ans
            

# definetely more confusig than I intially thought, but in considering it as an undirected graph,
# we can see that the maximum value reachable from a position is the maximum value in the connected
# component.