# 3640. Trionic Array II
# You are given an integer array nums of length n.
# A trionic subarray is a contiguous subarray nums[l...r] (with 0 <= l < r < n) for which there exist indices l < p < q < r such that:
# nums[l...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...r] is strictly increasing.
# Return the maximum sum of any trionic subarray in nums.


# Example 1:
# Input: nums = [0,-2,-1,-3,0,2,-1]
# Output: -4
# Explanation:
# Pick l = 1, p = 2, q = 3, r = 5:
# nums[l...p] = nums[1...2] = [-2, -1] is strictly increasing (-2 < -1).
# nums[p...q] = nums[2...3] = [-1, -3] is strictly decreasing (-1 > -3)
# nums[q...r] = nums[3...5] = [-3, 0, 2] is strictly increasing (-3 < 0 < 2).
# Sum = (-2) + (-1) + (-3) + 0 + 2 = -4.

# Example 2:
# Input: nums = [1,4,2,7]
# Output: 14
# Explanation:
# Pick l = 0, p = 1, q = 2, r = 3:
# nums[l...p] = nums[0...1] = [1, 4] is strictly increasing (1 < 4).
# nums[p...q] = nums[1...2] = [4, 2] is strictly decreasing (4 > 2).
# nums[q...r] = nums[2...3] = [2, 7] is strictly increasing (2 < 7).
# Sum = 1 + 4 + 2 + 7 = 14.

# Constraints:
# 4 <= n = nums.length <= 105
# -109 <= nums[i] <= 109
# It is guaranteed that at least one trionic subarray exists.

class Solution(object):
    def maxSumTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = float("-inf")
        i = 0
        
        while i < n:
            j = i + 1
            res = 0
            
            #Phase 1: strictly increasing segment
            while j < n and nums[j - 1] < nums[j]:
                j += 1
            
            p = j - 1  #peak position
            if p == i:  #no valid increasing segment
                i += 1
                continue
            
            #Phase 2: strictly decreasing segment
            #include last 2 elements of phase 1 (mandatory for the pattern to be true)
            res += nums[p] + nums[p - 1]
            
            #add all elements in the decreasing segment
            while j < n and nums[j - 1] > nums[j]:
                res += nums[j]
                j += 1
            
            q = j - 1  # valley position
            
            #check if we have a valid decreasing segment AND valid start of phase 3
            if q == p or q == n - 1 or (j < n and nums[j] <= nums[q]):
                i = q
                continue
            
            #Phase 3: strictly increasing segment
            #add the first element of phase 3 (mandatory)
            res += nums[q + 1]
            
            #find the maximum prefix sum from the rest of phase 3
            max_sum = 0
            curr_sum = 0
            k = q + 2
            while k < n and nums[k] > nums[k - 1]:
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)
                k += 1
            res += max_sum
            
            #find the maximum suffix sum from the rest of phase 1
            max_sum = 0
            curr_sum = 0
            for k in range(p - 2, i - 1, -1):
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)
            res += max_sum
            
            #update answer
            ans = max(ans, res)
            
            #jump to valley position for next iteration
            i = q
        
        return ans
    
    #The overall principle is to find the 3 segments, and then try to expand them as much as possible to get the maximum sum
    # find a segment that is strictly increasing, then find a segment that is strictly decreasing, then find a segment that is strictly increasing
    # by including all of teh 2nd segment, find the maximum possilbe first and last segments to add to this, and update the answer
    # following this, given you have already found the next decreasing segment (from finding the end of the increasing segment), you can jump to the end of the decreasing segment to start the next
    # iteration, as you know that the next trionic subarray must start after this

    # this allows you to jump around, making it slightly faster than just iterating through every possible starting point, and then finding the 3 segments from there
    # this method allows you to form view atmost each element 2 times
        # one for passing through to find the segments
        # and one for calculating the sum of the segments
    #This results in:
    #  Time Complexity - O(n)
    #  Space Complexity - O(1)