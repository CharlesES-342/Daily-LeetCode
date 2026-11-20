#3510. Minimum Pair Removal to Sort Array 2

# Given an array nums, you can perform the following operation any number of times:

# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.

# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).



# Example 1:
# Input: nums = [5,2,3,1]
# Output: 2
# Explanation:
# The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# The array nums became non-decreasing in two operations.

# Example 2:
# Input: nums = [1,2,2]
# Output: 0
# Explanation:
# The array nums is already sorted.


# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109











#APPRAOCH 1:
# my initial idea was to use a greedy approach, but this was too ineficient as poping
# an element from the middle of a list is O(n)

#APPROACH 2:
# to rectify the isses from APPRACH 1, I used a set 'removed' to keep track of unused
# spaces reather than remove them to reduce time
# but this still resulted in a Time Limit Exceeded error

# after many queries with Claude, I found out that the problem can be solved


# OVERVIEW:
# using a doubly linked list we can keep track of the elements and their neighbors
# using a min heap, we can always get the minimum sum pair in O(log n) time
#   this stores the lement, its neighbor and the locaitons of both of these elements
#  when it comes to solving:
# 1. count the number of invalid data points in the heap (where nums[i] < nums[j], where j>i) - not in non-decreasing order
# 2. while there are invalid data points:
#   a. pop from the heap until we find a valid pair (not dirty data)
#   b. when a valid pair is found, we check how many invalid data points are removed or added
#      by merging this pair
#  c. merge the pair, update the linked list and add new pairs to the heap
#      since there can be multiple incorrectly ordered pairs next to eahother (even after an addition), we need to check of the new
#      merged element creates or removes invalid data points with both its left and right neighbors
# 3. return the number of operations performed
# COMPLEXITY:
# Time: O(n log n) - each element is added to the heap at most twice

# I would like to thank Claude for helping me come up with this solution as I beleive that I would never have come up with it on my own,
# especially using a min heap in this solution. I undertand teh practice and how each part works indepndently, and how it combines together
# into the time complexity, however, my knowledge would have lead me to be wrong in terms of how I could use heaps and how they would not
# impeed on the time complexity of the solution to the extent that I first beleived.
