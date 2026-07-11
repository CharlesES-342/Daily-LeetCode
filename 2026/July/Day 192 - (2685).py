# 2685. Count the Number of Complete Components

# You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.
# Return the number of complete connected components of the graph.
# A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
# A connected component is said to be complete if there exists an edge between every pair of its vertices.

# Example 1:
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# Output: 3
# Explanation: From the picture above, one can see that all of the components of this graph are complete.

# Example 2:
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
# Output: 1
# Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.

# Constraints:
# 1 <= n <= 50
# 0 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated edges.


from collections import defaultdict

class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #1. form a graph
        #2. go thorugh connected components to determine a component
        #3. count the number of edges (m*(m-1) / 2) to chekc for completeness (remove nodes form final check that were involved in the check)

        # 1. Build the adjacency list to represent the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        complete_components_count = 0
        
        # Helper function to traverse the component
        def dfs(node, component_nodes):
            visited[node] = True
            component_nodes.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component_nodes)

        # 2. Go through each node to find connected components
        for i in range(n):
            if not visited[i]:
                component_nodes = []
                dfs(i, component_nodes)
                
                # 3. Check for completeness
                m = len(component_nodes)
                actual_edges_count = 0
                
                # Count the total degree of all nodes in this component
                for node in component_nodes:
                    actual_edges_count += len(graph[node])
                
                # Since it's an undirected graph, each edge is counted twice
                actual_edges_count //= 2
                
                # A component is complete if it has exactly m * (m - 1) / 2 edges
                expected_edges_count = (m * (m - 1)) // 2
                if actual_edges_count == expected_edges_count:
                    complete_components_count += 1
                    
        return complete_components_count