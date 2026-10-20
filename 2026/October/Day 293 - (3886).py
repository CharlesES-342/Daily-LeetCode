# 3886. Sum of Sortable Integers

# You are given an integer array nums of length n.
# An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:
# Partition nums into consecutive subarrays of length k.
# Cyclically rotate each subarray independently any number of times to the left or to the right.
# Return an integer denoting the sum of all possible sortable integers k.

# Example 1:
# Input: nums = [3,1,2]
# Output: 3
# Explanation:​​​​​​​
# For n = 3, possible divisors are 1 and 3.
# For k = 1: each subarray has one element. No rotation can sort the array.
# For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.
# Only k = 3 is sortable. Hence, the answer is 3.

# Example 2:
# Input: nums = [7,6,5]
# Output: 0
# Explanation:
# For n = 3, possible divisors are 1 and 3.
# For k = 1: each subarray has one element. No rotation can sort the array.
# For k = 3: the single subarray [7, 6, 5] cannot be rotated into non-decreasing order.
# No k is sortable. Hence, the answer is 0.

# Example 3:
# Input: nums = [5,8]
# Output: 3
# Explanation:​​​​​​​
# For n = 2, possible divisors are 1 and 2.
# Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer is 1 + 2 = 3.

# Constraints:
# 1 <= n == nums.length <= 105
# 1 <= nums[i] <= 105

'''
The following approach did not work and resulted in a time limit ecceeded error.
'''
class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # need the divisors
        n = len(nums)
        sorted_nums = sorted(nums)

        # check if these sub arrays contains elements that can be in order
        def helper(block, sorted_block):
            double_block = block + block
            k = len(block)
            for j in range(k):
                if double_block[j : j + k] == sorted_block:
                    return True
            return False


        ans = 0

        # Default case to check that  n = k works aswell
        if helper(nums, sorted_nums):
            ans += n

        # compair adjoining blocks, check that the order is maintained over concatinated blocks
        for k in range(1, n // 2 +1):
            if n % k == 0:
                works = True
                for i in range(0, n, k):
                    original_block = nums[i : i + k]
                    sorted_block = sorted_nums[i : i + k]
                    
                    if not helper(original_block, sorted_block):
                        works = False
                        break
                
                if works:
                    ans += k
                                
        return ans

'''
The issue is the factors. By cycling throguh so many numbers, a factor is checked for every number. It is more efficnet
to determine the factors and then cycle throguh those. To do
this you can use the Square Root Factorisation method.
'''

class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Find all divisors of n using the square-root method
        fac = []
        for x in range(1, int(n ** 0.5) + 1):
            if n % x == 0:
                fac.append(x)
                if n // x != x:
                    fac.append(n // x)
                    
        target = sorted(nums)
        
        # KMP helper function to check if nums2 is a cyclic rotation of nums1
        def kmp(nums1, nums2):
            length1, length2 = len(nums1), len(nums2)
            pi = [0] * length2
            j = 0
            
            for i in range(1, length2):
                while j > 0 and nums2[i] != nums2[j]:
                    j = pi[j - 1]
                if nums2[i] == nums2[j]:
                    j += 1
                pi[i] = j
                
            j = 0
            for i in range(length1):
                while j > 0 and nums1[i] != nums2[j]:
                    j = pi[j - 1]
                if nums1[i] == nums2[j]:
                    j += 1
                if j == length2:
                    return True
            return False

        ans = 0
        
        # Check every valid divisor k
        for k in fac:
            works = True
            for i in range(0, n, k):
                original_block = nums[i : i + k]
                target_block = target[i : i + k]
                
                # Double the first block to check for all cyclic rotations via KMP
                if not kmp(original_block + original_block, target_block):
                    works = False
                    break
            
            if works:
                ans += k
                
        return ans