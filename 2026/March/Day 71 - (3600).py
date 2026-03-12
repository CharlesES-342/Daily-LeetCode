# 3600. Maximize Spanning Tree Stability with Upgrades

# You are given an integer n, representing n nodes numbered from 0 to n - 1 and a list of edges, where edges[i] = [ui, vi, si, musti]:
# ui and vi indicates an undirected edge between nodes ui and vi.
# si is the strength of the edge.
# musti is an integer (0 or 1). If musti == 1, the edge must be included in the spanning tree. These edges cannot be upgraded.
# You are also given an integer k, the maximum number of upgrades you can perform. Each upgrade doubles the strength of an edge, and each eligible edge (with musti == 0)
# can be upgraded at most once.
# The stability of a spanning tree is defined as the minimum strength score among all edges included in it.
# Return the maximum possible stability of any valid spanning tree. If it is impossible to connect all nodes, return -1.
# Note: A spanning tree of a graph with n nodes is a subset of the edges that connects all nodes together (i.e. the graph is connected) without forming any cycles, and
# uses exactly n - 1 edges.

# Example 1:
# Input: n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1
# Output: 2
# Explanation:
# Edge [0,1] with strength = 2 must be included in the spanning tree.
# Edge [1,2] is optional and can be upgraded from 3 to 6 using one upgrade.
# The resulting spanning tree includes these two edges with strengths 2 and 6.
# The minimum strength in the spanning tree is 2, which is the maximum possible stability.

# Example 2:
# Input: n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2
# Output: 6
# Explanation:
# Since all edges are optional and up to k = 2 upgrades are allowed.
# Upgrade edges [0,1] from 4 to 8 and [1,2] from 3 to 6.
# The resulting spanning tree includes these two edges with strengths 8 and 6.
# The minimum strength in the tree is 6, which is the maximum possible stability.

# Example 3:
# Input: n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0
# Output: -1
# Explanation:
# All edges are mandatory and form a cycle, which violates the spanning tree property of acyclicity. Thus, the answer is -1.

# Constraints:
# 2 <= n <= 105
# 1 <= edges.length <= 105
# edges[i] = [ui, vi, si, musti]
# 0 <= ui, vi < n
# ui != vi
# 1 <= si <= 105
# musti is either 0 or 1.
# 0 <= k <= n
# There are no duplicate edges.


class Solution(object):
    def maxStability(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
       #check if a spanning tree is even possible with ALL edges
        def get_parent(parent, i):
            if parent[i] == i: return i
            parent[i] = get_parent(parent, parent[i])
            return parent[i]

        def can_form_tree(min_val):
            parent = list(range(n))
            edges_count = 0
            upgrades_used = 0
            
            #Mandatory edges MUST be used, but only if they meet min_val
            #Optional edges can be used if si >= min_val or 2*si >= min_val
            
            #check if mandatory edges alone form a cycle
            mandatory_edges = []
            for u, v, s, must in edges:
                if must == 1:
                    if s < min_val: return False #mandatory edge fails requirement
                    root_u = get_parent(parent, u)
                    root_v = get_parent(parent, v)
                    if root_u == root_v: return False # Cycle in mandatory edges
                    parent[root_u] = root_v
                    edges_count += 1
            
            #add optional edges that DON'T need upgrades
            for u, v, s, must in edges:
                if must == 0 and s >= min_val:
                    root_u = get_parent(parent, u)
                    root_v = get_parent(parent, v)
                    if root_u != root_v:
                        parent[root_u] = root_v
                        edges_count += 1
            
            #add optional edges that DO need upgrades (up to k)
            for u, v, s, must in edges:
                if must == 0 and s < min_val and 2*s >= min_val:
                    if upgrades_used < k:
                        root_u = get_parent(parent, u)
                        root_v = get_parent(parent, v)
                        if root_u != root_v:
                            parent[root_u] = root_v
                            edges_count += 1
                            upgrades_used += 1
                            
            return edges_count == n - 1

        # Binary Search for the maximum possible min_val
        low = 1
        high = 200000
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_form_tree(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
    

'''
How It Works:
    1. By binary search, of all possible values 0 - 2x10^5, see if you can form an tree os size
    atleasst this value
    2. DSU (Disjoint Set Union) - keep track of the connected nodes
        If 2 nodes have the same parent then they are connected
        Check to see if a loop is formed before adding it
    3. 'can_form_tree' used to check if all of the requirements are valid/fulfilled
'''
#this follows the hints provided by the question. Code was generated by Gemini.ai
#initially, I didnt understand how it owrked, but I decided to read th ecode and make sense of it
#now i understand how it works