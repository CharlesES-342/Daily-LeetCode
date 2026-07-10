# 3534. Path Existence Queries in a Graph II

# You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.
# You are also given an integer array nums of length n and an integer maxDiff.
# An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).
# You are also given a 2D integer array queries. For each queries[i] = [ui, vi], find the minimum distance between nodes ui and vi. If no path exists between the two nodes, return -1 for that query.
# Return an array answer, where answer[i] is the result of the ith query.
# Note: The edges between the nodes are unweighted.

# Example 1:
# Input: n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]
# Output: [1,1]
# Explanation:
# The resulting graph is:
# Query	Shortest Path	Minimum Distance
# [0, 3]	0 → 3	1
# [2, 4]	2 → 4	1
# Thus, the output is [1, 1].

# Example 2:
# Input: n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]]
# Output: [1,2,-1,1]
# Explanation:
# The resulting graph is:
# Query	Shortest Path	Minimum Distance
# [0, 1]	0 → 1	1
# [0, 2]	0 → 1 → 2	2
# [2, 3]	None	-1
# [4, 3]	3 → 4	1
# Thus, the output is [1, 2, -1, 1].

# Example 3:
# Input: n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]]
# Output: [0,-1,-1]
# Explanation:
# There are no edges between any two nodes because:
# Nodes 0 and 1: |nums[0] - nums[1]| = |3 - 6| = 3 > 1
# Nodes 0 and 2: |nums[0] - nums[2]| = |3 - 1| = 2 > 1
# Nodes 1 and 2: |nums[1] - nums[2]| = |6 - 1| = 5 > 1
# Thus, no node can reach any other node, and the output is [0, -1, -1].

# Constraints:
# 1 <= n == nums.length <= 105
# 0 <= nums[i] <= 105
# 0 <= maxDiff <= 105
# 1 <= queries.length <= 105
# queries[i] == [ui, vi]
# 0 <= ui, vi < n

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # sort nodes to allow for the formaiton of a binary tree
        #   since there is no edge weight (weightless graph) there is zero cost to a route, and so any path can be taken so long as it starts and ends in the correct place (so long as they are joined)
        #   new graphs are only formed if the difference > MaxDiff, so a new graph would be formed
        
        # Pair each number with its original index and sort by value
        sorted_pairs = sorted((nums[i], i) for i in range(n))
        sorted_values = [p[0] for p in sorted_pairs]
        
        # Map from original index to its position in the sorted array
        pos_in_sorted = [0] * n
        for sorted_idx, (_, orig_idx) in enumerate(sorted_pairs):
            pos_in_sorted[orig_idx] = sorted_idx
            
        LOG_N = 18
        # up[i][j] stores the 2^j-th greedy step from the i-th sorted node
        up = [[-1] * LOG_N for _ in range(n)]
        
        # Step 1: Find the immediate greedy parent for each sorted node
        for i in range(n):
            max_reachable_val = sorted_values[i] + maxDiff
            # Find the largest value less than or equal to max_reachable_val
            idx = bisect.bisect_right(sorted_values, max_reachable_val) - 1
            if idx > i:
                up[i][0] = idx
            else:
                up[i][0] = -1  # Cannot move forward to any larger element
                
        # Step 2: Build the binary lifting table
        for j in range(1, LOG_N):
            for i in range(n):
                if up[i][j-1] != -1:
                    up[i][j] = up[up[i][j-1]][j-1]
                else:
                    up[i][j] = -1
                    
        # Step 3: Process queries
        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
                continue
                
            # Get their positions in the sorted array
            idx_u = pos_in_sorted[u]
            idx_v = pos_in_sorted[v]
            
            # always jump from smaller to larger (just swap them around)
            if idx_u > idx_v:
                idx_u, idx_v = idx_v, idx_u
                
            # If directly connected
            if sorted_values[idx_v] - sorted_values[idx_u] <= maxDiff:
                answer.append(1)
                continue
                
            # Lift up to find the number of steps
            steps = 0
            curr = idx_u
            
            # move up to find a common parent
            for j in range(LOG_N - 1, -1, -1):
                # If jumping 2^j steps doesn't reach or overshoot idx_v, take the jump
                if up[curr][j] != -1 and up[curr][j] < idx_v:
                    curr = up[curr][j]
                    steps += (1 << j)
            
            # Take one final step to try to land on or past idx_v
            curr = up[curr][0]
            steps += 1
            
            # If the final step is valid and reaches or overshoots idx_v, a path exists
            if curr != -1 and curr >= idx_v:
                answer.append(steps)
            else:
                answer.append(-1)
                
        return answer
    
    '''
    Code generated by Gemini.ai based on my thought processes:
    .Leap-frogging (Binary jumping) allows for efficient pathfinding in the sorted graph by not looking at all connected nodes
        rather jumping in the direction of the target node (as far as the MaxDiff will allow) and then checking if the jump has overshot.
        This formed a Binary Search like approach, allowing you to ind a node in OO(log(n))
    .Count the intermediate steps taken to reach the target node, and if the target node is reached, return the number of steps taken.
        Else, return -1 if the target node is unreachable (be this because it is not connected or because
        the MaxDiff is too small - the seporation too large).
    '''