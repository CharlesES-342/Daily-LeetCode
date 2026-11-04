# 3505. Minimum Operations to Make Elements Within K Subarrays Equal

# You are given an integer array nums and two integers, x and k. You can perform the following operation any number of times (including zero):
# Increase or decrease any element of nums by 1.
# Return the minimum number of operations needed to have at least k non-overlapping subarrays of size exactly x in nums, where all elements within each subarray are equal.

# Example 1:
# Input: nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2
# Output: 8
# Explanation:
# Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
# Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
# Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.

# Example 2:
# Input: nums = [9,-2,-2,-2,1,5], x = 2, k = 2
# Output: 3
# Explanation:
# Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2, -2, -2, -2, 5].
# Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and [-2, -2] (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.

# Constraints:
# 2 <= nums.length <= 105
# -106 <= nums[i] <= 106
# 2 <= x <= nums.length
# 1 <= k <= 15
# 2 <= k * x <= nums.length

class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        # use x as a sliding window size
        # the split between the k sub arrays has to be x (for starting index)

        # for each location, determine the number of unique numbers (out of x (at most x)) -> O(n)
        #   determine the median and calculate the distance all numbers are overall from the median (+/- how far each number is from this in the window and determine an overall OUTNESS quantity)

        # loop back through the array O(n) and determine if an answer exists already and if not get the minimum OUTNESS scores in order given the seporation is enough (take the k smallest compatable subarrays (given enough seporation between them))
        
        n = len(nums)
        INF = float('inf')
        if x * k > n:
            return -1  # not enough room (normally excluded by constraints)

        # ---- 1. coordinate compression + Fenwick trees (count and sum) ----
        vals = sorted(set(nums))
        m = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}  # 1-indexed
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def update(v, dc):
            i = rank[v]
            ds = dc * v
            while i <= m:
                cnt[i] += dc
                sm[i] += ds
                i += i & -i

        top = 1
        while top * 2 <= m:
            top *= 2

        kth = (x + 1) // 2  # median position within the window

        def window_cost(total):
            # binary descent: find the kth smallest, tracking the count/sum below it
            pos, c, s = 0, 0, 0
            step = top
            while step:
                nxt = pos + step
                if nxt <= m and c + cnt[nxt] < kth:
                    pos = nxt
                    c += cnt[nxt]
                    s += sm[nxt]
                step >>= 1
            med = vals[pos]  # 0-indexed value of the kth smallest
            # c/s = count/sum of elements strictly below the median value
            return med * c - s + (total - s) - med * (x - c)

        # ---- 2. cost of every window of size x ----
        num_windows = n - x + 1
        cost = [0] * num_windows
        total = 0
        for i in range(x):
            update(nums[i], 1)
            total += nums[i]
        cost[0] = window_cost(total)
        for i in range(1, num_windows):
            out_v, in_v = nums[i - 1], nums[i + x - 1]
            update(out_v, -1)
            update(in_v, 1)
            total += in_v - out_v
            cost[i] = window_cost(total)

        # ---- 3. DP: choose k non-overlapping windows with minimum total cost ----
        prev = [0] * (n + 1)  # j = 0 windows: cost 0 everywhere
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(j * x, n + 1):
                best = cur[i - 1]
                cand = prev[i - x] + cost[i - x]
                cur[i] = cand if cand < best else best
            prev = cur

        return prev[n]