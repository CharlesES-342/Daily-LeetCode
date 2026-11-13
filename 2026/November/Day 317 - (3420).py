# 3420. Count Non-Decreasing Subarrays After K Operations

# You are given an array nums of n integers and an integer k.
# For each subarray of nums, you can apply up to k operations on it. In each operation, you increment any element of the subarray by 1.
# Note that each subarray is considered independently, meaning changes made to one subarray do not persist to another.
# Return the number of subarrays that you can make non-decreasing ​​​​​after performing at most k operations.
# An array is said to be non-decreasing if each element is greater than or equal to its previous element, if it exists.

# Example 1:
# Input: nums = [6,3,1,2,4,4], k = 7
# Output: 17
# Explanation:
# Out of all 21 possible subarrays of nums, only the subarrays [6, 3, 1], [6, 3, 1, 2], [6, 3, 1, 2, 4] and [6, 3, 1, 2, 4, 4] cannot be made non-decreasing after applying up to k = 7 operations. Thus, the number of non-decreasing subarrays is 21 - 4 = 17.

# Example 2:
# Input: nums = [6,3,1,3,6], k = 4
# Output: 12
# Explanation:
# The subarray [3, 1, 3, 6] along with all subarrays of nums with three or fewer elements, except [6, 3, 1], can be made non-decreasing after k operations. There are 5 subarrays of a single element, 4 subarrays of two elements, and 2 subarrays of three elements except [6, 3, 1], so there are 1 + 5 + 4 + 2 = 12 subarrays that can be made non-decreasing.

# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109

from collections import deque


class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        # prefix sums so any segment sum is O(1)
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]

        def seg(s, e):
            # cost of raising every element in [s, e] up to nums[s]
            return nums[s] * (e - s + 1) - (P[e + 1] - P[s])

        # l moves right-to-left; adding elements on the left can only increase
        #   the cost, so the best right end r only moves left.
        # The deque holds the "record" indices (prefix maximums starting at l).
        #   Each record covers up to the next record (or r), and costs seg() of that range.
        dq = deque()
        cost = 0
        r = n - 1
        ans = 0

        for l in range(n - 1, -1, -1):
            # records that nums[l] beats are no longer records, so remove their cost
            while dq and nums[dq[0]] <= nums[l]:
                end = dq[1] - 1 if len(dq) > 1 else r
                cost -= seg(dq[0], end)
                dq.popleft()

            # nums[l] becomes a record and covers up to the next record (or r)
            end = dq[0] - 1 if dq else r
            cost += seg(l, end)
            dq.appendleft(l)

            # too expensive: shrink the window from the right
            while cost > k:
                cost -= nums[dq[-1]] - nums[r]  # drop nums[r]'s contribution
                if dq[-1] == r:
                    dq.pop()
                r -= 1

            # every subarray [l..r'] with r' <= r is also valid
            ans += r - l + 1

        return ans
    
'''
I looked at the hints to get an idea for an apropriate approach. However, I tought I could do better.
Using an expanding window to track if the cost is atmost k. 
By forming a large subarray that is valid, also includes sub-arrays that are also valid. As a result,
determien the maximum size and add them. move along the window for each.
'''

# someone else approach
from collections import deque
class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        q = deque()
        cost = 0
        r = n-1
        ans = 0

        for l in range(n-1,-1,-1):
            x = nums[l]

            while q and nums[q[0]]<=x:
                j = q.popleft()
                end = q[0] if q else r+1
                cost += (x - nums[j]) * (end - j)
            q.appendleft(l)

            while cost > k:
                cost -= nums[q[-1]] - nums[r]  
                if q[-1] == r:
                    q.pop()                 
                r -= 1

            ans += r - l + 1
        return ans
'''
Why is this better: O(n) time, O(n) space.
  - Brute force checks every subarray and its cost: O(n^2) subarrays (O(n^3) if the cost is recomputed each time).
  - Sparse table can't merge two blocks in O(1) (right block's cost depends on the left block's max), so O(n log n) at best.
  - Here, l moves right-to-left exactly once, and r only ever moves left, so r moves at most n times in total.
  - Each index is pushed onto the deque once (appendleft) and popped at most once
    (popleft when a bigger value beats it, or pop when r passes it).
  - So the while loops do O(n) total work across the whole run (amortized O(1) per step), and the cost is updated
    incrementally instead of recomputed.
'''