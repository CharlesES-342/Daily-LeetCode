# 3721. Longest Balanced Subarray II

# A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.
# Return the length of the longest balanced subarray.

# Example 1:
# Input: nums = [2,5,4,3]
# Output: 4
# Explanation:
# The longest balanced subarray is [2, 5, 4, 3].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.

# Example 2:
# Input: nums = [3,2,2,5,4]
# Output: 5
# Explanation:
# The longest balanced subarray is [3, 2, 2, 5, 4].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.

# Example 3:
# Input: nums = [1,2,3,2]
# Output: 3

# Explanation:
# The longest balanced subarray is [2, 3, 2].
# It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.

# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

from collections import defaultdict, deque

class LazyTag:
    """Represents a lazy propagation tag for range updates"""
    def __init__(self):
        self.to_add = 0  # Value to add to a range
    
    def add(self, other):
        """Combine this tag with another tag"""
        self.to_add += other.to_add
        return self
    
    def has_tag(self):
        """Check if this tag has a pending update"""
        return self.to_add != 0
    
    def clear(self):
        """Clear the tag after applying it"""
        self.to_add = 0

class SegmentTreeNode:
    """Node in the segment tree storing min/max values and lazy tag"""
    def __init__(self):
        self.min_value = 0  # Minimum value in this segment
        self.max_value = 0  # Maximum value in this segment
        self.lazy_tag = LazyTag()  # Pending updates for this segment

class SegmentTree:
    """Segment tree with lazy propagation supporting range add and range query"""
    def __init__(self, data):
        self.n = len(data)
        # Allocate 4n nodes for the segment tree
        self.tree = [SegmentTreeNode() for _ in range(self.n * 4 + 1)]
        # Build the tree from initial data (1-indexed)
        self._build(data, 1, self.n, 1)
    
    def add(self, l, r, val):
        """Add 'val' to all positions in range [l, r] (1-indexed)"""
        tag = LazyTag()
        tag.to_add = val
        self._update(l, r, tag, 1, self.n, 1)
    
    def find_last(self, start, val):
        """Find the rightmost position >= start where the value equals 'val'"""
        if start > self.n:
            return -1
        return self._find(start, self.n, val, 1, self.n, 1)
    
    def _apply_tag(self, i, tag):
        """Apply a lazy tag to node i"""
        self.tree[i].min_value += tag.to_add
        self.tree[i].max_value += tag.to_add
        self.tree[i].lazy_tag.add(tag)
    
    def _pushdown(self, i):
        """Push lazy tag from node i to its children"""
        if self.tree[i].lazy_tag.has_tag():
            tag = LazyTag()
            tag.to_add = self.tree[i].lazy_tag.to_add
            # Apply to left child (i << 1)
            self._apply_tag(i << 1, tag)
            # Apply to right child ((i << 1) | 1)
            self._apply_tag((i << 1) | 1, tag)
            self.tree[i].lazy_tag.clear()
    
    def _pushup(self, i):
        """Update node i based on its children's values"""
        self.tree[i].min_value = min(
            self.tree[i << 1].min_value, self.tree[(i << 1) | 1].min_value
        )
        self.tree[i].max_value = max(
            self.tree[i << 1].max_value, self.tree[(i << 1) | 1].max_value
        )
    
    def _build(self, data, l, r, i):
        """Build segment tree from data array, covering range [l, r] at node i"""
        if l == r:
            # Leaf node - store the value (data is 0-indexed, l is 1-indexed)
            self.tree[i].min_value = data[l - 1]
            self.tree[i].max_value = data[l - 1]
            return
        # Recursively build left and right subtrees
        mid = l + ((r - l) >> 1)
        self._build(data, l, mid, i << 1)
        self._build(data, mid + 1, r, (i << 1) | 1)
        self._pushup(i)
    
    def _update(self, target_l, target_r, tag, l, r, i):
        """Update range [target_l, target_r] with tag, current node covers [l, r]"""
        if target_l <= l and r <= target_r:
            # Current range completely within target range
            self._apply_tag(i, tag)
            return
        # Push down lazy tags before splitting
        self._pushdown(i)
        mid = l + ((r - l) >> 1)
        # Update left child if it overlaps with target range
        if target_l <= mid:
            self._update(target_l, target_r, tag, l, mid, i << 1)
        # Update right child if it overlaps with target range
        if target_r > mid:
            self._update(target_l, target_r, tag, mid + 1, r, (i << 1) | 1)
        # Update current node based on children
        self._pushup(i)
    
    def _find(self, target_l, target_r, val, l, r, i):
        """
        Find rightmost position in [target_l, target_r] where value equals 'val'
        Uses discrete intermediate value theorem: if val is in [min, max], it exists
        """
        # If val is not in the range [min, max], it doesn't exist here
        if self.tree[i].min_value > val or self.tree[i].max_value < val:
            return -1
        if l == r:
            # Leaf node - found it
            return l
        # Push down lazy tags before going deeper
        self._pushdown(i)
        mid = l + ((r - l) >> 1)
        # Search right child first (to find rightmost occurrence)
        if target_r >= mid + 1:
            res = self._find(target_l, target_r, val, mid + 1, r, (i << 1) | 1)
            if res != -1:
                return res
        # If not found in right, search left child
        if l <= target_r and mid >= target_l:
            return self._find(target_l, target_r, val, l, mid, i << 1)
        return -1

class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurrences = defaultdict(deque)  # Track all positions where each value appears
        
        def sgn(x):
            """Map even to +1, odd to -1 (contribution to prefix sum)"""
            return 1 if x % 2 == 0 else -1
        
        length = 0  # Maximum balanced subarray length found so far
        prefix_sum = [0] * len(nums)  # Prefix sum array
        
        # Initialize: first element
        prefix_sum[0] = sgn(nums[0])
        occurrences[nums[0]].append(1)  # Store position (1-indexed)
        
        # Build prefix sum array
        # Key: only add sgn(nums[i]) if this is the FIRST occurrence of nums[i]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1]
            occ = occurrences[nums[i]]
            if not occ:
                # First occurrence of this value - add its contribution
                prefix_sum[i] += sgn(nums[i])
            occ.append(i + 1)  # Store position (1-indexed)
        
        # Build segment tree from prefix sums
        seg = SegmentTree(prefix_sum)
        
        # Iterate over all possible left boundaries
        for i in range(len(nums)):
            # Optimization: skip if we can't improve current best
            if i + length >= len(nums):
                break
            
            # Find rightmost position >= i + length + 1 where prefix_sum = 0
            # This gives us a balanced subarray [i, result-1] in 0-indexed terms
            result = seg.find_last(i + length + 1, 0)  # 1-indexed search
            if result != -1:
                length = max(length, result - i)  # result is 1-indexed, i is 0-indexed
            
            # Remove contribution of nums[i] as we move left boundary forward
            next_pos = len(nums) + 1
            occurrences[nums[i]].popleft()  # Remove current position
            if occurrences[nums[i]]:
                next_pos = occurrences[nums[i]][0]  # Next occurrence (1-indexed)
            
            # Subtract nums[i]'s contribution from range [i+1, next_pos-1] (1-indexed)
            # This is because nums[i] was contributing to all positions >= i
            # Now it should only contribute to positions >= next_pos
            seg.add(i + 1, next_pos - 1, -sgn(nums[i]))
        
        return length
    

#I would have never have gotten a solution. This was all generated by Claude,
#all I did was provide ideas and potential methods to make it happen.

#The problem started with me looking at the hints after my sliding window attempt failed
#since the hist mentioned a lazy segment tree, I asked caude to construct this class fro me to use, fit with
#all of the required methods. 
#   The purpose of this is to maintain a prefix sum array that tracks the difference between distinct even and
#   odd numbers
#using this, we move through the array, treating each position as a potential left boundary of a balanced subarray.
# For each left boundary, we query the segment tree to find the rightmost position where the prefix sum is zero
#   (indicating a balanced subarray).
# We also update the segment tree to reflect the removal of the left boundary's contribution as we move it forward.

#=====COMPLEXITY ANALYSIS=====
#Time Complexity: O(n log n) due to segment tree operations for each of the n positions.
#Space Complexity: O(n) for the segment tree and auxiliary data structures.

#=====OVERALL=====
#I would have never have gotten this solction on my own.
#I understood that tracking positive and negative contributions to a prefix sum could help
# identify balanced subarrays, but I couldn't figure out how to efficiently maintain and query this information.