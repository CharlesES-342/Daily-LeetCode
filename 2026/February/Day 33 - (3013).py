# 3013. Divide an Array into Subarrays with minimum Cost 2

# You are given a 0-indexed array of integers nums of length n, and two positive integers k and dist.
# The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.
# You need to divide nums into k disjoint contiguous subarrays, such that the difference between the starting index of the second
# subarray and the starting index of the kth subarray should be less than or equal to dist. In other words, if you divide nums into
# the subarrays nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ..., nums[ik-1..(n - 1)], then ik-1 - i1 <= dist.
# Return the minimum possible sum of the cost of these subarrays.


# Example 1:
# Input: nums = [1,3,2,6,4,2], k = 3, dist = 3
# Output: 5
# Explanation: The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because ik-1 - i1 is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
# It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.

# Example 2:
# Input: nums = [10,1,2,2,2,1], k = 4, dist = 3
# Output: 15
# Explanation: The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because ik-1 - i1 is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
# The division [10], [1], [2,2,2], and [1] is not valid, because the difference between ik-1 and i1 is 5 - 1 = 4, which is greater than dist.
# It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.

# Example 3:
# Input: nums = [10,8,18,9], k = 3, dist = 1
# Output: 36
# Explanation: The best possible way to divide nums into 4 subarrays is: [10], [8], and [18,9]. This choice is valid because ik-1 - i1 is 2 - 1 = 1 which is equal to dist.The total cost is nums[0] + nums[1] + nums[2] which is 10 + 8 + 18 = 36.
# The division [10], [8,18], and [9] is not valid, because the difference between ik-1 and i1 is 3 - 1 = 2, which is greater than dist.
# It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 36.


# Constraints:
# 3 <= n <= 105
# 1 <= nums[i] <= 109
# 3 <= k <= n
# k - 2 <= dist <= n - 2


from sortedcontainers import SortedList

class Container(object):
    def __init__(self, k):
        self.k = k
        self.st1 = SortedList()
        self.st2 = SortedList()
        self.sm = 0
        
    def adjust(self):
        # If st1 has too few elements, pull smallest from st2
        while len(self.st1) < self.k and len(self.st2) > 0:
            x = self.st2[0]
            self.st1.add(x)
            self.st2.remove(x)
            self.sm += x
        # If st1 has too many, push largest to st2
        while len(self.st1) > self.k:
            x = self.st1[-1]
            self.st2.add(x)
            self.st1.remove(x)
            self.sm -= x
            
    def add(self, x):
        if len(self.st2) > 0 and x >= self.st2[0]:
            self.st2.add(x) # if x is large
        else:
            self.st1.add(x) # if x is small
            self.sm += x
        self.adjust()#rebalance
        
    def erase(self, x): # removing elements from lists/heaps
        if x in self.st1:
            self.st1.remove(x)
            self.sm -= x
        elif x in self.st2:
            self.st2.remove(x)
        self.adjust()
        
    def sum(self):
        return self.sm

class Solution(object):
    def minimumCost(self, nums, k, dist):
        """
        :type nums: List[int]
        :type k: int
        :type dist: int
        :rtype: int
        """
        n = len(nums)
        cnt = Container(k - 2)
        
        # Initialize with first k-1 elements (indices 1 to k-1)
        for i in range(1, k - 1):
            cnt.add(nums[i])
        
        ans = cnt.sum() + nums[k - 1]
        
        # Slide the window
        for i in range(k, n):
            j = i - dist - 1
            if j > 0:
                cnt.erase(nums[j])
            cnt.add(nums[i - 1])
            ans = min(ans, cnt.sum() + nums[i])
        
        return ans + nums[0]
    
# I was very stuck on this one.

# =====INITIAL IDEA=====
# Initially, my thought was to use the approach from yesterdays problem, but addapt it for a varying difference (dist).
# the way I wanted to do this was to:
# 1. take the first element
# 2. for all remaining elements, sort them into a sorted list
# 3. go through teh list in order and ensure that the difference between teh element selected and the first element was atleast dist
# 4. repreate for the next element based on the last selected element
# Hoever, this approach woudl not work as it would not guarantee the minimum cost for a combination, for example:
# nums = [1, 100, 1, 1, 1], k = 3, dist = 2
# Using my approach, I would select 1, 1, 1 for a total cost of 3
# However, the optimal solution is 1, 100, 1 for a total cost of 2
# Thus, I had to rethink my approach.

# =====SECOND APPROACH=====
# I then thought to make use of a sliging window approach, where I would maintain a window of size dist
# I would then use a min-heap to keep track of the smallest k-2 elements
# This would allow me to efficiently get the smallest k-2 elements within the window
# However, the issue with this approach is that heaps do not support efficient removal of arbitrary elements
# I thought of using a lazy removal approach to hasndle removals without actually performing them

# =====FINAL APPROACH=====
# Use a sliding window with two sorted sets (Container class):
# - Maintain k-2 smallest elements from the valid window efficiently
# - st1 holds exactly k-2 smallest, st2 holds the rest
# - As we slide, remove elements that fall outside [i-dist, i-1] window
# - Add new candidates as they enter the window
# - Track sum of st1 for O(1) cost calculation
# Time: O(n log n), Space: O(dist)

# =====OVERALL=====
# I woulod not have gotten this approach on my own, and had to look at the examople solution to get an appropriate method of solving
# I would not have gotten this far on my own.
