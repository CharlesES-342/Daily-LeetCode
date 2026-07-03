'''
The Day that Bella was put down :(
We miss you Bella
'''

# 3620. Network Recovery Pathways

# You are given a directed acyclic graph of n nodes numbered from 0 to n − 1. This is represented by a 2D array edges of length m, where edges[i] = [ui, vi, costi] indicates a one‑way communication from node ui to node vi with a recovery cost of costi.
# Some nodes may be offline. You are given a boolean array online where online[i] = true means node i is online. Nodes 0 and n − 1 are always online.
# A path from 0 to n − 1 is valid if:
# All intermediate nodes on the path are online.
# The total recovery cost of all edges on the path does not exceed k.
# For each valid path, define its score as the minimum edge‑cost along that path.
# Return the maximum path score (i.e., the largest minimum-edge cost) among all valid paths. If no valid path exists, return -1.

# Example 1:
# Input: edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [true,true,true,true], k = 10
# Output: 3
# Explanation:
# The graph has two possible routes from node 0 to node 3:
# Path 0 → 1 → 3
# Total cost = 5 + 10 = 15, which exceeds k (15 > 10), so this path is invalid.
# Path 0 → 2 → 3
# Total cost = 3 + 4 = 7 <= k, so this path is valid.
# The minimum edge‐cost along this path is min(3, 4) = 3.
# There are no other valid paths. Hence, the maximum among all valid path‐scores is 3.

# Example 2:
# Input: edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [true,true,true,false,true], k = 12
# Output: 6
# Explanation:
# Node 3 is offline, so any path passing through 3 is invalid.
# Consider the remaining routes from 0 to 4:
# Path 0 → 1 → 4
# Total cost = 7 + 5 = 12 <= k, so this path is valid.
# The minimum edge‐cost along this path is min(7, 5) = 5.
# Path 0 → 2 → 3 → 4
# Node 3 is offline, so this path is invalid regardless of cost.
# Path 0 → 2 → 4
# Total cost = 6 + 6 = 12 <= k, so this path is valid.
# The minimum edge‐cost along this path is min(6, 6) = 6.
# Among the two valid paths, their scores are 5 and 6. Therefore, the answer is 6.

# Constraints:
# n == online.length
# 2 <= n <= 5 * 104
# 0 <= m == edges.length <= min(105, n * (n - 1) / 2)
# edges[i] = [ui, vi, costi]
# 0 <= ui, vi < n
# ui != vi
# 0 <= costi <= 109
# 0 <= k <= 5 * 1013
# online[i] is either true or false, and both online[0] and online[n − 1] are true.
# The given graph is a directed acyclic graph.

'''
My initial approach was wrong as I mis-understood the problem. I read it incorrectly and thought that
you were wanting to find the length of the minimum path from one node to another following edges, however,
the idea was to give the minimum stops to get from S to B given teh cost between them was atmost k.

My appraoch (whick was wrong) was to:
Remove edges containing nodes that are offline
Perfoem Dijkstras over the remaining edges, returning the minimum length of the path.
Then back pedel throguht to determine the number of nodes on the route by using BFS over the
possible paths when removing a route until you get back to the start of value 0
'''

'''
In this revised stratagy:
Thinking as th eproblem being trains and station, if a station is closed, you cant go thorugh it. How
many stops do you need to get from S to B given the cost (or time) between them is atmost k.
1. remove offline nodes/stops
2. form adjacency table of connecitons and what can be done
3. order nodes in topological order (which come before what, and have to coe before)
4. for each node in topological order, check if it can be reached from the start node (0) and if so,
    check if it can reach the end node (n-1) with a cost of atmost k. If so, update the maximum score
    (minimum edge cost) for that path.
5. using Binary search, find the maximum score (minimum edge cost) that can be achieved for a valid path
    from 0 to n-1 with a total cost of atmost k.
6. return this value
'''
from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        # Dynamically determine the number of nodes from the online array length
        n = len(online)
        
        # Step 1: Filter out edges connected to offline intermediate nodes
        valid_edges = []
        for u, v, cost in edges:
            if online[u] and online[v]:
                valid_edges.append((u, v, cost))
        
        # Step 2: Build an adjacency list for topological sort
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        
        for u, v, cost in valid_edges:
            adj[u].append((v, cost))
            in_degree[v] += 1
            
        # Step 3: Standard Kahn's algorithm for Topological Sort
        topo_order = []
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v, _ in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        # Step 4: Define the helper check function using DP over the Topo Sort
        def check(min_edge_threshold):
            dist = [float('inf')] * n
            dist[0] = 0
            
            for u in topo_order:
                if dist[u] == float('inf'):
                    continue
                for v, cost in adj[u]:
                    if cost >= min_edge_threshold:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                            
            return dist[n - 1] <= k

        # Step 5: Binary Search for the maximum possible minimum-edge cost
        low = 0
        high = max([cost for _, _, cost in edges]) if edges else 0
        ans = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if check(mid):
                ans = mid      
                low = mid + 1  
            else:
                high = mid - 1 
                
        return ans