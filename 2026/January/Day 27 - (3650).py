# 3650. Minimum COst Path with Edge Reversals

# You are given a directed, weighted graph with n nodes labeled from 0 to n - 1, and an array edges
# where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with cost wi.
# Each node ui has a switch that can be used at most once: when you arrive at ui and have not yet
# used its switch, you may activate it on one of its incoming edges vi → ui reverse that edge to
# ui → vi and immediately traverse it.
# The reversal is only valid for that single move, and using a reversed edge costs 2 * wi.
# Return the minimum total cost to travel from node 0 to node n - 1. If it is not possible,
# return -1.


# Example 1:
# Input: n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
# Output: 5
# Explanation:
# Use the path 0 → 1 (cost 3).
# At node 1 reverse the original edge 3 → 1 into 1 → 3 and traverse it at cost 2 * 1 = 2.
# Total cost is 3 + 2 = 5.

# Example 2:
# Input: n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]
# Output: 3
# Explanation:
# No reversal is needed. Take the path 0 → 2 (cost 1), then 2 → 1 (cost 1), then 1 → 3 (cost 1).
# Total cost is 1 + 1 + 1 = 3.


# Constraints:
# 2 <= n <= 5 * 104
# 1 <= edges.length <= 105
# edges[i] = [ui, vi, wi]
# 0 <= ui, vi <= n - 1
# 1 <= wi <= 1000




import heapq

class Solution(object):
    def minCost(self, n, edges):
        # Add all reverse edges
        temp = len(edges)
        for i in range(temp):
            edge = edges[i]
            edges.append([edge[1], edge[0], 2*edge[2]])
        
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, weight in edges:
            graph[u].append((v, weight))
        
        # Initialize distances
        distances = [float('inf')] * n
        distances[0] = 0
        
        # Priority queue: (cost, node)
        pq = [(0, 0)]
        
        while pq:
            current_cost, node = heapq.heappop(pq)
            
            # If we reached the end, return the cost
            if node == n - 1:
                return current_cost
            
            # Skip if we've already found a better path
            if current_cost > distances[node]:
                continue
            
            # Check all neighbors
            for neighbor, weight in graph[node]:
                new_cost = current_cost + weight
                
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))
        
        return -1
    
#why this works?
# rather than taking into account which nodes are switched, since the final solution will only have
# on instance of a node in it (as there cannot be negative edges and no loops), we ensure that there
# is atmost one reversal per node. Thus we can add all reversed edges to the graph at the start,
# and use dijkstra's algorithm to find the shortest path from 0 to n-1

# initially I wrote the Dijkstra's algorithm incorrectly and used Claud to find my issue
# (i forgot to got to n-1 nodes, not n)
# claud told me it would be incorrect for the p[roblem, but I was sure I could do it my way and after
# some looking at others responces, I relised I was correct and he has now been informed