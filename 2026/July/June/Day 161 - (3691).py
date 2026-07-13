# 3691. Maximum Total Subarray Value II

# You are given an integer array nums of length n and an integer k.
# You must select exactly k distinct subarrays nums[l..r] of nums. Subarrays may overlap, but the exact same subarray (same l and r) cannot be chosen more than once.
# The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]).
# The total value is the sum of the values of all chosen subarrays.
# Return the maximum possible total value you can achieve.

# Example 1:
# Input: nums = [1,3,2], k = 2
# Output: 4
# Explanation:
# One optimal approach is:
# Choose nums[0..1] = [1, 3]. The maximum is 3 and the minimum is 1, giving a value of 3 - 1 = 2.
# Choose nums[0..2] = [1, 3, 2]. The maximum is still 3 and the minimum is still 1, so the value is also 3 - 1 = 2.
# Adding these gives 2 + 2 = 4.

# Example 2:
# Input: nums = [4,2,5,1], k = 3
# Output: 12
# Explanation:
# One optimal approach is:
# Choose nums[0..3] = [4, 2, 5, 1]. The maximum is 5 and the minimum is 1, giving a value of 5 - 1 = 4.
# Choose nums[1..3] = [2, 5, 1]. The maximum is 5 and the minimum is 1, so the value is also 4.
# Choose nums[2..3] = [5, 1]. The maximum is 5 and the minimum is 1, so the value is again 4.
# Adding these gives 4 + 4 + 4 = 12.

# Constraints:
# 1 <= n == nums.length <= 5 * 10​​​​​​​4
# 0 <= nums[i] <= 109
# 1 <= k <= min(105, n * (n + 1) / 2)

'''
I had no idea how to do this problem and the hints were no help, so I looked at the editorial and fed it
into Gemini.ai to form the following code.
How it works:
1. as you increase the window size, you can only increase the value of the subarray (differences)
2. step back from the end k times, adding them to the stack
3. To make this heap approach viable, we must be able to calculate max(nums[l..r]) -
    min(nums[l..r]) instantly. Doing a standard loop to find the min and max takes O(n)
    time, which is too slow.A Sparse Table is a static data structure that precomputes
    range queries in O(n \log n) time, allowing us to find the max and min of any range in
    O(1) time using powers of 2.
'''
import heapq

class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0 or k == 0:
            return 0
        
        # 1. Precompute log values to enable O(1) sparse table queries
        LOG = [0] * (n + 1)
        for i in range(2, n + 1):
            LOG[i] = LOG[i // 2] + 1
            
        max_power = LOG[n] + 1
        
        # 2. Build the Sparse Tables for both Min and Max queries
        stMax = [[0] * max_power for _ in range(n)]
        stMin = [[0] * max_power for _ in range(n)]
        
        for i in range(n):
            stMax[i][0] = nums[i]
            stMin[i][0] = nums[i]
            
        for j in range(1, max_power):
            for i in range(n - (1 << j) + 1):
                stMax[i][j] = max(stMax[i][j-1], stMax[i + (1 << (j-1))][j-1])
                stMin[i][j] = min(stMin[i][j-1], stMin[i + (1 << (j-1))][j-1])
        
        # Helper function to get the value of a subarray in O(1) time
        def get_subarray_value(l, r):
            j = LOG[r - l + 1]
            mx = max(stMax[l][j], stMax[r - (1 << j) + 1][j])
            mn = min(stMin[l][j], stMin[r - (1 << j) + 1][j])
            return mx - mn

        # 3. Seed the Max Heap with the absolute maximum of each sequence (r = n - 1)
        max_heap = []
        for l in range(n):
            r = n - 1
            val = get_subarray_value(l, r)
            # Invert val for max-heap behaviour
            heapq.heappush(max_heap, (-val, l, r))
            
        total_value_sum = 0
        
        # 4. Extract the top k largest distinct subarray values
        for _ in range(k):
            if not max_heap:
                break
                
            neg_val, l, r = heapq.heappop(max_heap)
            total_value_sum += (-neg_val)
            
            # If the sequence can step backward to the left, push the next candidate
            if r > l:
                next_r = r - 1
                next_val = get_subarray_value(l, next_r)
                heapq.heappush(max_heap, (-next_val, l, next_r))
                
        return total_value_sum