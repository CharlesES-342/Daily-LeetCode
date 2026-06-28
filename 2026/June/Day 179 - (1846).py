# 1846. Maximum Element After Decreasing and Rearranging

# You are given an array of positive integers arr. Perform some operations (possibly none) on arr so that it satisfies these conditions:
# The value of the first element in arr must be 1.
# The absolute difference between any 2 adjacent elements must be less than or equal to 1. In other words, abs(arr[i] - arr[i - 1]) <= 1 for each i where 1 <= i < arr.length (0-indexed). abs(x) is the absolute value of x.
# There are 2 types of operations that you can perform any number of times:
# Decrease the value of any element of arr to a smaller positive integer.
# Rearrange the elements of arr to be in any order.
# Return the maximum possible value of an element in arr after performing the operations to satisfy the conditions.

# Example 1:
# Input: arr = [2,2,1,2,1]
# Output: 2
# Explanation: 
# We can satisfy the conditions by rearranging arr so it becomes [1,2,2,2,1].
# The largest element in arr is 2.

# Example 2:
# Input: arr = [100,1,1000]
# Output: 3
# Explanation: 
# One possible way to satisfy the conditions is by doing the following:
# 1. Rearrange arr so it becomes [1,100,1000].
# 2. Decrease the value of the second element to 2.
# 3. Decrease the value of the third element to 3.
# Now arr = [1,2,3], which satisfies the conditions.
# The largest element in arr is 3.

# Example 3:
# Input: arr = [1,2,3,4,5]
# Output: 5
# Explanation: The array already satisfies the conditions, and the largest element is 5.

# Constraints:
# 1 <= arr.length <= 105
# 1 <= arr[i] <= 109

class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # to get the minimum difference, order them (then they can only increase)
        #arr.sort() # the largest gap between 2 elements is the smallest possible (given then all increase the minimum gap is maintained)

        #now to make the difference at most 1
        # 1. divide to ensure the first element is 1 (dividing by itself)
        # 2. perform adequate reductions to minimise the array
        
        # all of this can be simplified
        # given an array, the max value that can be formed
        # this is not the maximum of unique values as this can be hindered as the numbers can't be increaed (for the same reason this does not work for the total number of values)

        arr.sort()
        
        # The first element must be 1, so the maximum possible value at index 0 is 1.
        Max = 1 
        
        # Start checking from the second element (index 1)
        for i in range(1, len(arr)):
            if arr[i] >= Max + 1:
                Max += 1
                
        return Max