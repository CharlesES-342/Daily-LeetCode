# 3559. Number of Ways to Assign Edge Weights II

# There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1. The tree is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi.
# Initially, all edges have a weight of 0. You must assign each edge a weight of either 1 or 2.
# The cost of a path between any two nodes u and v is the total weight of all edges in the path connecting them.
# You are given a 2D integer array queries. For each queries[i] = [ui, vi], determine the number of ways to assign weights to edges in the path such that the cost of the path between ui and vi is odd.
# Return an array answer, where answer[i] is the number of valid assignments for queries[i].
# Since the answer may be large, apply modulo 109 + 7 to each answer[i].
# Note: For each query, disregard all edges not in the path between node ui and vi.

# Example 1:
# Input: edges = [[1,2]], queries = [[1,1],[1,2]]
# Output: [0,1]
# Explanation:
# Query [1,1]: The path from Node 1 to itself consists of no edges, so the cost is 0. Thus, the number of valid assignments is 0.
# Query [1,2]: The path from Node 1 to Node 2 consists of one edge (1 → 2). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

# Example 2:
# Input: edges = [[1,2],[1,3],[3,4],[3,5]], queries = [[1,4],[3,4],[2,5]]
# Output: [2,1,4]
# Explanation:
# Query [1,4]: The path from Node 1 to Node 4 consists of two edges (1 → 3 and 3 → 4). Assigning weights (1,2) or (2,1) results in an odd cost. Thus, the number of valid assignments is 2.
# Query [3,4]: The path from Node 3 to Node 4 consists of one edge (3 → 4). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.
# Query [2,5]: The path from Node 2 to Node 5 consists of three edges (2 → 1, 1 → 3, and 3 → 5). Assigning (1,2,2), (2,1,2), (2,2,1), or (1,1,1) makes the cost odd. Thus, the number of valid assignments is 4.

# Constraints:
# 2 <= n <= 105
# edges.length == n - 1
# edges[i] == [ui, vi]
# 1 <= queries.length <= 105
# queries[i] == [ui, vi]
# 1 <= ui, vi <= n
# edges represents a valid tree.



class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(edges) + 1
        
        # 1. Form the tree (Adjacency List)
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # LOG is the maximum power of 2 needed for binary lifting (2^17 > 10^5)
        LOG = 17 
        depth = [0] * (n + 1)
        # parent[k][v] stores the (2^k)-th ancestor of node v
        parent = [[-1] * (n + 1) for _ in range(LOG)]
        
        # 2. DFS to populate immediate parents (2^0) and depths
        stack = [(1, -1, 0)] # (node, parent_node, current_depth)
        visited = [False] * (n + 1)
        
        while stack:
            u, p, d = stack.pop()
            if visited[u]:
                continue
            visited[u] = True
            depth[u] = d
            parent[0][u] = p
            
            for v in graph[u]:
                if v != p:
                    stack.append((v, u, d + 1))
                    
        # 3. Compute the binary lifting sparse table
        # this allows jumping up by powers of 2 (to parents) allowing for movement in log(n) time rather than jumping to every element at that depth
        for k in range(1, LOG):
            for v in range(1, n + 1):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]
                    
        # Helper function to find Lowest Common Ancestor using Binary Lifting
        def get_lca(u, v):
            '''
            Args: u,v (2 nodes)
            Return: the lowest common ancestor in the tree
            Method:
                Works by moving the nodes up the tree until they are at the same level/have a common direct parent, this parent is the LCA
            '''
            if depth[u] < depth[v]:
                u, v = v, u
                
            # Bring both nodes to the same depth
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if (diff >> k) & 1:
                    u = parent[k][u]
                    
            if u == v:
                return u
                
            # Lift both nodes simultaneously right before their common ancestor
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
                    
            return parent[0][u]

        # 4. Process each query
        ans = []
        for u, v in queries:
            if u == v: #if the same, no distance
                ans.append(0)
            else:
                lca_node = get_lca(u, v)
                # Distance formula in a tree: depth[u] + depth[v] - 2 * depth[LCA]
                # the distance is that to the common ancestor and back down to the other node
                distance = depth[u] + depth[v] - 2 * depth[lca_node]
                
                # Number of ways to get an odd path sum is 2^(distance - 1)
                ans.append(pow(2, distance - 1, MOD)) # minimum distance acheivable form then parity combinations (the most occurances of 1 possible, plus the minimum number of 2's)
                
        return ans
    
    '''
    Despite the code being generated by Gemini.ai, this follows my thought process exactly (as I asked it to use
    my understanding as the prompt for the code). The one section that I was not so sure on is the use of the
    LOG variable. However, following review, I completely undertand the use and am annoyed that I wanted to do it
    the long way (jumping up the tree one by one) instead of using binary lifting. I think the main reason for the
    lack of understanding in this section was due to the naming conventions used, I was unfarmiliar with the term
    "binary lifting" and so didnt realise that the method was what it said.
    In heindsight, this is exactly how I would ave done it, with the increased efficiency from the Binary Lifting.
    With every other aspect being how I planned.
    It was a nice addition to yesterday's problem, as despite the added complexity, many of the learnt stratacgies
    could be carried over.
    '''