# 1722. Minimize Hamming Distance After Swap Operations

# You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source. Note that you can swap elements at a specific pair of indices multiple times and in any order.
# The Hamming distance of two arrays of the same length, source and target, is the number of positions where the elements are different. Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).
# Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.

# Example 1:
# Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
# Output: 1
# Explanation: source can be transformed the following way:
# - Swap indices 0 and 1: source = [2,1,3,4]
# - Swap indices 2 and 3: source = [2,1,4,3]
# The Hamming distance of source and target is 1 as they differ in 1 position: index 3.

# Example 2:
# Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
# Output: 2
# Explanation: There are no allowed swaps.
# The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.

# Example 3:
# Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
# Output: 0

# Constraints:
# n == source.length == target.length
# 1 <= n <= 105
# 1 <= source[i], target[i] <= 105
# 0 <= allowedSwaps.length <= 105
# allowedSwaps[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi

from collections import defaultdict, Counter

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        # form a list where each position refects what elements could potentially be there (from any number of swaps)
        # then compaire this to the source, by how much do they differ (remove a map in the event a value has been used already - to avoid re-using)

        # since the order of where the miss-match is is not a problem (just the count) we can follow a first come first serve approach
        
        n = len(source)
        parent = list(range(n))

        # Union-Find: Helper to find the "root" of a group
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        # Union-Find: Connect two indices
        for a, b in allowedSwaps:
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_a] = root_b

        # Group source and target elements by their root parent
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        hamming_dist = 0
        for root in groups:
            indices = groups[root]
            
            # Count elements in source vs target for THIS specific group
            source_counts = Counter(source[i] for i in indices)
            target_counts = Counter(target[i] for i in indices)
            
            # Elements in target that exist in source (within this group)
            matches = 0
            for val in target_counts:
                matches += min(target_counts[val], source_counts[val])
            
            # The distance for this group is (total elements - matches)
            hamming_dist += (len(indices) - matches)

        return hamming_dist

    # all my logic (my step by step breakdown) but I got gemini to write the code to get this exact answer. Dissertation is now handed in and today is a chill day, so not trying!