# 2916. Subarrays Distinct Element Sum of Squares II

# You are given a 0-indexed integer array nums.
# The distinct count of a subarray of nums is defined as:
# Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
# Return the sum of the squares of distinct counts of all subarrays of nums.
# Since the answer may be very large, return it modulo 109 + 7.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,2,1]
# Output: 15
# Explanation: Six possible subarrays are:
# [1]: 1 distinct value
# [2]: 1 distinct value
# [1]: 1 distinct value
# [1,2]: 2 distinct values
# [2,1]: 2 distinct values
# [1,2,1]: 2 distinct values
# The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

# Example 2:
# Input: nums = [2,2]
# Output: 3
# Explanation: Three possible subarrays are:
# [2]: 1 distinct value
# [2]: 1 distinct value
# [2,2]: 1 distinct value
# The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.

# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # segment tree
        # starting at i, to go from i to i+1 elements you gain the previosu number of sub array answers again (for each you can choose to keep or eclude that character)
        
        MOD = 10**9 + 7
        n = len(nums)
        
        # Segment tree arrays
        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push(node, l, r):
            if lazy[node] != 0:
                val = lazy[node]
                mid = (l + r) // 2
                
                # Update left child
                lazy[2 * node] = (lazy[2 * node] + val) % MOD
                tree[2 * node] = (tree[2 * node] + val * (mid - l + 1)) % MOD
                
                # Update right child
                lazy[2 * node + 1] = (lazy[2 * node + 1] + val) % MOD
                tree[2 * node + 1] = (tree[2 * node + 1] + val * (r - mid)) % MOD
                
                lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                tree[node] = (tree[node] + val * (r - l + 1)) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return
            
            push(node, l, r)
            mid = (l + r) // 2
            update(2 * node, l, mid, ql, qr, val)
            update(2 * node + 1, mid + 1, r, ql, qr, val)
            tree[node] = (tree[2 * node] + tree[2 * node + 1]) % MOD

        def query(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 0
            if ql <= l and r <= qr:
                return tree[node]
            
            push(node, l, r)
            mid = (l + r) // 2
            return (query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr)) % MOD

        last = {}
        ans = 0
        current_sum_squares = 0
        
        for i in range(n):
            x = nums[i]
            prev_idx = last.get(x, -1)
            
            # The range [prev_idx + 1, i] gets its distinct count incremented by 1.
            # This adds 2 * sum(counts) + length to the sum of squares.
            sum_val = query(1, 0, n - 1, prev_idx + 1, i)
            length = i - (prev_idx + 1) + 1
            
            added = (2 * sum_val + length) % MOD
            current_sum_squares = (current_sum_squares + added) % MOD
            
            # Apply range update to segment tree
            update(1, 0, n - 1, prev_idx + 1, i, 1)
            
            last[x] = i
            ans = (ans + current_sum_squares) % MOD
            
        return ans