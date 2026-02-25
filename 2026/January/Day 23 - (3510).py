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

import heapq

class Solution(object):
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        
        # Doubly linked list
        nxt = list(range(1, n + 1))
        prv = list(range(-1, n - 1))
        
        # Track which elements have been merged
        merged = [False] * n
        
        # Count decreasing adjacent pairs
        decrease_count = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                decrease_count += 1
        
        if decrease_count == 0:
            return 0
        
        # Min heap: (sum, left_index, right_index, nums[left], nums[right])
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i, i + 1, nums[i], nums[i + 1]))
        
        operations = 0
        
        while decrease_count > 0:
            # Pop until we find a valid pair
            while heap:
                pair_sum, i, j, val_i, val_j = heapq.heappop(heap)
                
                # Check if this is dirty data
                # 1. Both elements must not be merged
                if merged[i] or merged[j]:
                    continue
                
                # 2. They must still be adjacent
                if nxt[i] != j:
                    continue
                
                # 3. The sum should match (or if it matches, it's valid even if dirty)
                if nums[i] + nums[j] != pair_sum:
                    continue
                
                # Valid pair found!
                # Calculate decrease_count changes
                
                # Case 1: If (i, j) was decreasing, remove that violation
                if nums[i] > nums[j]:
                    decrease_count -= 1
                
                # Case 2: Check left neighbor (i-1, i)
                prev_i = prv[i]
                if prev_i != -1 and not merged[prev_i]:
                    was_decreasing = nums[prev_i] > nums[i]
                    will_be_decreasing = nums[prev_i] > (nums[i] + nums[j])
                    
                    if was_decreasing and not will_be_decreasing:
                        decrease_count -= 1
                    elif not was_decreasing and will_be_decreasing:
                        decrease_count += 1
                
                # Case 3: Check right neighbor (j, j+1)
                next_j = nxt[j]
                if next_j < n and not merged[next_j]:
                    was_decreasing = nums[j] > nums[next_j]
                    will_be_decreasing = (nums[i] + nums[j]) > nums[next_j]
                    
                    if was_decreasing and not will_be_decreasing:
                        decrease_count -= 1
                    elif not was_decreasing and will_be_decreasing:
                        decrease_count += 1
                
                # Merge: always merge to the left (i)
                nums[i] = nums[i] + nums[j]
                merged[j] = True
                
                # Update linked list
                nxt[i] = next_j
                if next_j < n:
                    prv[next_j] = i
                
                operations += 1
                
                # Add new pairs to heap
                # Left pair: (prev_i, i)
                if prev_i != -1 and not merged[prev_i]:
                    heapq.heappush(heap, (nums[prev_i] + nums[i], prev_i, i, nums[prev_i], nums[i]))
                
                # Right pair: (i, next_j)
                if next_j < n and not merged[next_j]:
                    heapq.heappush(heap, (nums[i] + nums[next_j], i, next_j, nums[i], nums[next_j]))
                
                break
        
        return operations