# 3876. Construct Uniform Parity Array II

# You are given an array nums1 of n distinct integers.
# You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.
# For each index i, you must choose exactly one of the following (in any order):
# nums2[i] = nums1[i]​​​​​​​
# nums2[i] = nums1[i] - nums1[j], for an index j != i, such that nums1[i] - nums1[j] >= 1
# Return true if it is possible to construct such an array, otherwise return false.

# Example 1:
# Input: nums1 = [1,4,7]
# Output: true
# Explanation:​​​​​​​​​​​​​​
# Set nums2[0] = nums1[0] = 1.
# Set nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3.
# Set nums2[2] = nums1[2] = 7.
# nums2 = [1, 3, 7], and all elements are odd. Thus, the answer is true.

# Example 2:
# Input: nums1 = [2,3]
# Output: false
# Explanation:
# It is not possible to construct nums2 such that all elements have the same parity. Thus, the answer is false.

# Example 3:
# Input: nums1 = [4,6]
# Output: true
# Explanation:
# Set nums2[0] = nums1[0] = 4.
# Set nums2[1] = nums1[1] = 6.
# nums2 = [4, 6], and all elements are even. Thus, the answer is true.

# Constraints:
# 1 <= n == nums1.length <= 105
# 1 <= nums1[i] <= 109
# nums1 consists of distinct integers.

class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # Check if all elements already have the same parity
        f = nums1[0] % 2
        all_same = True
        for i in nums1:
            if i % 2 != f:
                all_same = False
                break
        
        if all_same:
            return True

        # If parities are mixed, all elements must be made odd (it cant be even becuase this requires teh smallest odd to have a smaller odd, this is not possible -> this is becuase of the transition rule "nums2[1] = nums1[1] - nums1[0]": smallest_odd - smaller_odd = new_odd (this is not possible you cant have something smaller than the smallest otherwwwise it was never the smallest))
        # Find the minimum odd number in the array.
        min_odd = float('inf')
        for i in nums1:
            if i % 2 != 0:
                if i < min_odd:
                    min_odd = i

        # Check if there is any even number smaller than the minimum odd number (if it exists, it can never be made odd)
        for i in nums1:
            if i % 2 == 0:
                if i < min_odd:
                    return False

        return True