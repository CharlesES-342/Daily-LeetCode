# 3532. Path Existence Queries in a Graph I

# You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.
# You are also given an integer array nums of length n sorted in non-decreasing order, and an integer maxDiff.
# An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).
# You are also given a 2D integer array queries. For each queries[i] = [ui, vi], determine whether there exists a path between nodes ui and vi.
# Return a boolean array answer, where answer[i] is true if there exists a path between ui and vi in the ith query and false otherwise.

# Example 1:
# Input: n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]
# Output: [true,false]
# Explanation:
# Query [0,0]: Node 0 has a trivial path to itself.
# Query [0,1]: There is no edge between Node 0 and Node 1 because |nums[0] - nums[1]| = |1 - 3| = 2, which is greater than maxDiff.
# Thus, the final answer after processing all the queries is [true, false].

# Example 2:
# Input: n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]
# Output: [false,false,true,true]
# Explanation:
# The resulting graph is:
# Query [0,1]: There is no edge between Node 0 and Node 1 because |nums[0] - nums[1]| = |2 - 5| = 3, which is greater than maxDiff.
# Query [0,2]: There is no edge between Node 0 and Node 2 because |nums[0] - nums[2]| = |2 - 6| = 4, which is greater than maxDiff.
# Query [1,3]: There is a path between Node 1 and Node 3 through Node 2 since |nums[1] - nums[2]| = |5 - 6| = 1 and |nums[2] - nums[3]| = |6 - 8| = 2, both of which are within maxDiff.
# Query [2,3]: There is an edge between Node 2 and Node 3 because |nums[2] - nums[3]| = |6 - 8| = 2, which is equal to maxDiff.
# Thus, the final answer after processing all the queries is [false, false, true, true].

# Constraints:
# 1 <= n == nums.length <= 105
# 0 <= nums[i] <= 105
# nums is sorted in non-decreasing order.
# 0 <= maxDiff <= 105
# 1 <= queries.length <= 105
# queries[i] == [ui, vi]
# 0 <= ui, vi < nA

'''
My initial idea was to apply Floyd-Warshall to determine the shortest paths (these would be with the
MaxDiff threshold) which should allw for an O(1) query time. However, this gives an O(n^3) time when forming
the table.
'''
class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # 1. Initialise the table with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
            
        # 2. Correctly populate initial direct weights using elements from nums
        for i in range(n):
            for j in range(i + 1, n):
                weight = abs(nums[i] - nums[j])
                dist[i][j] = weight
                dist[j][i] = weight

        # 3. Stabilise the table (Floyd-Warshall minimax path)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    bottleneck = max(dist[i][k], dist[k][j])
                    if bottleneck < dist[i][j]:
                        dist[i][j] = bottleneck

        # 4. Process queries
        results = []
        for u, v in queries:
            if dist[u][v] <= maxDiff:
                results.append(True)
            else:
                results.append(False)
                
        return results


'''
The next approach takes into account each step. Each node can only move to it s neighbours, and so its not a question of how far, rather if it is possible, then the associated value
'''
class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # Preprocess the components into continuous segments
        # component_id[i] will store which cluster node i belongs to
        component_id = [0] * n
        curr_id = 0
        
        for i in range(1, n):
            # If the gap between adjacent elements is too large, it's a new component
            if abs(nums[i] - nums[i-1]) > maxDiff:
                curr_id += 1
            component_id[i] = curr_id
            
        # Process each query in O(1) time
        results = []
        for u, v in queries:
            # If they share the same component ID, a valid continuous path exists
            if component_id[u] == component_id[v]:
                results.append(True)
            else:
                results.append(False)
                
        return results